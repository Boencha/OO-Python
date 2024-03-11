class Analyze:
    def __init__(self, habits_list):
        self.habits = habits_list

    def data_of_all_habits(self) -> list:
        """
        Выводим список созданных привычек
        """
        return self.habits

    def data_of_custom_periodicity_habits(self, periodicity:int) -> list:
        """
        Выводим привычки с заданной периодичсностью
        """
        return [habit for habit in self.habits if habit['periodicity'] == periodicity]

    def data_of_single_habit(self, habit_name:list[dict]) -> list:
        """
        Выводим данные указанной отдельной привычки
        """
        return [habit for habit in self.habits if habit['name'] == habit_name]

    def show_habits_data(self, periodicity=None):
        """
        Выводим данные о всех привычках в табличном формате
        """
        if periodicity is not None:
            data = self.data_of_custom_periodicity_habits(periodicity)
        else:
            data = self.data_of_all_habits()
        if len(data) > 0:
            print("\n{:<15} {:<15} {:<25}".format("Name", "Periodicity", "Last Completion"))
            print(f"{'_' * 70}")
            for habit in data:
                print("{:<10} {:<15} {:<15}".format(
                    habit['name'].capitalize(),
                    habit['periodicity'].capitalize(),
                    habit['last_completion_time'].capitalize() if habit['last_completion_time'] is not None else "--/--/-- --:--"
                ))
            print(f"{'_' * 70}\n")
        else:
            print("\nНе обнаружено ни одной привычки\n")

    def show_habit_streak_data(self, habit=None):
        """
        Выводим серию привычки/всех привычек
        """
        if habit is None:
            data = self.data_of_all_habits()
        else:
            data = self.data_of_single_habit(habit)
        if len(data) > 0:
            print("\n{:<15} {:<15} {:<25} {:<20}".format("Name", "Periodicity", "Last Completion Time", "Current Streak"))  # заголовок таблицы
            print(f"{'_' * 75}")
            for habit in data:
                period = " Day(s)" if habit['periodicity'] == "daily" else (
                    " Week(s)" if habit['periodicity'] == "weekly" else " Month(s)")  # определяем в чем изм-ся период
                print("{:<15} {:<15} {:<25} {:<20}".format(
                    habit['name'].capitalize(),
                    habit['periodicity'].capitalize(),
                    habit['last_completion_time'] if habit['last_completion_time'] is not None else "--/--/-- --:--",
                    str(habit['streak']) + period
                ))
                print(f"{'_' * 75}\n")
        else:
            print("\nПривычка не найдена. Добавьте сначала, пожалуйста!\n")
    