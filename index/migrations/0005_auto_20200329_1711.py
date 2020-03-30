# Generated by Django 3.0.4 on 2020-03-30 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200329_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(blank=True, null=True, to='index.Ingredient'),
        ),
    ]