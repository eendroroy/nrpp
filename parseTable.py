# coding=utf-8
"""
xxx
"""
__author__ = 'eendro'

from Follow import Follow


# noinspection PyDocstring
class ParseTable(object):
    """
    """

    def __init__(self):
        self.__followObj = Follow()
        self.__grammarObj = self.__followObj.get_grammar_object()
        self.__firstObj = self.__followObj.get_first_object()
        self.__variableList = self.__grammarObj.get_variables()
        self.__terminalList = self.__grammarObj.get_terminals()
        self.__parseTable = [{'variable': "", 'terminal': "", 'product': [[]]}]

    @staticmethod
    def __remove_duplicate(_list):
        temp = [{}]
        for i in _list:
            if not temp.__contains__(i):
                temp.append(i)
        temp.remove({})
        return temp

    def get_follow_object(self):
        return self.__followObj

    def get_first_object(self):
        return self.__firstObj

    def get_grammar_object(self):
        return self.__grammarObj

    def get_parse_table(self):
        return self.__parseTable

    def generate_parse_table(self):
        """
        """
        rules = self.__grammarObj.get_grammar_list()
        for eachRule in rules:
            for each in self.__firstObj.get_first_of(eachRule['product'][0]):
                if each == "EFS":
                    self.__parseTable.append(
                        {'variable': eachRule.get('variable'), 'terminal': "$", 'product': eachRule.get('product')})
                    for eachF in self.__followObj.get_follow_of(eachRule.get('variable')):
                        self.__parseTable.append({'variable': eachRule.get('variable'), 'terminal': eachF,
                                                  'product': eachRule.get('product')})

                else:
                    self.__parseTable.append(
                        {'variable': eachRule.get('variable'), 'terminal': each, 'product': eachRule.get('product')})

        self.__parseTable = self.__remove_duplicate(self.__parseTable)
        self.__parseTable.remove({'variable': "", 'terminal': "", 'product': [[]]})

        return self

    def print_parse_table(self):
        for each in self.__parseTable:
            print (each)
        return self

    def print_to_file(self):
        output = open("parseTable.txt", "w+")
        _list = self.__terminalList
        _list.append("$")
        for eachV in self.__variableList:
            output.write("-------------------------------------------------------\n" + eachV + "\n")

            for eachT in _list:
                for eachR in self.__parseTable:
                    if not eachR.get('variable') == eachV:
                        continue
                    if not eachR.get('terminal') == eachT:
                        continue
                    output.write("\t\t-----------------------------------------------\n\t\t->" + eachT + "\n\t\t\t\t ")
                    for eachS in eachR.get('product'):
                        output.write(eachS + " ")
                    output.write("\n")
        output.write("-------------------------------------------------------")
        output.close()


fl = Follow()

fl.get_grammar_object().print_grammar_file()

print
print

fl.get_first_object().print_first()

print
print

fl.print_follow_list()

print
print

ParseTable().generate_parse_table().print_parse_table()
ParseTable().generate_parse_table().print_to_file()
