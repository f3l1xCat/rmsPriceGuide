# Generated by Django 5.0.2 on 2024-03-03 15:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuff_name', models.CharField(max_length=60, unique=True)),
                ('category', models.CharField(choices=[('E', 'Equipment'), ('U', 'Usable'), ('S', 'Set-up'), ('T', 'Etc'), ('N', 'NX')], max_length=1)),
                ('stuff_image', models.ImageField(upload_to='stuff_images')),
            ],
        ),
        migrations.CreateModel(
            name='transaction_equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STR', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(200)])),
                ('DEX', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(200)])),
                ('INT', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(300)])),
                ('LUK', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(200)])),
                ('ACC', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(150)])),
                ('Avoid', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(150)])),
                ('att', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(250)])),
                ('Matt', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(300)])),
                ('slot', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(20)])),
                ('price', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('equip_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='priceGuide.stuff')),
            ],
        ),
        migrations.CreateModel(
            name='transaction_others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField(auto_now_add=True)),
                ('others_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='priceGuide.stuff')),
            ],
        ),
    ]
