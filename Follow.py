# coding=utf-8
"""
Follow class
"""
__author__ = 'indrajit'

from Grammar import Grammar
from First import First


class Follow(object):
    """END"""

    def __init__(self):
        self.__firstObj = First()
        self.__grammarObj = Grammar("input.txt")
        self.first_list = self.get_first_object().get_first()

        self.__variableList = self.__grammarObj.get_variables()
        self.__terminalList = self.__grammarObj.get_terminals()
        self.__grammarList = self.__grammarObj.get_grammar_list()

        self.__followList = [{'variable': "", 'follow': []}]
        self.__generate_follow()

    @staticmethod
    def __remove_duplicate(_list):
        temp_list = []
        for i in _list:
            if not temp_list.__contains__(i):
                temp_list.append(i)
            else:
                continue
        return temp_list

    def __get_follow_of(self, var):
        follow_temp = {}
        for follow_temp in self.__followList:
            if follow_temp.get('variable') == var:
                break
        return list(follow_temp.get('follow'))

    def __generate_follow(self):
        """
        """
        for variableT in self.__variableList:
            flag = True
            follow_temp = []

            if self.__variableList[0] == variableT:
                follow_temp.append("$")

            for rule in self.__grammarList:
                if not rule['product'].__contains__(variableT):
                    continue
                else:
                    for tran in range(0, rule.get('product').__len__()):
                        if rule.get('product')[tran] == variableT:
                            if not (tran + 1) < rule.get('product').__len__():
                                if not follow_temp.__contains__(rule.get('variable')) and not rule.get(
                                        'variable') == variableT:
                                    follow_temp.append(rule.get('variable'))
                            else:
                                if self.__variableList.__contains__(rule.get('product')[tran + 1]):
                                    temp2 = self.__firstObj.get_first_of(rule.get('product')[tran + 1])
                                    if temp2.__contains__('EFS'):
                                        temp2.remove('EFS')
                                        temp2.extend(self.__get_follow_of(rule.get('variable')))
                                    follow_temp.extend(temp2)
                                else:
                                    follow_temp.append(rule.get('product')[tran + 1])
            temp_list = []
            for followIter in follow_temp:
                if not temp_list.__contains__(followIter):
                    temp_list.append(followIter)
            follow_temp = temp_list
            self.__followList.append({'variable': variableT, 'follow': follow_temp})

            while flag:
                flag = False

                for _iter in range(0, self.__followList.__len__()):
                    for variableT in self.__followList[_iter]['follow']:
                        if self.__variableList.__contains__(variableT):
                            self.__followList[_iter]['follow'].remove(variableT)
                            self.__followList[_iter]['follow'].extend(self.__get_follow_of(variableT))
                            self.__followList[_iter]['follow'] = self.__remove_duplicate(
                                self.__followList[_iter]['follow'])
                            flag = True

        self.__followList.remove({'variable': "", 'follow': []})

        return self

    # noinspection PyDocstring
    def print_follow_list(self):
        """
        """
        for followIter in self.__followList:
            print(followIter)
        return self

    # noinspection PyDocstring
    def get_grammar_object(self):
        """
        """
        return self.__grammarObj

    # noinspection PyDocstring
    def get_first_object(self):
        """
        """
        return self.__firstObj

    def get_follow_of(self, var):
        """
        :param var: Dynamic
        """
        return list(self.__get_follow_of(var))

    def __del__(self):
        """
        """
        del self
