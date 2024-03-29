# Generated by Django 4.2.6 on 2023-11-08 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geoapp', '0003_geozone_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='geozone',
            options={'verbose_name': 'Геозону', 'verbose_name_plural': 'Геозоны пользователей'},
        ),
        migrations.AlterField(
            model_name='geozone',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания'),
        ),
        migrations.AlterField(
            model_name='geozone',
            name='geojson',
            field=models.TextField(verbose_name='Геоданные'),
        ),
        migrations.AlterField(
            model_name='geozone',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название геозоны'),
        ),
        migrations.AlterField(
            model_name='geozone',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
