# Generated by Django 4.1 on 2022-08-30 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
