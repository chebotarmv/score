# -*- coding: utf-8 -*-
from django.db import models
from datetime import date


class KhlTeam(models.Model):
    class Meta:
        verbose_name = 'Команда КХЛ'
        verbose_name_plural = 'Команды КХЛ'

    TEAM = (
        ("Ак Барс", "Ак Барс"),
        ("Салават Юлаев", "Салават Юлаев"),
        ("Трактор", "Трактор"),
        ("Автомобилист", "Автомобилист"),
        ("Металлург Мг", "Металлург Мг"),
        ("Нефтехимик", "Нефтехимик"),
        ("Авангард", "Авангард"),
        ("Амур", "Амур"),
        ("Торпедо", "Торпедо"),
        ("Сибирь", "Сибирь"),
        ("Барыс", "Барыс"),
        ("Адмирал", "Адмирал"),
        ("Куньлунь РС", "Куньлунь РС"),
        ("СКА", "СКА"),
        ("ЦСКА", "ЦСКА"),
        ("Йокерит", "Йокерит"),
        ("Локомотив", "Локомотив"),
        ("ХК Сочи", "ХК Сочи"),
        ("Спартак", "Спартак"),
        ("Северсталь", "Северсталь"),
        ("Динамо Мск", "Динамо Мск"),
        ("Динамо Мн", "Динамо Мн"),
        ("Витязь", "Витязь"),
        ("Слован", "Слован"),
        ("Динамо Р", "Динамо Р")

    )

    team_name = models.CharField('Имя команды',
                                 primary_key=True,
                                 max_length=50,
                                 blank=False,
                                 help_text="Choose team",
                                 choices=TEAM)

    def __str__(self):
        return self.team_name


class KhlGame(models.Model):
    class Meta:
        verbose_name = 'Игра КХЛ'
        verbose_name_plural = 'Игры КХЛ'

    id = models.IntegerField('id игры', primary_key=True)
    first_team_name = models.ForeignKey(KhlTeam,
                                        verbose_name='имя первой команды',
                                        to_field="team_name",
                                        related_name="first_team",
                                        on_delete=models.CASCADE)
    second_team_name = models.ForeignKey(KhlTeam,
                                         verbose_name='Имя второй команды',
                                         to_field="team_name",
                                         related_name="second_team",
                                         on_delete=models.CASCADE)
    game_data = models.DateField('Дата', default=date.today)


class KhlGameStat(models.Model):
    class Meta:
        verbose_name = 'Статистика по игре КХЛ'
        verbose_name_plural = 'Статистика по играм КХЛ'

    team_name = models.ForeignKey(KhlTeam, verbose_name='Имя команы', to_field="team_name", on_delete=models.CASCADE)
    game_id = models.ForeignKey(KhlGame, verbose_name='id игры', to_field="id", on_delete=models.CASCADE)
    shot_count = models.IntegerField('Броски по воротам')
    reflected_count = models.IntegerField('Отбитые броски')
    period_number = models.IntegerField('Период')


class NhlTeam(models.Model):
    class Meta:
        verbose_name = 'Команда НХЛ'
        verbose_name_plural = 'Команды НХЛ'

    TEAM = (
        ("Анахайм Дакс", "Анахайм Дакс"),
        ("Бостон Брюинз", "Бостон Брюинз"),
        ("Вашингтон Кэпиталз", "Вашингтон Кэпиталз"),
        ("Вегас Голден Найтс", "Вегас Голден Найтс"),
        ("Виннипег Джетс", "Виннипег Джетс"),
        ("Коламбус Блю Джекетс", "Коламбус Блю Джекетс"),
        ("Колорадо Эвеланш", "Колорадо Эвеланш"),
        ("Лос-Анджелес Кингз", "Лос-Анджелес Кингз"),
        ("Миннесота Уайлд", "Миннесота Уайлд"),
        ("Нью-Джерси Дэвилз", "Нью-Джерси Дэвилз"),
        ("Нэшвилл Предаторз", "Нэшвилл Предаторз"),
        ("Питтсбург Пингвинз", "Питтсбург Пингвинз"),
        ("Сан-Хосе Шаркс", "Сан-Хосе Шаркс"),
        ("Тампа-Бэй Лайтнинг", "Тампа-Бэй Лайтнинг"),
        ("Торонто Мэйпл Лифс", "Торонто Мэйпл Лифс"),
        ("Филадельфия Флайерз", "Филадельфия Флайерз")
    )

    team_name = models.CharField('Имя команды', primary_key=True, max_length=50, blank=False, help_text="Choose team", choices=TEAM)

    def __str__(self):
        return self.team_name


class NhlGame(models.Model):
    class Meta:
        verbose_name = 'Игра НХЛ'
        verbose_name_plural = 'Игры НХЛ'

    id = models.IntegerField('id игры', primary_key=True)
    first_team_name = models.ForeignKey(NhlTeam,
                                        verbose_name='Имя первой команды',
                                        to_field="team_name",
                                        related_name="first_team",
                                        on_delete=models.CASCADE)
    second_team_name = models.ForeignKey(NhlTeam,
                                         verbose_name='Имя второй команды',
                                         to_field="team_name",
                                         related_name="second_team",
                                         on_delete=models.CASCADE)
    game_data = models.DateField('Дата', default=date.today)


class NhlGameStat(models.Model):
    class Meta:
        verbose_name = 'Статистика по игре НХЛ'
        verbose_name_plural = 'Статистика по играм НХЛ'

    team_name = models.ForeignKey(NhlTeam, verbose_name='Имя команды', to_field="team_name", on_delete=models.CASCADE)
    game_id = models.ForeignKey(NhlGame, verbose_name='id игры', to_field="id", on_delete=models.CASCADE)
    shot_count = models.IntegerField('Броски по воротам')
    reflected_count = models.IntegerField('Отбитые броски')
    period_number = models.IntegerField('Период')
