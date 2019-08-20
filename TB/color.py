#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint


__all__ = ['FlatUIColors']
__author__ = 'Yee_172'
__date__ = '2019/08/21'


def _color_list_beautify(color_class):
    return ', '.join('([{}]: {} -> {})'.format(i, color_class.index[i], color_class.color[color_class.index[i]]) for i in range(len(color_class.color)))


class FlatUIColors:
    """Flat UI Colors
    
    source: https://flatuicolors.com/palette/defo
    """
    def __init__(self):
        self.color = {'torquoise': '#1abc9c',
                      'greensea': '#16a085',
                      'sunflower': '#f1c40f',
                      'orange': '#f39c12',
                      'emerald': '#2ecc71',
                      'nephritis': '#27ae60',
                      'carrot': '#e67e22',
                      'pumpkin': '#d35400',
                      'peterriver': '#3498db',
                      'belizehole': '#2980b9',
                      'alizarin': '#e74c3c',
                      'pomegranate': '#c0392b',
                      'amethyst': '#9b59b6',
                      'wisteria': '#8e44ad',
                      'clouds': '#ecf0f1',
                      'silver': '#bdc3c7',
                      'wetasphalt': '#34495e',
                      'midnightblue': '#2c3e50',
                      'concrete': '#95a5a6',
                      'asbestos': '#7f8c8d'}
        self.index = { 0: 'torquoise',
                       1: 'greensea',
                       2: 'sunflower',
                       3: 'orange',
                       4: 'emerald',
                       5: 'nephritis',
                       6: 'carrot',
                       7: 'pumpkin',
                       8: 'peterriver',
                       9: 'belizehole',
                      10: 'alizarin',
                      11: 'pomegranate',
                      12: 'amethyst',
                      13: 'wisteria',
                      14: 'clouds',
                      15: 'silver',
                      16: 'wetasphalt',
                      17: 'midnightblue',
                      18: 'concrete',
                      19: 'asbestos'}

    def __getitem__(self, item):
        try:
            if isinstance(item, int):
                return self.__get_color_by_index(item)
            elif isinstance(item, str):
                return self.color[item.replace(' ', '').lower()]
            else:
                raise
        except:
            raise Exception('No such color or index {}'.format(item))

    def __get_color_by_index(self, i):
        return self.color[self.index[i]]

    def __str__(self):
        return self.show_color_list()

    def show_color_list(self):
        return _color_list_beautify(self)

    def extract_random_color(self):
        return self.__get_color_by_index(randint(0, len(self.color) - 1))


if __name__ == '__main__':
    color1 = FlatUIColors()
    print(color1.extract_random_color())
    print(color1)
