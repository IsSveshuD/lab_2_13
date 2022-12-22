#!/usr/bin/env python3
# _*_ coding: utf-8 -*-


from fun1 import fun1


a1 = input("Введите параметр type: ")
a2 = input("Введите список целых чисел через пробел: ")
list_fun = fun1(a1)
print(list_fun(a2))
