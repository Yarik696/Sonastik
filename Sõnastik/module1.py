import random

def Loe_failist(fail: str) -> list:
    f = open(fail, 'r', encoding="utf-8-sig")
    mas = []
    for rida in f:
        mas.append(rida.strip('\n').upper())
    f.close()
    return mas

def lisamine(mas: list, file: str):
    f = open(file, 'w', encoding="utf-8-sig")
    for item in mas:
        f.write(item + "\n")
    f.close()

def connect(est: list, rus: list) -> None:
    zipped = zip(est, rus)
    print(list(zipped))

def elementi_lisamine(est: list, rus: list):
    es = input("Слово на эстонском: ")
    est.append(es)
    ru = input("Слово на русском: ")
    rus.append(ru)
    return est, rus

def est_to_rus(est: list, rus: list):
    n = input("Пожалуйста, введите слово на эстонском языке: ").upper()
    if n in est:
        ind = est.index(n)
        print(f"{n} -- {rus[ind]}")
        v = int(input("Если считаете, что перевод некорректный, введите 0: "))
        if v == 0:
            cor = input("Введите корректный перевод: ")
            rus[ind] = cor
            lisamine(rus, "rus.txt")
            print(est)
            print(rus)
        else:
            print("Пока!")
    else:
        print("Слово отсутствует. Хотите добавить его в словарь? (да/нет)")
        choice = input().lower()
        if choice == "да":
            est, rus = elementi_lisamine(est, rus)
            lisamine(est, "est.txt")
            lisamine(rus, "rus.txt")
        elif choice == "нет":
            print("ОК, вы можете продолжить работу.")
        else:
            print("Некорректный ввод.")

def rus_to_est(est: list, rus: list):
    n = input("Введите слово на русском языке: ").upper()
    if n in rus:
        ind = rus.index(n)
        print(f"{n} -- {est[ind]}")
        v = int(input("Если считаете, что слово введено некорректно, введите 0: "))
        if v == 0:
            cor = input("Введите корректный перевод: ")
            est[ind] = cor
            lisamine(est, "est.txt")
            print(est)
            print(rus)
        else:
            print("Пока!")
    else:
        print("Слово отсутствует. Хотите добавить его в словарь? (да/нет)")
        choice = input().lower()
        if choice == "да":
            est, rus = elementi_lisamine(est, rus)
            lisamine(est, "est.txt")
            lisamine(rus, "rus.txt")
        elif choice == "нет":
            print("ОК, вы можете продолжить работу.")
        else:
            print("Некорректный ввод.")

def mang(est: list, rus: list):
    oige = 0
    total = 5
    for i in range(total):
        n = random.choice(est)
        print(n)
        ind = est.index(n)
        v = input("Введите перевод: ").upper()
        if v in rus and v == rus[ind]:
            oige += 1
            print(f"Правильно! Правильное слово: {rus[ind]}")
        else:
            print("К сожалению, ответ неверный.")
    
    accuracy = (oige / total) * 100
    print(f"Ваш результат: {accuracy}%")


def show_menu():
    print("Меню:")
    print("1. Показать все слова и их переводы")
    print("2. Добавить слово и его перевод в словарь")
    print("3. Перевести слово с эстонского на русский")
    print("4. Перевести слово с русского на эстонский")
    print("5. Проверить знание слов из словаря")
    print("6. Выход")

def main_menu(est, rus):
    while True:
        show_menu()
        choice = input("Выберите опцию: ")
        if choice == "1":
            connect(est, rus)
        elif choice == "2":
            est, rus = elementi_lisamine(est, rus)
        elif choice == "3":
            est_to_rus(est, rus)
        elif choice == "4":
            rus_to_est(est, rus)
        elif choice == "5":
            mang(est, rus)
        elif choice == "6":
            print("До свидания!")
            break  # Здесь использовано ключевое слово break для завершения цикла
        else:
            print("Некорректный выбор. Пожалуйста, выберите опцию от 1 до 6.")

# Загрузка словарей
est = Loe_failist("est.txt")
rus = Loe_failist("rus.txt")

# Запуск основного меню
main_menu(est, rus)

