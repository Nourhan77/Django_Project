# Generated by Django 4.1.2 on 2022-10-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='donations',
            field=models.FloatField(null=True),
        ),
    ]
