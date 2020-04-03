# Generated by Django 3.0.4 on 2020-04-03 21:21

from django.db import migrations
import django_resized.forms
import functools
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0017_auto_20200403_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=0, size=[300, 300], upload_to=functools.partial(index.models._update_filename, *(), **{'path': 'images/'})),
        ),
    ]