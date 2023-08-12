# Generated by Django 4.2.3 on 2023-08-03 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
        ('asosiy', '0003_alter_mahsulot_son'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatistikaViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('summa', models.PositiveIntegerField()),
                ('tolangan_summa', models.PositiveIntegerField()),
                ('nasiya', models.PositiveIntegerField()),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('mijoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mijoz')),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.omborxona')),
            ],
        ),
    ]