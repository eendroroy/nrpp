# coding=utf-8
"""
xxx
"""
__author__ = 'indrajit'

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

    def __removeDuplicate(self, _list):
        temp = [{}]
        for i in _list:
            if not temp.__contains__(i):
                temp.append(i)
        temp.remove({})
        return temp

    def getFollowObj(self):
        return self.__followObj

    def getFirstObj(self):
        return self.__firstObj

    def getGrammarObj(self):
        return self.__grammarObj

    def getParseTable(self):
        return self.__parseTable

    def generateParseTable(self):
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

        self.__parseTable = self.__removeDuplicate(self.__parseTable)
        self.__parseTable.remove({'variable': "", 'terminal': "", 'product': [[]]})

        return self

    def printParseTable(self):
        for each in self.__parseTable:
            print (each)
        return self

    def printToFile(self):
        OUTPUT = open("parseTable.txt", "w+")
        _list = self.__terminalList
        _list.append("$")
        for eachV in self.__variableList:
            OUTPUT.write("-------------------------------------------------------\n" + eachV + "\n")

            for eachT in _list:
                for eachR in self.__parseTable:
                    if not eachR.get('variable') == eachV:
                        continue
                    if not eachR.get('terminal') == eachT:
                        continue
                    OUTPUT.write("\t\t-----------------------------------------------\n\t\t->" + eachT + "\n\t\t\t\t ")
                    for eachS in eachR.get('product'):
                        OUTPUT.write(eachS + " ")
                    OUTPUT.write("\n")
        OUTPUT.write("-------------------------------------------------------")
        OUTPUT.close()


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

ParseTable().generateParseTable().printParseTable()
ParseTable().generateParseTable().printToFile()
