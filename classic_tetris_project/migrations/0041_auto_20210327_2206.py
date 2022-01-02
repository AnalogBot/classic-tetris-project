# Generated by Django 3.1.3 on 2021-03-27 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0040_auto_20210327_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='seed_count',
            field=models.IntegerField(default=16),
            preserve_default=False,
        ),
    ]