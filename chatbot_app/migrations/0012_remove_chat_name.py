# Generated by Django 2.2 on 2020-04-07 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_app', '0011_auto_20200407_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='name',
        ),
    ]