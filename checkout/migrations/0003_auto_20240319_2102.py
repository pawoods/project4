# Generated by Django 3.2.23 on 2024-03-19 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20240317_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_basket',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
