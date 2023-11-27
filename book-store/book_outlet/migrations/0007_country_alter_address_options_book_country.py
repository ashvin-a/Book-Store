# Generated by Django 4.2.7 on 2023-11-27 05:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_address_author_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Entries'},
        ),
        migrations.AddField(
            model_name='book',
            name='country',
            field=models.ManyToManyField(to='book_outlet.country'),
        ),
    ]