# Generated by Django 2.2 on 2020-04-05 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_app', '0003_auto_20200404_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='chat',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_app.UserAccount'),
        ),
    ]
