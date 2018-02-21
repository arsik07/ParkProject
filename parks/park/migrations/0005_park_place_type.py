# Generated by Django 2.0.2 on 2018-02-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0004_review_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='place_type',
            field=models.CharField(choices=[('Pa', 'Парки'), ('Ca', 'Кафе'), ('Aq', 'Аквапарки'), ('Ac', 'Активный отдых'), ('Ci', 'Кинотеатры')], default='Aq', max_length=200),
        ),
    ]
