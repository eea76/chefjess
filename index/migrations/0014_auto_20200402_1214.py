# Generated by Django 3.0.4 on 2020-04-02 19:14

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20200402_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=0, size=[300, 300], upload_to='images/'),
        ),
    ]
