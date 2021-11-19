# Generated by Django 3.2.9 on 2021-11-06 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='winrate',
            new_name='win_rate',
        ),
        migrations.AddField(
            model_name='player',
            name='total_lose',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='total_tie',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='total_win',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bot',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.player'),
        ),
    ]