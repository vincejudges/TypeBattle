#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import turtle
from header import flat_UI_color


__all__ = []
__author__ = 'Yee_172'
__date__ = '2019/08/21'


if __name__ == '__main__':
    # set up screen
    # turtle.setup(1000, 600)
    turtle.setup(width=.75, height=.75)
    screen = turtle.Screen()
    screen.bgcolor(flat_UI_color['midnight blue'])

    # set keyboard bindings
    screen.onkey(exit, 'Escape')
    screen.listen()

    turtle.done()
