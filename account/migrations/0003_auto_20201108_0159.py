# Generated by Django 3.1.3 on 2020-11-08 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('indore', 'indore'), ('outdore', 'outdore')], max_length=200, null=True),
        ),
    ]
