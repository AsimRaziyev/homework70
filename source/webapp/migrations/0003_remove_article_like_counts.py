# Generated by Django 3.2.15 on 2022-09-18 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20220912_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like_counts',
        ),
    ]