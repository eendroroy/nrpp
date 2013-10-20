# coding=utf-8
"""
Grammar class
"""
__author__ = 'eendro'

from Grammar import Grammar


# noinspection PyDocstring
class First(object):
    """

    """

    def __init__(self):
        """
        """
        self.__grammarObj = Grammar("input.txt")
        self.__variableList = self.__grammarObj.get_variables()
        self.__terminalList = self.__grammarObj.get_terminals()
        self.__grammarList = self.__grammarObj.get_grammar_list()
        self.__firstList = [{'variable': "", 'first': []}]
        for _i in self.__variableList:
            self.__firstList.append({'variable': _i, 'first': []})
        self.__firstList.remove({'variable': "", 'first': []})
        self.__generate_first()

    def __get_first(self, var):
        """
        """
        global i
        for i in range(0, self.__firstList.__len__()):
            if self.__firstList[i].get('variable') == var:
                break
        return self.__firstList[i].get('first')

    @staticmethod
    def __remove_duplicate(temp):
        """
        """
        temp2 = []
        for _i in temp:
            if not temp2.__contains__(_i):
                temp2.append(_i)
            else:
                continue
        return temp2

    def get_grammar_list(self):
        """
        """
        return self.__grammarList

    def get_grammar(self):
        """
        """
        return self.__grammarObj

    def __generate_first(self):
        """
        """
        for var in range(0, self.__firstList.__len__()):
            for length in range(0, self.__grammarList.__len__()):
                if not self.__grammarList[length].get('variable') == self.__variableList[var]:
                    continue
                else:
                    if not self.__firstList[var]['first'].__contains__(self.__grammarList[length]['product'][0]):
                        self.__firstList[var]['first'].append(self.__grammarList[length]['product'][0])

        flag = True
        while flag:
            flag = False
            for var1 in range(0, self.__firstList.__len__()):
                self.__firstList[var1]['first'] = self.__remove_duplicate(self.__firstList[var1]['first'])
                if self.__firstList[var1]['variable'] in self.__firstList[var1]['first']:
                    self.__firstList[var1]['first'].remove(self.__firstList[var1]['variable'])
                for var2 in range(0, self.__firstList[var1]['first'].__len__()):
                    if self.__firstList[var1]['first'][var2] in self.__variableList:
                        flag = True
                        self.__firstList[var1]['first'].extend(self.__get_first(self.__firstList[var1]['first'][var2]))
                        self.__firstList[var1]['first'].remove(self.__firstList[var1]['first'][var2])
        return self

    def print_first(self):
        """
        """
        for f in self.__firstList:
            print (f)
        return None

    def get_first(self):
        """
        """
        return self.__firstList

    def get_first_of(self, var):
        """
        """
        if self.__terminalList.__contains__(var):
            return [var]
        for _i in range(0, self.__firstList.__len__()):
            if self.__firstList[_i]['variable'] == var:
                return list(self.__firstList[_i]['first'])

    def __del__(self):
        """
        """
