# Generated by Django 3.2.8 on 2021-11-27 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_comment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='profile',
            new_name='author',
        ),
    ]
