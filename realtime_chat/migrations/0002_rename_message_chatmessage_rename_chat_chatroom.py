# Generated by Django 5.0.4 on 2024-05-04 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtime_chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='ChatMessage',
        ),
        migrations.RenameModel(
            old_name='Chat',
            new_name='ChatRoom',
        ),
    ]
