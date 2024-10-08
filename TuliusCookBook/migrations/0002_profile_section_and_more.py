# Generated by Django 4.2.14 on 2024-07-31 12:23

import TuliusCookBook.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TuliusCookBook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nikname', models.CharField(max_length=64, verbose_name='Ник')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', validators=[TuliusCookBook.models.Profile.validate_image])),
                ('signature', models.CharField(max_length=512, null=True, verbose_name='Подпись')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=128, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.AddIndex(
            model_name='catalogstories',
            index=models.Index(fields=['title'], name='TuliusCookB_title_ff87c5_idx'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
