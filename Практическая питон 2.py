import getpass

users = [
    {'username': 'raul', 'password': 'raul', 'role': 'user', 'subscription_type': 'Premium'},
    {'username': 'admin', 'password': 'admin', 'role': 'admin'}
]

services = [
    {'name': 'Кардио-тренировка', 'price': 500, 'description': '30 минут'},
    {'name': 'Силовые тренировки', 'price': 700, 'description': '60 минут'},
    {'name': 'Йога', 'price': 900, 'description': '90 минут'}
]

user_purchases = []


def authenticate(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None


def create_user():
    while True:
        username = input("Введите логин: ")
        if any(user['username'] == username for user in users):
            print("Пользователь с таким логином уже существует.")
        else:
            password = getpass.getpass("Введите пароль: ")
            confirm_password = getpass.getpass("Подтвердите пароль: ")
            if password == confirm_password:
                users.append({'username': username, 'password': password, 'role': 'user', 'subscription_type': None})
                print("Пользователь успешно создан.")
                break
            else:
                print("Пароли не совпадают.")


def show_services(sort_by='name', ascending=True, min_price=None, max_price=None):
    filtered_services = services[:]

    if min_price is not None:
        filtered_services = list(filter(lambda x: x['price'] >= min_price, filtered_services))
    if max_price is not None:
        filtered_services = list(filter(lambda x: x['price'] <= max_price, filtered_services))

    if sort_by == 'name':
        filtered_services = sorted(filtered_services, key=lambda x: x['name'], reverse=(not ascending))
    elif sort_by == 'price':
        filtered_services = sorted(filtered_services, key=lambda x: x['price'], reverse=(not ascending))

    if filtered_services:
        for i, service in enumerate(filtered_services):
            print(f"{i+1}. {service['name']} - {service['price']} руб.  ({service['description']})")
    else:
        print("Услуг, удовлетворяющих условиям фильтрации, не найдено.")


def user_menu(user):
    while True:
        print("\nМеню пользователя:")
        print("1. Просмотреть все услуги")
        print("2. Просмотреть услуги (по цене, по возрастанию)")
        print("3. Просмотреть услуги (по цене, по убыванию)")
        print("4. Просмотреть услуги (по названию, по возрастанию)")
        print("5. Просмотреть услуги (по названию, по убыванию)")
        print("6. Фильтровать услуги по цене")
        print("7. Купить услугу")
        print("8. История покупок")
        print("9. Изменить пароль")
        print("10. Выйти")

        choice = input("Выберите действие: ")

        try:
            if choice == '1':
                show_services()
            elif choice == '2':
                show_services(sort_by='price', ascending=True)
            elif choice == '3':
                show_services(sort_by='price', ascending=False)
            elif choice == '4':
                show_services(sort_by='name', ascending=True)
            elif choice == '5':
                show_services(sort_by='name', ascending=False)
            elif choice == '6':
                try:
                    min_p = int(input("Минимальная цена: "))
                    max_p = int(input("Максимальная цена: "))
                    show_services(min_price=min_p, max_price=max_p)
                except ValueError:
                    print("Ошибка: Введите целые числа.")
            elif choice == '7':
                buy_service(user) # заглушка
            elif choice == '8':
                show_purchase_history(user) # заглушка
            elif choice == '9':
                change_password(user) # заглушка
            elif choice == '10':
                break
            else:
                print("Неверный выбор.")
        except Exception as e:
            print(f"Ошибка: {e}")
            
def admin_menu():
    while True:
        print("\nМеню администратора:")
        print("1. Добавить услугу") 
        print("2. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
          add_service()
        elif choice == '2':
            break
        else:
            print("Неверный выбор.")


def show_services():
    for i, service in enumerate(services):
        print(f"{i+1}. {service['name']} - {service['price']} руб.  ({service['description']})")



def buy_service(user):
  show_services()
  try:
    service_index = int(input("Выберите услугу: ")) -1
    if 0 <= service_index < len(services):
      purchase = {'username': user['username'], 'service': services[service_index]['name'], 'price': services[service_index]['price']}
      user_purchases.append(purchase)
      print(f"Услуга '{purchase['service']}' добавлена в историю покупок.")
    else:
      print("Неверный номер услуги.")
  except ValueError:
    print("Ошибка: Введите число.")


def show_purchase_history(user):
    user_purchases_filtered = list(filter(lambda x: x['username'] == user['username'], user_purchases))
    if user_purchases_filtered:
        print("\nИстория покупок:")
        for purchase in user_purchases_filtered:
            print(f"- {purchase['service']} ({purchase['price']} руб.)")
    else:
        print("История покупок пуста.")


def change_password(user):
    new_password = getpass.getpass("Введите новый пароль: ")
    user['password'] = new_password
    print("Пароль успешно изменен.")


def add_service():
  name = input("Название услуги: ")
  try:
    price = int(input("Цена: "))
    description = input("Описание: ")
    services.append({'name': name, 'price': price, 'description': description})
    print("Услуга добавлена.")
  except ValueError:
    print("Ошибка: Неверный формат цены.")


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Войти как пользователь")
        print("2. Войти как администратор")
        print("3. Создать пользователя")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            username = input("Логин: ")
            password = getpass.getpass("Пароль: ")
            user = authenticate(username, password)
            if user and user['role'] == 'user':
                user_menu(user)
            else:
                print("Неверный логин или пароль.")
        elif choice == '2':
            username = input("Логин: ")
            password = getpass.getpass("Пароль: ")
            user = authenticate(username, password)
            if user and user['role'] == 'admin':
                admin_menu()
            else:
                print("Неверный логин или пароль.")

        elif choice == '3':
            create_user()
        elif choice == '4':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()