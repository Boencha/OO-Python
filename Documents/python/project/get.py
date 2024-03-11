import questionary as qt

def habit_name():
    return qt.text("Пожалуйста, введите привычку, которую хотите создать:",
                    validate=lambda name: True if name.isalpha() and len(name) > 1
                    else "Пожалуйста, введите верное имя").ask().lower()

def habit_periodicity():
    return qt.select("Пожалуйста, выберите периодичность",
                    choices=["Daily", "Weekly", "Monthly"]).ask().lower()


def periodicity_change_confirmed():
    return qt.confirm("Изменение периодичности привычки приведет к сбросу серии. Продолжить?").ask()

def habits_from_list(habits_list):
    '''
    Отображаем имена созданных привычек на выбор пользователя.

    :return: Возвращаем выбранную привычку из списка вариантов.
    :raises ValueError: если нет доступных привычек, выдается ValueError.
    '''
    habit_names = [habit['name'] for habit in habits_list]
    if habit_names:
        return qt.select("Пожалуйста, выберите привычку",
                             choices=sorted(habit_names)).ask().lower()
    else:
        raise ValueError("В списке нет привычек; Сначала добавьте привычку, чтобы использовать эту функцию.")

def habit_delete_confirmation(habit_name_to_delete):
    '''
    Предлагаем пользователю подтвердить, хочет ли он удалить привычку или нет.
    :return: Возвращаем True, если да, иначе возвращаем False
    '''
    return qt.confirm(f"Уверены, что хотите удалить привычку '{habit_name_to_delete}'?").ask()

def show_period_choices():
    return qt.select( "Хотели бы вы просмотреть все привычки или отсортировать привычки по периодичности?",
                        choices=[
                            "Просмотреть все привычки",
                            "Просмотреть ежедневные привычки",
                            "Просмотреть еженедельные привычки",
                            "Просмотреть ежемесячные привычки",
                            "Вернуться в главное меню"
                        ]).ask()

def analytics_choices():
    return qt.select("Пожалуйста, выберите опцию:",
                        choices=[
                            "Просмотреть все серии привычек",
                            "Просмотреть серию определенной привычки",
                            "Вернуться в главное меню"
                         ]).ask()
