# Generated by Django 5.0.6 on 2024-06-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_formdata_remove_uses_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='pics',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='onkar_pics/'),
        ),
    ]
