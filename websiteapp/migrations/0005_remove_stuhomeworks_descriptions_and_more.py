# Generated by Django 5.0.7 on 2024-07-15 19:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0004_stuhomeworks_stunotes_subjecteight_subjectnine_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuhomeworks',
            name='descriptions',
        ),
        migrations.AddField(
            model_name='stuhomeworks',
            name='descripeditor',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
