# Generated by Django 4.2.3 on 2023-08-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistika', '0002_rename_statistikaviews_statistika'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistika',
            name='olchov',
            field=models.CharField(choices=[('dona', 'dona'), ('kg', 'kg'), ('litr', 'litr')], max_length=50, null=True),
        ),
    ]
