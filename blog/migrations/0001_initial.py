# Generated by Django 5.0.1 on 2024-01-10 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(upload_to='blog/imagenes/')),
                ('fecha', models.DateField(verbose_name=datetime.date.today)),
            ],
        ),
    ]