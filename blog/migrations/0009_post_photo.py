# Generated by Django 2.1.5 on 2019-02-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190125_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
