# Generated by Django 3.1.4 on 2020-12-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penguin', '0006_product_owners'),
        ('users', '0008_auto_20201211_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='user_items',
            field=models.ManyToManyField(to='penguin.Product'),
        ),
    ]