# Generated by Django 4.1 on 2022-08-28 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_alter_post_downvotes_alter_post_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvotes',
        ),
    ]
