# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0003_auto_20180613_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nhlgame',
            old_name='first_team_id',
            new_name='first_team_name',
        ),
        migrations.RenameField(
            model_name='nhlgame',
            old_name='second_team_id',
            new_name='second_team_name',
        ),
        migrations.RenameField(
            model_name='nhlgamestat',
            old_name='team_id',
            new_name='team_name',
        ),
        migrations.RemoveField(
            model_name='nhlteam',
            name='id',
        ),
        migrations.AlterField(
            model_name='nhlteam',
            name='team_name',
            field=models.CharField(choices=[('Анахайм Дакс', 'Анахайм Дакс'), ('Бостон Брюинз', 'Бостон Брюинз'), ('Вашингтон Кэпиталз', 'Вашингтон Кэпиталз'), ('Вегас Голден Найтс', 'Вегас Голден Найтс'), ('Виннипег Джетс', 'Виннипег Джетс'), ('Коламбус Блю Джекетс', 'Коламбус Блю Джекетс'), ('Колорадо Эвеланш', 'Колорадо Эвеланш'), ('Лос-Анджелес Кингз', 'Лос-Анджелес Кингз'), ('Миннесота Уайлд', 'Миннесота Уайлд'), ('Нью-Джерси Дэвилз', 'Нью-Джерси Дэвилз'), ('Нэшвилл Предаторз', 'Нэшвилл Предаторз'), ('Питтсбург Пингвинз', 'Питтсбург Пингвинз'), ('Сан-Хосе Шаркс', 'Сан-Хосе Шаркс'), ('Тампа-Бэй Лайтнинг', 'Тампа-Бэй Лайтнинг'), ('Торонто Мэйпл Лифс', 'Торонто Мэйпл Лифс'), ('Филадельфия Флайерз', 'Филадельфия Флайерз')], help_text='Choose team', max_length=50, primary_key=True, serialize=False),
        ),
    ]