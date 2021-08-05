# Generated by Django 3.2.5 on 2021-08-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_beverages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('SPECIALITY', 'SPECIALITY'), ('RING FILLED', 'RING FILLED'), ('CLASSIC', 'CLASSIC')], max_length=255)),
                ('price', models.FloatField()),
                ('desc', models.TextField()),
                ('calories', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.CharField(choices=[('1KG', '1KG'), ('5KG', '2KG'), ('10KG', '10KG')], max_length=255)),
                ('price', models.FloatField()),
                ('desc', models.TextField()),
            ],
        ),
    ]