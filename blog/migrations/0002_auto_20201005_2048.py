# Generated by Django 3.1.2 on 2020-10-05 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_title',
            new_name='title',
        ),
    ]
