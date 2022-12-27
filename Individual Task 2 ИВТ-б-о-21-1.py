#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from ROUTE import get_contact, display_contact, select_contact


if __name__ == '__main__':
    contacts = []

    while True:
        command = input(">>> ").lower()
        """
        Меню команд для взаимодействия с программой.
        """
        if command == 'exit':
            break

        elif command == 'add':
            contact = get_contact()
            contacts.append(contact)
            if len(contacts) > 1:
                contacts.sort(key=lambda item: item.get('number', [0 - 2]))

        elif command == 'list':
            display_contact(contacts)

        elif command.startswith('select'):
            period = input('Введите Фамилию человека,'
                           ' информацию по которому Вы хотите найти: ')

            selected = select_contact(contacts, period)
            display_contact(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - Добавить контакт;")
            print("list - Вывести список контактов;")
            print("select -  Поиск по фамилии;")
            print("help - Отобразить справку;")
            print("exit - Завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
