import questionary as qt
import get
from habit import Habit
from analyze import Analyze
import pickle


# хранение привычек
def load_habits():
    try:
        with open('habits_data.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
     
def save_habits(habits_list):
    with open('habits_data.pkl', 'wb') as file:
        pickle.dump(habits_list, file)   

habits_list = load_habits()
analyze = Analyze(habits_list)

# приветственное письмо
def decorator(function_to_decorate):
    def wrapper():
        print("-" * 34)
        function_to_decorate()
        print("-" * 34)
    return wrapper()

@decorator
def greetings():
    print("Добро пожаловать в трекер привычек")


# CLI Interface
def menu():
    """
    CLI Interface используем с библиотекой questionary для отображения menu
    """
    # user делает выбор
    choice = qt.select(
        "Что вы хотите сделать?",
        choices=[
            "Добавить/Удалить привычку",
            "Изменить периодичность привычки",
            "Отметить привычку как выполненную",
            "Показать привычки (все или отсортированные по периодичности)",
            "Анализ",
            "Выход"
            ]).ask()

    if choice == "Добавить/Удалить привычку":
        # более точный выбор
        second_choice = qt.select(
            "Хотите добавить или удалить привычку?",
    choices=[
        "Добавить привычку",
        "Удалить привычку",
        "Вернуться в главное меню"
            ]).ask()

        if second_choice == "Добавить привычку":
            habit_name = get.habit_name()
            habit_periodicity = get.habit_periodicity()
            habit = Habit(habit_name, habit_periodicity)
            habit.add(habits_list)

        elif second_choice == "Удалить привычку":
            try:
                habit_name = get.habits_from_list(habits_list)
            except ValueError:
                print("\nOops! Привычек не найдено. Сначала добавьте привычку\n")
            else:
                habit = Habit(habit_name)
                if get.habit_delete_confirmation(habit_name):
                    habit.remove(habits_list)
                else:
                    print("\nNo problem!:)\n")

        elif second_choice == "Вернуться в главное меню":
            menu()

    elif choice == "Изменить периодичность привычки":
        try:
            habit_name = get.habits_from_list(habits_list)
        except ValueError:
            print("\nOops! Привычек не найдено. Сначала добавьте привычку\n")
        else:
            new_periodicity = get.habit_periodicity()
            if get.periodicity_change_confirmed():
                habit = Habit(habit_name, new_periodicity)
                habit.change_periodicity(habits_list)
            else:
                print(f"\nПериодичность {habit_name} остается неизменной!\n")
                
    elif choice == "Отметить привычку как выполненную":
        try:
            habit_name = get.habits_from_list(habits_list)
        except ValueError:
            print("\nOops! Привычек не найдено. Сначала добавьте привычку\n")
        else:
            habit = Habit(habit_name)
            habit.mark_as_completed(habits_list)

    elif choice == "Показать привычки (все или отсортированные по периодичности)":
        second_choice = get.show_period_choices()
        if second_choice == "Просмотреть все привычки":
            analyze.show_habits_data()
            
        elif second_choice == "Просмотреть ежедневные привычки":
            analyze.show_habits_data("daily")
            
        elif second_choice == "Просмотреть еженедельные привычки":
            analyze.show_habits_data("weekly")
            
        elif second_choice == "Просмотреть ежемесячные привычки":
            analyze.show_habits_data("monthly")
            
        elif second_choice == "Вернуться в главное меню":
            menu()

    elif choice == "Анализ":
        second_choice = get.analytics_choices()
        if second_choice == "Просмотреть все серии привычек":
            analyze.show_habit_streak_data()
            
        elif second_choice == "Просмотреть серию определенной привычки":
            try:
                habit_name = get.habits_from_list(habits_list)
            except ValueError:
                print("\nOops! Привычек не найдено. Сначала добавьте привычку\n")
            else:
                analyze.show_habit_streak_data(habit_name)
                
        elif second_choice == "Вернуться в главное меню":
            menu()

    elif choice == "Выход":
        save_habits(habits_list)
        print("\nПока! Хорошего дня!")  
        exit()
         

if __name__ == "__main__":
    while True:
        menu()
