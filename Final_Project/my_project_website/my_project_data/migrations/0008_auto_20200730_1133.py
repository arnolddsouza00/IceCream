# Generated by Django 2.2 on 2020-07-30 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_project_data', '0007_auto_20200730_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='created_at',
            new_name='submitted_at',
        ),
    ]
