#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_contact():
    """
    Запросить данные о человеке
    """
    family = input("Фамилия? ")
    name = input("Имя? ")
    number = int(input("Номер телефона? "))
    born = list(map(int, input("Дата рождения? ").split('.', 2)))

    return {
        'family': family,
        'name': name,
        'number': number,
        'born': born,
    }


def display_contact(contacts):
    """
    Отобразить спискок контактов
    """
    if contacts:
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 30,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^30} | {:^20} |'.format(
                "№",
                "Фамилия",
                "Имя",
                "Номер телефона",
                "Дата Рождения"
            )
        )
        print(line)

        for idx, contact in enumerate(contacts, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:<30} | {:>20} |'.format(
                    idx,
                    contact.get('family', ''),
                    contact.get('name', ''),
                    contact.get('number', 0),
                    '.'.join((str(i) for i in contact['born']))
                )
            )
        print(line)
    else:
        print("Список контктов пуст.")


def select_contact(contacts, period):
    """
    Выбрать маршрут
    """
    result = []
    for contact in contacts:
        if contact.get('family') == period:
            result.append(contact)

    return result

