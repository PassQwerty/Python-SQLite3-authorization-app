import os
import sqlite3

dataBase = None
sql = None


def isValidUser(login):
    return sql.execute(
        f"SELECT login FROM Users WHERE login='{login}' ")


def addUser(login, password):
    cursor = isValidUser(login)

    row = cursor.fetchone()
    if row is None:
        sql.execute(
            f"INSERT INTO Users (login, password) VALUES ('{login}', '{password}')")
        print(f'Пользователь {login} успешно добавлен!!')
        dataBase.commit()
    else:
        print(f'{login} уже добавлен!!')

    finishQuestion()


def finishQuestion():
    choice = input(
        "Хотите продолжить и вернуться в главное меню ('да'|'нет')?: ")
    if choice == 'да':
        main()
    else:
        print("Вы успешно вышли из программы.")
        exit()


def removeUser(login):
    row = isValidUser(login).fetchone()
    if row:
        sql.execute(f"DELETE FROM Users WHERE login='{login}' ")
        print(f'Пользователь {login} успешно удален!!')
        dataBase.commit()
    else:
        print(f'{login} не существует!!')

    finishQuestion()


def updatePasswordUser(login, password):
    row = isValidUser(login).fetchone()
    if row:
        sql.execute(
            f"UPDATE Users SET password = '{password}' WHERE login = '{login}' ")
        print(f'Пароль у пользователя {login} успешно обновлен!!')
        dataBase.commit()
    else:
        print(f'{login} не существует!!')

    finishQuestion()


def Init():
    global dataBase, sql

    dataBase = sqlite3.connect('DataBase/data.db')
    sql = dataBase.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS Users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            login TEXT,
                            password TEXT
                    )""")


def main():
    os.system('cls||clear')

    choice = input("Программа База Данных пользователей... \
        \n1)Добавить пользователя        - 'д [логин] [пароль]'\
        \n2)Удалить пользователя         - 'у [логин]'\
        \n3)Обновить пароль пользователя - 'о [логин] [новый пароль]'\
        \n4)Выход из программы           - 'в' \
        \n\nВведите действие: ")

    words = choice.split()  # разбиение текста на список слов
    word = words[0].lower()
    wordLen = len(words)

    if choice.lower() == 'в':
        print('Вы успешно вышли с программы.')
        exit()
    elif word == 'д' and wordLen == 3:
        addUser(words[1], words[2])
    elif word == 'у' and wordLen == 2:
        removeUser(words[1])
    elif word == 'о' and wordLen == 3:
        updatePasswordUser(words[1], words[2])
    else:
        print('Вы успешно вышли с программы.')


def startApp():
    Init()
    main()


if __name__ == '__main__':
    startApp()
