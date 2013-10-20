# coding=utf-8
"""
xxx
"""
__author__ = 'eendro'


# noinspection PyShadowingBuiltins,PyDocstring
class Grammar(object):
    """
    """

    def __init__(self, input):
        """
        initializer
        :type input: object
        """
        self.__grammarFile = "~~$normalizedGrammar"
        self.__grammarList = [dict(variable="", product=[])]
        self.__variables = []
        self.__terminals = []
        self.input = input
        self.__normalize()

    def get_grammar_file(self, mode="r+"):
        """
        returns file, named __grammar
        """

        return open(self.__grammarFile, mode)

    def get_grammar_list(self):
        """
        """
        return list(self.__grammarList)

    def get_variables(self):
        """
        returns __variables
        """
        return list(self.__variables)

    def get_terminals(self):
        """
        returns __terminals
        """
        return list(self.__terminals)

    def __normalize(self):
        """
        """
        self.__normalize_to_list()
        return self

    def __normalize_to_file(self):
        """
        split multiple rules
        """
        file = open(self.input.__str__(), "r+")
        lines = file.readlines()
        variables = []
        terminals = []
        grammar = [()]
        grammar.remove(())

        for LINE in lines:
            words = LINE.split("->")

            if words.__getitem__(words.__len__() - 1).endswith("\n"):
                temp = words.__getitem__(words.__len__() - 1)
                words.remove(temp)
                words.append(temp[:-len("\n")])

            if words.__len__() < 2:
                continue

            variables = variables.__add__([words[0][:words[0].__len__() - 1]])
            words2 = words[1].split("|")

            for RULE in words2:
                grammar = grammar.__add__([(words[0][:words[0].__len__() - 1], RULE.split())])

        normalized_grammar = open(self.__grammarFile, "w+")

        for i in grammar:
            normalized_grammar.write(i[0])
            normalized_grammar.write(" -> ")

            for j in range(0, i[1].__len__()):
                normalized_grammar.write(i[1][j])

                if not terminals.__contains__(i[1][j]):
                    terminals.append(i[1][j])

                if j < i[1].__len__() - 1:
                    normalized_grammar.write(" ")

            normalized_grammar.write("\n")

        normalized_grammar.close()
        self.__variables = variables
        self.__terminals = terminals

        for i in self.__variables:
            while self.__terminals.__contains__(i):
                self.__terminals.remove(i)

        file.close()

        return None

    def __normalize_to_list(self):
        """
        """

        self.__normalize_to_file()

        file = open(self.__grammarFile, "r+")
        lines = file.readlines()
        grammar = [dict(variable="", product=[])]

        for LINE in lines:
            words = LINE.split(" -> ")
            if words.__len__() < 2:
                continue
            if words[1].__contains__('\n'):
                words[1] = words[1][:words[1].__len__() - 1]
            grammar.append({'variable': words[0], 'product': words[1].split()})

        grammar.remove(dict(variable="", product=[]))
        self.__grammarList = grammar

        return None

    def print_grammar_file(self):
        """
        print attributes
        """
        temp = self.get_grammar_file()
        lines = temp.readlines()
        for line in lines:
            print (line)

        return None

    def print_grammar_list(self):
        """
        """
        for i in self.__grammarList:
            print(i)

        return None

    def __del__(self):
        """
        destructor
        """
