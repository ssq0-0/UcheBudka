# Generated by Django 5.0.1 on 2024-02-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_subject', models.CharField(max_length=50)),
                ('task_text', models.TextField()),
                ('fact_answer', models.TextField()),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
