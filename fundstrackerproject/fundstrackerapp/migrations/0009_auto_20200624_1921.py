# Generated by Django 3.0.7 on 2020-06-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundstrackerapp', '0008_auto_20200623_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyexpense',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='monthlyincome',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
