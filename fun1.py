#!/usr/bin/env python3
# _*_ coding: utf-8 -*-


def fun1(type_='max'):
    def fun2(lst):
        return eval(f'{type_}(lst)')
    print(type_)
    return fun2
