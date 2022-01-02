# Generated by Django 3.1.3 on 2021-04-05 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0046_auto_20210405_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentplayer',
            name='qualifier',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='tournament_player', to='classic_tetris_project.qualifier'),
        ),
        migrations.AlterField(
            model_name='tournamentplayer',
            name='user',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tournament_players', to='classic_tetris_project.user'),
        ),
    ]