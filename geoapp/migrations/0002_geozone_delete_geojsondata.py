# Generated by Django 4.2.6 on 2023-11-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geojson', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='GeoJSONData',
        ),
    ]
