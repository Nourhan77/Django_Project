# Generated by Django 4.1.2 on 2022-10-18 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_project_donate_project_total_donations_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='total_donations',
            new_name='donate',
        ),
    ]
