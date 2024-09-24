from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class CatalogStories(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    description = models.TextField(null=True, verbose_name="Аннотация")
    link_to_story = models.CharField(max_length=512, null=True, verbose_name="Ссылка на сюжет")
    link_to_image = models.CharField(max_length=512, null=True, verbose_name="Ссылка на карту")

    class Meta:
        verbose_name = 'Сюжет'
        verbose_name_plural = 'Сюжеты'
        indexes = [models.Index(fields=['title', ])]

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=32, unique=True, verbose_name="Название")
    description = models.CharField(max_length=128, verbose_name="Описание")

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title


class Profile(models.Model):
    def validate_image(self):
        filesize = self.file.size
        limit = 512
        if filesize > limit * 1024:
            raise ValidationError("Изображение не должно быть больше %sKB" % str(limit))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nikname = models.CharField(max_length=64, verbose_name="Ник")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, validators=[validate_image])
    signature = models.CharField(max_length=512, blank=True, null=True, verbose_name="Подпись")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        indexes = [models.Index(fields=['nikname', ])]

    def __str__(self):
        return f'{self.user} - {self.nikname}'


class Recipe(models.Model):
    def validate_image(self):
        filesize = self.file.size
        limit = 3
        if filesize > limit * 1024 * 1024:
            raise ValidationError("Изображение не должно быть больше %sMB" % str(limit))

    dish_name = models.CharField(max_length=128, verbose_name='Название блюда')
    ingredient = CKEditor5Field(verbose_name="Ингридиенты", config_name='extends', blank=True)
    recipe_text = CKEditor5Field(verbose_name='Текст рецепта', config_name='extends', blank=True)
    description = CKEditor5Field(verbose_name='Описание рецепта', blank=True, config_name='extends')
    image = models.ImageField(upload_to='receipt/', null=True, blank=True, validators=[validate_image])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(CatalogStories, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    time_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        indexes = [models.Index(fields=['dish_name', ])]

    def __str__(self):
        return f'{self.dish_name}. Автор: {self.author.profile.nikname}'

    def get_absolute_url(self):
        return f'/tuliuscookbook/receipt/{self.pk}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    time_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.text}. Автор: {self.author.profile.nikname}'


class Fact(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Интересный факт')
    time_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'

    def __str__(self):
        return f'{self.text}. Автор: {self.author.profile.nikname}'
