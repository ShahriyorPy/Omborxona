# Generated by Django 4.2.3 on 2023-08-03 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistika', '0004_alter_statistika_nasiya_alter_statistika_summa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistika',
            name='olchov',
            field=models.CharField(choices=[('dona', 'dona'), ('kg', 'kg'), ('litr', 'litr')], max_length=150, null=True),
        ),
    ]
