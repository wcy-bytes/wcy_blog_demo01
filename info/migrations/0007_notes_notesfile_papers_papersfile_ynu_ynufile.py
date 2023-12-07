# Generated by Django 2.2 on 2023-12-06 14:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20231206_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='NotesFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.FileField(upload_to='NotesFiles')),
            ],
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='PapersFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.FileField(upload_to='PapersFiles')),
            ],
        ),
        migrations.CreateModel(
            name='YNU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='YNUFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.FileField(upload_to='YNUFiles')),
            ],
        ),
    ]