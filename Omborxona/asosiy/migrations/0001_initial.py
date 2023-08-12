# Generated by Django 4.2.3 on 2023-08-01 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('dokon', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=20)),
                ('manzil', models.CharField(max_length=100)),
                ('qarz', models.PositiveIntegerField()),
                ('omborxona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.omborxona')),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('brend', models.CharField(max_length=50)),
                ('narx', models.PositiveIntegerField()),
                ('son', models.PositiveSmallIntegerField()),
                ('olchov', models.CharField(choices=[('dona', 'dona'), ('kg', 'kg'), ('litr', 'litr')], max_length=50)),
                ('sana', models.DateField()),
                ('omborxona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userapp.omborxona')),
            ],
        ),
    ]