# Generated by Django 3.2.2 on 2021-06-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_personagem_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='personagem',
            name='Foto',
            field=models.FileField(default='foto', upload_to='static'),
        ),
    ]
