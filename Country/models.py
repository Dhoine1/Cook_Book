from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User
from TuliusCookBook.models import Section


class Country(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название страны")
    info = CKEditor5Field(verbose_name="О стране", config_name='extends', blank=True)
    banner = models.ImageField(upload_to='country/', null=True, blank=True)
    flag = models.ImageField(upload_to='country/flags/', null=True, blank=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        indexes = [models.Index(fields=['title', ])]

    def __str__(self):
        return f'{self.title}'


class CountryReceipt(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название блюда')
    ingredient = CKEditor5Field(verbose_name="Ингридиенты", config_name='extends', blank=True)
    recipe_text = CKEditor5Field(verbose_name='Текст рецепта', config_name='extends', blank=True)
    about = CKEditor5Field(verbose_name='О блюде', blank=True, config_name='extends')
    description = models.TextField(verbose_name='Краткая информация')
    foto = models.CharField(max_length=1024, verbose_name="Ссылка на фото")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    time_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        indexes = [models.Index(fields=['name', ])]

    def __str__(self):
        return f'{self.name} - {self.country}'

    def get_absolute_url(self):
        return f'/countryreceipts/receipt/{self.pk}'


class CountryComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    receipt = models.ForeignKey(CountryReceipt, on_delete=models.CASCADE)
    time_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.text}. Автор: {self.author.profile.nikname}'
