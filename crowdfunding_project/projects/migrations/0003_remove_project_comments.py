# Generated by Django 4.1.2 on 2022-10-15 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_comment_project_avg_rate_project_donate_project_rate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='comments',
        ),
    ]
