# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-15 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Project Call', 'Project Call'), ('Study Group Call', 'Study Group Call'), ('Community Call', 'Community Call'), ('Workshop', 'Workshop'), ('Sprint', 'Sprint'), ('MozFest', 'MozFest'), ('Conference', 'Conference'), ('Meetup', 'Meetup'), ('Convening', 'Convening')], default='Project Call', help_text='Select the type of event', max_length=50),
        ),
    ]
