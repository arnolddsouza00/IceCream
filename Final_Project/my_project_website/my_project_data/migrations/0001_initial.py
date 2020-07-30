# Generated by Django 2.2 on 2020-07-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=300)),
                ('email_id', models.CharField(blank=True, max_length=300)),
                ('contact_number', models.CharField(blank=True, max_length=300)),
                ('message', models.TextField(blank=True, max_length=3000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact Form',
                'verbose_name_plural': 'Contact Form Data',
            },
        ),
    ]