from django import forms

KHL_TEAM = (
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

NHL_TEAM = (
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
PERIOD = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3")
)

class KhlGameForm(forms.Form):
    first_team = forms.ChoiceField(label='Выберите команду', choices=KHL_TEAM)
    second_team = forms.ChoiceField(label='Выберите команду', choices=KHL_TEAM)
    data = forms.DateField(label='Введите дату игры', widget=forms.SelectDateWidget)
    first_period = forms.ChoiceField(label='Введите перод', choices=PERIOD, initial='1')
    fp_shot_count = forms.IntegerField(label='Количество бросков')
    fp_reflected_count = forms.IntegerField(label='Количество отраженных бросков')
    second_period = forms.ChoiceField(label='Введите перод', choices=PERIOD, initial='2')
    sp_shot_count = forms.IntegerField(label='Количество бросков')
    sp_reflected_count = forms.IntegerField(label='Количество отраженных бросков')
    third_period = forms.ChoiceField(label='Введите перод', choices=PERIOD, initial='3')
    tp_shot_count = forms.IntegerField(label='Количество бросков')
    tp_reflected_count = forms.IntegerField(label='Количество отраженных бросков')

class NhlGameForm(forms.Form):
    first_team = forms.ChoiceField(label='Выберите команду', choices=NHL_TEAM)
    second_team = forms.ChoiceField(label='Выберите команду', choices=NHL_TEAM)
    data = forms.DateField(label='Введите дату игры', widget=forms.SelectDateWidget)
    first_period = forms.ChoiceField(label='Введите перод', choices=PERIOD, initial='1')
    fp_shot_count = forms.IntegerField(label='Количество бросков')
    fp_reflected_count = forms.IntegerField(label='Количество отраженных бросков')
    second_period = forms.ChoiceField(label='Введите перод', choices=PERIOD, initial='2')
    sp_shot_count = forms.IntegerField(label='Количество бросков')
    sp_reflected_count = forms.IntegerField(label='Количество отраженных бросков')
    third_period = forms.ChoiceField(label='Введите перод', choices=PERIOD, initial='3')
    tp_shot_count = forms.IntegerField(label='Количество бросков')
    tp_reflected_count = forms.IntegerField(label='Количество отраженных бросков')