# Generated by Django 3.0.7 on 2020-06-23 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fundstrackerapp', '0007_auto_20200619_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='financial_goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='fundstrackerapp.FinancialGoal'),
        ),
    ]
