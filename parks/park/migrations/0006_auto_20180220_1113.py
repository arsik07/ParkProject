# Generated by Django 2.0.2 on 2018-02-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0005_park_place_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.NullBooleanField(choices=[(None, 'Unknown'), (True, 'Good'), (False, 'Bad')]),
        ),
    ]