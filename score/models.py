# -*- coding: utf-8 -*-
from django.db import models
from datetime import date


class KhlTeam(models.Model):
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
    team_name = models.CharField(primary_key=True, max_length=50, blank=False, help_text="Choose team", choices=TEAM)

    def __str__(self):
        return self.team_name


class KhlGame(models.Model):
    id = models.IntegerField(primary_key=True)
    first_team_name = models.ForeignKey(KhlTeam,
                                        to_field="team_name",
                                        related_name="first_team",
                                        on_delete=models.CASCADE)
    second_team_name = models.ForeignKey(KhlTeam,
                                         to_field="team_name",
                                         related_name="second_team",
                                         on_delete=models.CASCADE)
    game_data = models.DateField(default=date.today)


class KhlGameStat(models.Model):
    team_name = models.ForeignKey(KhlTeam, to_field="team_name", on_delete=models.CASCADE)
    game_id = models.ForeignKey(KhlGame, to_field="id", on_delete=models.CASCADE)
    shot_count = models.IntegerField()
    reflected_count = models.IntegerField()
    period_number = models.IntegerField()


class NhlTeam(models.Model):
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

    team_name = models.CharField(primary_key=True, max_length=50, blank=False, help_text="Choose team", choices=TEAM)

    def __str__(self):
        return self.team_name


class NhlGame(models.Model):
    id = models.IntegerField(primary_key=True)
    first_team_name = models.ForeignKey(NhlTeam,
                                        to_field="team_name",
                                        related_name="first_team",
                                        on_delete=models.CASCADE)
    second_team_name = models.ForeignKey(NhlTeam,
                                         to_field="team_name",
                                         related_name="second_team",
                                         on_delete=models.CASCADE)
    game_data = models.DateField(default=date.today)


class NhlGameStat(models.Model):
    team_name = models.ForeignKey(NhlTeam, to_field="team_name", on_delete=models.CASCADE)
    game_id = models.ForeignKey(NhlGame, to_field="id", on_delete=models.CASCADE)
    shot_count = models.IntegerField()
    reflected_count = models.IntegerField()
    period_number = models.IntegerField()
