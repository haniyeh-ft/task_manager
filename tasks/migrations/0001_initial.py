# Generated by Django 5.0.4 on 2024-04-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('detail', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('completed', 'Completed')], max_length=20)),
            ],
        ),
    ]
