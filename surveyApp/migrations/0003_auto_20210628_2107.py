# Generated by Django 3.2.3 on 2021-06-28 18:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surveyApp', '0002_auto_20210628_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice',
        ),
        migrations.AddField(
            model_name='answer',
            name='mChoices',
            field=models.ManyToManyField(related_name='mChoices', to='surveyApp.Choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='sChoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sChoice', to='surveyApp.choice'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='survey',
            name='dateEnd',
            field=models.DateField(default=datetime.datetime(2021, 6, 28, 21, 7, 56, 840249)),
        ),
        migrations.AlterField(
            model_name='survey',
            name='dateStart',
            field=models.DateField(default=datetime.datetime(2021, 6, 28, 21, 7, 56, 840249)),
        ),
    ]
