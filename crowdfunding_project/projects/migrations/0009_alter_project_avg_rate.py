# Generated by Django 4.1.2 on 2022-10-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_comment_reported_project_reported'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='avg_rate',
            field=models.FloatField(default=1),
        ),
    ]
