# Generated by Django 3.2.4 on 2021-06-15 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technicalcourses', '0003_alter_allcourses_startedfrom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allcourses',
            name='startedfrom',
        ),
    ]
