# coding=utf-8
"""
xxx
"""
__author__ = 'hermes'


# noinspection PyDocstring
class Stack(object):
    """
    """

    def __init__(self):
        """
        """
        self.__list = ['$']
        self.__size = 0
        self.__top = '$'

    def push(self, value):
        """
        """
        self.__list.append(value)
        self.__size += 1
        self.__top = value

        return None

    def pop(self):
        """
        """
        if self.__size < 0:
            raise Exception("stack empty")
        else:
            listTemp = []
            for at in range(0, self.__list.__len__() - 1):
                listTemp.append(self.__list[at])
            self.__list = listTemp
            self.__size -= 1
            if self.__size < 0:
                self.__top = None
            else:
                self.__top = self.__list[self.__size]

    def len(self):
        """
        """
        return int(self.__size)

    def __len__(self):
        """
        """
        return int(self.__size + 1)

    def top(self):
        """
        """
        return type(self.__top)(self.__top)

    def __del__(self):
        """
        """
