# Generated by Django 3.2.6 on 2021-08-10 23:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]