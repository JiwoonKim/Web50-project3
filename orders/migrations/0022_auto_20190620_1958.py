# Generated by Django 2.1.4 on 2019-06-20 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20190620_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularpizza',
            name='topping_type',
            field=models.CharField(choices=[('Cheese', 'Cheese'), ('1 Topping', '1 topping'), ('2 Toppings', '2 Toppings'), ('3 Toppings', '3 Toppings'), ('Special', 'Special')], max_length=7),
        ),
    ]
