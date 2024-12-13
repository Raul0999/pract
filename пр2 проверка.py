import getpass

users = [
    {'username': 'john_doe', 'password': 'password', 'role': 'user', 'subscription_type': 'Premium'},
    {'username': 'admin', 'password': 'admin', 'role': 'admin'}
]

services = [
    {'name': 'Кардио-тренировка', 'price': 500, 'rating': 4.5, 'description': '30 минут'},
    {'name': 'Силовые тренировки', 'price': 700, 'rating': 4.8, 'description': '60 минут'},
    {'name': 'Йога', 'price': 600, 'rating': 4.2, 'description': '90 минут'},
    {'name': 'Пилатес', 'price': 650, 'rating': 4.7, 'description': '60 минут'}
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



def filter_and_sort_services(min_price=0, max_price=float('inf'), sort_by='name', descending=False):
    filtered_services = [service for service in services
                         if min_price <= service['price'] <= max_price]
    if sort_by in ['price', 'rating', 'name']:
        filtered_services.sort(key=lambda x: x[sort_by], reverse=descending)
    return filtered_services


def purchase_service(user):
    show_services()
    try:
        service_index = int(input("Выберите услугу: ")) - 1
        if 0 <= service_index < len(services):
            purchase = {'username': user['username'], 'service': services[service_index]['name'],
                        'price': services[service_index]['price']}
            user_purchases.append(purchase)
            print(f"Услуга '{purchase['service']}' добавлена в историю покупок.")
        else:
            print("Неверный номер услуги.")
    except ValueError:
        print("Ошибка: Введите число.")


def view_purchase_history(user):
    user_purchases_filtered = [p for p in user_purchases if p['username'] == user['username']]
    if user_purchases_filtered:
        print("\nИстория покупок:")
        for purchase in user_purchases_filtered:
            print(f"- {purchase['service']} ({purchase['price']} руб.)")
    else:
        print("История покупок пуста.")


def update_profile(user):
    new_password = getpass.getpass("Введите новый пароль (или оставьте пустым для пропуска): ")
    if new_password:
        user['password'] = new_password
        print("Пароль успешно изменен.")
    else:
        print("Пароль не изменен.")


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
                buy_service(user)
            elif choice == '8':
                show_purchase_history(user)
            elif choice == '9':
                change_password(user)
            elif choice == '10':
                break
            else:
                print("Неверный выбор.")
        except Exception as e:
            print(f"Ошибка: {e}")




def show_services(sort_by='name', ascending=True, min_price=None, max_price=None):
    if sort_by == 'name':
        sorted_services = sorted(services, key=lambda x: x['name'], reverse=(not ascending))
    elif sort_by == 'price':
        sorted_services = sorted(services, key=lambda x: x['price'], reverse=(not ascending))
    else:
        sorted_services = services

    for i, service in enumerate(sorted_services):
        print(f"{i+1}. {service['name']} - {service['price']} руб.  ({service['description']})")






def admin_menu():
    while True:
        print("\nМеню администратора:")
        print("1. Добавить услугу")  # Упрощенное добавление услуги
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