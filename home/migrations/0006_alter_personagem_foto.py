# Generated by Django 3.2.2 on 2021-06-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_personagem_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personagem',
            name='Foto',
            field=models.FileField(default='foto', upload_to='fotosdabio'),
        ),
    ]