# Generated by Django 4.1.3 on 2022-12-08 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_game_info_games_alter_transaction_g_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='g_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.games'),
        ),
    ]