# Generated by Django 3.1.2 on 2020-11-11 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0002_comment_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
