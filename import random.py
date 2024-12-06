import random

class Game:
    def __init__(self):
        self.inventory = []
        self.levels = {
            1: "Вака",
            2: "Людмила",
            3: "Вопрос",
            4: "Выход из замка Людмилы"
        }
        self.monster_defeated = False
        self.completed_tasks = set()
        self.keys_found = set()
        self.monster_required_item = "флэш"
        self.total_keys = 3

    def show_inventory(self):
        print("Ваш карман:", self.inventory if self.inventory else "пуст.")

    def collect_keys(self):
        print("Вы ищете ваки в комнате...")
        keys = {f"вака{num}" for num in range(1, self.total_keys + 1)}
        
        while keys:
            action = input("Что вы хотите сделать? (взять, проверить карман): ").lower()
            if action == "взять":
                key = random.choice(list(keys))
                keys.remove(key)
                self.keys_found.add(key)
                self.inventory.append(key)
                print(f"Вы нашли {key}. Осталось вак: {len(keys)}.")
            elif action == "проверить карман":
                self.show_inventory()
            else:
                print("Неверная команда, попробуйте снова.")
        print("Вы собрали все ваки!")

    def find_sword(self):
        print("Вы ищете флэш, чтобы победить Людмилу.")
        if "флэш" not in self.inventory:
            print("Вы нашли флэш!")
            self.inventory.append("флэш")

    def level_one(self):
        print("Вы находитесь в комнате где спрятаны ваки. Найдите ваки. На ваках будет код для выхода из замка.")
        self.collect_keys()

        while True:
            action = input("Что хотите сделать? (убежать, карман): ").lower()
            if action == "убежать" and self.keys_found:
                print("Вы убежали с вакой.")
                self.completed_tasks.add(self.levels[1])
                break
            elif action == "карман":
                self.show_inventory()
            else:
                print("Неверная команда, попробуйте снова.")

    def level_two(self):
        print("Вы вошли в темный коридор и встретили Людмилу!")
        self.find_sword()

        while True:
            action = input("Что вы хотите сделать? (победить, убежать, карман): ").lower()
            if action == "победить":
                if "флэш" in self.inventory:
                    print("Вы победили Людмилу с помощью флэша!")
                    self.monster_defeated = True
                    self.completed_tasks.add(self.levels[2])
                    break
                else:
                    print("Для победы над Людмилой вам нужен флэш!")
            elif action == "убежать":
                print("Вы убежали от Людмилы, но все еще находитесь в аудитории.")
            elif action == "карман":
                self.show_inventory()
            else:
                print("Неверная команда, попробуйте снова.")

    def level_three(self):
        print("Вы оказались на -1 этаже. Ответьте на вопрос, чтобы выбраться.")
        puzzle_answer = "даня"

        while True:
            answer = input("Кто хозяин -1 этажа? ").lower()
            if answer == puzzle_answer:
                print("Вы угадали кто хозяин -1 этажа и выбрались из замка Людмилы!")
                self.completed_tasks.add(self.levels[3])
                break
            else:
                print("Неправильный ответ. Попробуйте еще раз.")

    def level_four(self):
        print("Вы находитесь у выхода из замка, но дверь закрыта.")
        secret_code = "Гарик"  
        while True:
            code = input("Введите код для выхода: ")
            if code == secret_code:
                print("Вы успешно выбрались из замка! Поздравляем!")
                self.completed_tasks.add(self.levels[4])
                break
            else:
                print("Неверный код. Попробуйте ещё раз.")


    def start_game(self):
        print("Добро пожаловать в замок Людмилы!")
        self.level_one()
        if self.levels[1] in self.completed_tasks:
            print("Вы прошли уровень 1.")
        self.level_two()
        if self.monster_defeated:
            print("Вы прошли уровень 2.")
        self.level_three()
        if self.levels[3] in self.completed_tasks:
            print("Вы прошли уровень 3.")
        self.level_four()
        if self.levels[4] in self.completed_tasks:
            print("Вы завершили игру. Поздравляем!")

if __name__ == "__main__":
    game = Game()
    game.start_game()