# Generated by Django 2.1.5 on 2019-01-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0004_auto_20190129_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_agent',
            field=models.CharField(default='exit', max_length=200),
            preserve_default=False,
        ),
    ]
