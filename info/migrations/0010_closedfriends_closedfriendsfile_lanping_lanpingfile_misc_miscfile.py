# Generated by Django 2.2 on 2023-12-06 14:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_auto_20231206_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosedFriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='ClosedFriendsFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.FileField(upload_to='ClosedFriendFiles')),
            ],
        ),
        migrations.CreateModel(
            name='Lanping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='LanpingFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.FileField(upload_to='LanpingFiles')),
            ],
        ),
        migrations.CreateModel(
            name='Misc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='MiscFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.FileField(upload_to='MiscFiles')),
            ],
        ),
    ]