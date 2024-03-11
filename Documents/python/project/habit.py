from datetime import datetime

class Habit:
    """
    Habit class для взаимодействия с различными привычками
    """

    def __init__(self, name: str = None, periodicity: str = None):
        """
        Parameters
        ----------
        name : str, optional
            название привычки (default is None)
        periodicity : str, optional
            период повторения привычки (daily, weekly, or monthly) (default is None)
        """

        self.name = name
        self.periodicity = periodicity
        self.streak = 0 # серия выполнений привычки
        self.current_time = datetime.now().strftime("%m/%d/%Y %H:%M") #текущее время

    def add(self, habits_list):
        """
        Добавляем новую привычку
        """
        if not any(habit['name'] == self.name for habit in habits_list):
            new_habit = {
                'name': self.name,
                'periodicity': self.periodicity,
                'streak': self.streak,
                'last_completion_time': None  #последнее выполнение 
            }
            habits_list.append(new_habit)
            print(f"\nНовая привычка {self.name.capitalize()} создана\n")
        else:
            print("\nДанная привычка уже есть, выберите другую\n")

    def remove(self, habits_list):
        """
        Удаляем привычку из трекера
        """
        habits_list[:] = list(filter(lambda habit: habit['name'] != self.name, habits_list))
        print(f"\nПривычка {self.name.capitalize()} удалена\n")
    
    def change_periodicity(self, habits_list):
        """
        Изменить периодичность привычки
        """
        habit = next((habit for habit in habits_list if habit['name'] == self.name), None)
        if habit:
            habit['periodicity'] = self.periodicity
            habit['last_completion_time'] = self.current_time
            print(f"\nПериодичность привычки {self.name.capitalize()} изменена на {self.periodicity}\n")

    def mark_as_completed(self, habits_list):
        """
        Помечает привычку как выполненную.
        """
        habit = next((habit for habit in habits_list if habit['name'] == self.name), None)

        if habit:
            periodicity = habit['periodicity']

            if periodicity == "daily":
                self.handle_daily_completion(habit)
            elif periodicity == "weekly":
                self.handle_weekly_completion(habit)
            elif periodicity == "monthly":
                self.handle_monthly_completion(habit)
    
    def handle_daily_completion(self, habit):
        """
        Обрабатывает логику ежедневного выполнения.
        """
        days_since_last_completion = self.days_since_last_completion(habit)

        if days_since_last_completion == 0:
            print("\nВы уже выполнили эту привычку сегодня, пожалуйста, попробуйте завтра снова\n")
        elif days_since_last_completion == 1:
            self.update_streak(habit)
        else:
            self.reset_streak(habit)

    def handle_weekly_completion(self, habit):
        """
        Обрабатывает логику еженедельного выполнения.
        """
        weeks_since_last_completion = self.weeks_since_last_completion(habit)

        if weeks_since_last_completion == 0:
            print("\nВы уже выполнили привычку на этой неделе, пожалуйста, попробуйте на следующей неделе\n")
        elif weeks_since_last_completion == 1:
            self.update_streak(habit)
        else:
            self.reset_streak(habit)

    def handle_monthly_completion(self, habit):
        """
        Обрабатывает логику ежемесячного выполнения.
        """
        months_since_last_completion = self.months_since_last_completion(habit)

        if months_since_last_completion == 0:
            print("\nВы уже выполнили привычку в этом месяце, пожалуйста, попробуйте в следующем месяце\n")
        elif months_since_last_completion == 1:
            self.update_streak(habit)
        else:
            self.reset_streak(habit)

    def days_since_last_completion(self, habit_info):
        """
        Возвращает количество прошедших дней с момента последнего выполнения привычки.
        """
        last_completion_time = habit_info['last_completion_time']
        if last_completion_time:
            today = datetime.now().date()
            last_completion_date = datetime.strptime(last_completion_time.split()[0], "%m/%d/%Y").date()
            days_since_last_completion = (today - last_completion_date).days
            return days_since_last_completion
        else:
            return 1  # Если предыдущего выполнения не было, возвращаем 1 

    def weeks_since_last_completion(self, habit_info):
        """
        Возвращает количество прошедших недель с момента последнего выполнения привычки.
        """
        last_completion_time = habit_info['last_completion_time']
        if last_completion_time:
            today = datetime.now().date()
            last_completion_date = datetime.strptime(last_completion_time.split()[0], "%m/%d/%Y").date()
            days_since_last_completion = (today - last_completion_date).days
            weeks_since_last_completion = (days_since_last_completion + 1) // 7
            return weeks_since_last_completion
        else:
            return 2  # Если предыдущего выполнения не было, возвращаем 2 

    def months_since_last_completion(self, habit_info):
        """
        Возвращает количество прошедших месяцев с момента последнего выполнения привычки.
        """
        last_completion_time = habit_info['last_completion_time']
        if last_completion_time:
            today = datetime.now().date()
            last_completion_date = datetime.strptime(last_completion_time.split()[0], "%m/%d/%Y").date()
            months_since_last_completion = (today.year - last_completion_date.year) * 12 + \
                                        (today.month - last_completion_date.month)
            return months_since_last_completion
        else:
            return 1  # Если предыдущего выполнения не было, возвращаем 1 


    def reset_streak(self, habits_list):
        """
        Сбрасывает серию привычки.
        """
        habit = next((habit for habit in habits_list if habit['name'] == self.name), None)
        if habit:
            habit['streak'] = 0  # Устанавливаем серию в 0
            habit['last_completion_time'] = datetime.now().strftime("%m/%d/%Y %H:%M")  # Обновляем последнее выполнение
            print(f"\nOops! Пропущена серия:(")
            print(f"\nСерия {habit['name'].capitalize()} сброшена. Заново...\n")
        
    def update_streak(self, habit):
            """
            Увеличивает серию привычки и обновляет время последнего выполнения.
            """
            habit['streak'] += 1
            habit['last_completion_time'] = self.current_time
            print(f"\nМолодец! Новая серия привычки {self.name.capitalize()} - {habit['streak']}\n")