# Generated by Django 4.0.2 on 2022-03-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_slider2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='erfan', max_length=2083),
            preserve_default=False,
        ),
    ]
