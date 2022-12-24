#!/usr/bin/env python3
# _*_ coding: utf-8 -*-


def fun1(type_='list'):
    print(type_)

    def fun2(lst):
        if type_ == 'list':
            return list(lst.split())
        else:
            return tuple(lst.split())

    return fun2
