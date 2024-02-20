class Bank:
    def __init__(self, name, age, money, key):
        self._name = name
        self._age = age
        self.__money = money
        self.__key = key

    def set_name(self, name):
        self._name = name
        return self._name
    def get_name(self):
        return self._name


class Bank2(Bank):
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key

class User(Bank2):

    @property
    def name(self):
        return self._name
    @name.setter
    def set_name(self, name):
        self._name = name
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, age):
        self._age = age
        return self._age

    @property
    def money(self):
        return self.__money

    @money.setter
    def set_money(self, money):
        self.__money = money
        return self.__money

    @property
    def key(self):
        return self.__key

    @key.setter
    def set_key(self, key):
        self.__key = key
        return self.__key

