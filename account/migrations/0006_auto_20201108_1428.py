# Generated by Django 3.1.3 on 2020-11-08 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_order_cas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='customers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customers'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='tag',
            field=models.ManyToManyField(to='account.Tag'),
        ),
    ]
