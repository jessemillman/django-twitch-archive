# Generated by Django 3.1 on 2020-08-14 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0019_clip_on_twitch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clip',
            old_name='on_twitch',
            new_name='deleted_on_twitch',
        ),
    ]
