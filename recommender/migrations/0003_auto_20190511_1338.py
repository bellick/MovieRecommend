# Generated by Django 2.1.2 on 2019-05-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0002_auto_20190511_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='genres',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
