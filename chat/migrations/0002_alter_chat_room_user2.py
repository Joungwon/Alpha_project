# Generated by Django 3.2.18 on 2023-04-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_room',
            name='user2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]