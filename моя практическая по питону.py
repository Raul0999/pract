import random
import time

def print_delay(text):
    print(text)
    time.sleep(1)

inventory = []

def start_game():
    print_delay("Добро пожаловать в текстовую игру 'Фэнтезийный Квест'!")
    print_delay("Вы – смелый исследователь по имени Элис, задача которой – найти магическую чашу, которая дарует силу.")
    print_delay("Элис, готова к приключениям?")
    input("Нажмите Enter, чтобы начать...")
    level_one()

def level_one():
    print_delay("\nУровень 1: Вы стоите перед входом в древний замок. Перед вами три двери:")
    paths = ("Дверь А (Покрытая лианами)", "Дверь Б (Заваленная камнями)", "Дверь В (Тёмная и зловещая)")

    print(f"Какую дверь выберете?")
    for path in paths:
        print(f"- {path}")

    choice = input("Введите дверь (A, B или C): ").strip().upper()

    if choice in ["A", "B", "C"]:
        if choice == "A":
            print_delay("Вы проходите через покрытую лианами дверь и находите старую книгу с заклинаниями!")
            inventory.append("Книга заклинаний")
            print_delay("В вашем инвентаре теперь есть книга заклинаний.")
            level_two()
        elif choice == "B":
            print_delay("Вы пытаетесь пролезть через завал, но камни обрушиваются, и вы теряете время!")
            print_delay("Попробуйте другую дверь...")
            level_one()
        elif choice == "C":
            print_delay("Вы входите в темный проход и встречаете загадочного стража!")
            combat_choice = input("Вы хотите (сразиться/убежать)? ").strip().lower()
            if combat_choice == "сразиться":
                print_delay("Вы сражаетесь со стражем и одерживаете победу!")
                inventory.append("Магический трофей")
                print_delay("В вашем инвентаре теперь есть магический трофей.")
                level_two()
            else:
                print_delay("Вы решаете убежать и возвращаетесь к началу.")
                level_one()
    else:
        print_delay("Неверный выбор, попробуйте снова.")
        level_one()

def level_two():
    print_delay("\nУровень 2: Ваша книга заклинаний содержит загадку. Вам нужно решить её:")
    riddle = "Я лечу без крыльев, я плачу без глаз. Что я?"
    print(riddle)
    answer = input("Ваш ответ: ").strip().lower()

    if answer == "облако":
        print_delay("Правильно! Вы нашли заклинание для открытия двери!")
        inventory.append("Заклинание")
        print_delay("В вашем инвентаре теперь есть заклинание.")
        level_three()
    else:
        print_delay("Неправильно. Вы теряете время и должны вернуться к дверям.")
        level_one()

def level_three():
    print_delay("\nУровень 3: Вы добрались до запертой двери. Вам нужно заклинание!")
    if "Заклинание" in inventory:
        print_delay("У вас есть заклинание! Вы произносите его и дверь открывается.")
        level_four()
    else:
        print_delay("У вас нет заклинания. Вам нужно вернуться и найти его.")
        level_one()

def level_four():
    print_delay("\nУровень 4: Внутри вы находите древний алтарь. Вам нужно найти подсказку о местонахождении магической чаши.")
    hints = ["В подземелье", "На вершине башни", "В тайнике за статуей"]
    correct_hint = random.choice(hints)

    attempts = 2
    while attempts > 0:
        print_delay(f"У вас осталось {attempts} попыток.")
        guess = input(f"Где, по вашему мнению, спрятана магическая чаша? ({', '.join(hints)}): ").strip().lower()
        if guess == correct_hint.lower():
            print_delay(f"Вы нашли подсказку! Магическая чаша спрятана {correct_hint}!")
            level_five()
            break
        else:
            print_delay("Неверно. Попробуйте еще раз.")
            attempts -= 1
    if attempts == 0:
        print_delay("Вы не смогли найти подсказку. Игра окончена.")
        play_again()

def level_five():
    print_delay("\nУровень 5: Вы нашли магическую чашу!")
    end_game(True)

def end_game(success):
    if success:
        print_delay("\nПоздравляю! Вы нашли магическую чашу и стали легендарным исследователем!")
    else:
        print_delay("\nК сожалению, вы не смогли найти магическую чашу. Попробуйте снова.")
    play_again()

def play_again():
    again = input("Хотите сыграть снова? (да/нет) ").strip().lower()
    if again == "да":
        inventory.clear()
        start_game()
    else:
        print_delay("Спасибо за игру!")

if __name__ == "__main__":
    start_game()