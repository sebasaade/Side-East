# Generated by Django 2.0.2 on 2018-11-03 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20181103_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
