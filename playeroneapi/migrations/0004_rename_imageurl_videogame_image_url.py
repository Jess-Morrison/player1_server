# Generated by Django 4.1.6 on 2023-02-11 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playeroneapi', '0003_alter_videogame_game_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videogame',
            old_name='imageURL',
            new_name='image_url',
        ),
    ]