# Generated by Django 5.0.2 on 2024-03-03 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceGuide', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_equip',
            name='equip_name',
            field=models.ForeignKey(limit_choices_to={'category': 'E'}, on_delete=django.db.models.deletion.CASCADE, to='priceGuide.stuff'),
        ),
        migrations.AlterField(
            model_name='transaction_others',
            name='others_name',
            field=models.ForeignKey(limit_choices_to=models.Q(('category', 'U'), ('category', 'S'), ('category', 'T'), ('category', 'N'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='priceGuide.stuff'),
        ),
        migrations.AlterField(
            model_name='transaction_others',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]