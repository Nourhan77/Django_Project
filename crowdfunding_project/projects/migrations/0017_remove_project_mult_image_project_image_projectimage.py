# Generated by Django 4.1.2 on 2022-10-31 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_alter_project_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='mult_image',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
