# Generated by Django 4.1.2 on 2022-10-31 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('1', 'Infrastucture 8'), ('2', 'Development'), ('3', 'Product')], max_length=100, null=True),
        ),
    ]
