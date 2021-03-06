# Generated by Django 3.2.5 on 2021-08-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beverages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price_s', models.IntegerField()),
                ('price_m', models.IntegerField()),
                ('price_l', models.IntegerField()),
                ('desc', models.IntegerField()),
                ('type', models.CharField(choices=[('COLD', 'COLD'), ('HOT', 'HOT'), ('SMOOTHIE', 'SMOOTHIE'), ('PROMO', 'PROMO'), ('LUNCH', 'LUNCH'), ('BREAKFAST', 'BREAKFAST'), ('SPECIAL', 'SPECIAL'), ('DONUT', 'DONUT')], max_length=200)),
            ],
        ),
    ]
