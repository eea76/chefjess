# Generated by Django 3.0.4 on 2020-03-31 03:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20200329_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
