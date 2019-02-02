# Generated by Django 2.1.5 on 2019-02-02 08:49

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190201_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d'),
        ),
    ]
