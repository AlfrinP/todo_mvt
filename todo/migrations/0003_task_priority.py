# Generated by Django 5.0.4 on 2024-05-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_task_completed_remove_task_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default=None, max_length=20),
        ),
    ]
