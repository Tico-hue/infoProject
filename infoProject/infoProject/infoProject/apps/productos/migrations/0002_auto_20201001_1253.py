# Generated by Django 3.0 on 2020-10-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to='productos'),
        ),
    ]