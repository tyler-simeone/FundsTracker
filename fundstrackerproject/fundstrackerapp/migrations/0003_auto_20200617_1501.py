# Generated by Django 3.0.7 on 2020-06-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundstrackerapp', '0002_financialgoal_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialgoal',
            name='is_completed',
            field=models.BooleanField(null=True),
        ),
    ]