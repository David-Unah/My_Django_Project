# Generated by Django 4.1.3 on 2022-11-16 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_song_date_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyrics',
            name='Song',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='Artiste',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
            preserve_default=False,
        ),
    ]
