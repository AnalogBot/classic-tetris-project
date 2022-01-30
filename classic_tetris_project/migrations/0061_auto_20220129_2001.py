# Generated by Django 3.1.3 on 2022-01-29 20:01

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0060_auto_20220123_0527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournamentmatch',
            options={'permissions': [('restream', 'Can schedule and report restreamed matches')], 'verbose_name_plural': 'tournament matches'},
        ),
        migrations.AddField(
            model_name='tournament',
            name='details',
            field=markdownx.models.MarkdownxField(blank=True, help_text='Details to show on the tournament page'),
        ),
    ]