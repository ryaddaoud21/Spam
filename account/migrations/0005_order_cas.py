# Generated by Django 3.1.3 on 2020-11-08 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cas',
            field=models.CharField(choices=[('pending', 'pending'), ('out of delivry', 'out of delivry'), ('delivred', 'delivred')], max_length=200, null=True),
        ),
    ]
