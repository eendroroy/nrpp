# coding=utf-8
"""
Parser
"""
__author__ = 'hermes'

from parseTable import ParseTable
from stack import Stack


class Parser(object):
    """
    Parser class
    """

    def __init__(self):
        self.__parseTableObj = ParseTable()
        self.__parseTable = ParseTable().getParseTable()
        self.__input = Stack()
        self.__product = Stack()

