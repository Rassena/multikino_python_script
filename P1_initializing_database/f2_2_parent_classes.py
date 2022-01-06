class ObjectWithCounter:
    counter = 1

    @classmethod
    def next(cls):
        counter_val = cls.counter
        cls.counter += 1
        return counter_val


class AddableToDatabase:
    @property
    def sql_addable(self):
        """
        example: "INSERT INTO ClassName (Atr_1, Atr_2) VALUES (%(Atr_1)s, %(Atr_2)s)"
        """
        keys = ', '.join(self.__dict__.keys())
        keys_insertable = ', '.join([f'%({key})s' for key in self.__dict__.keys()])
        return f'INSERT INTO {self.__class__.__name__} ({keys}) VALUES ({keys_insertable})'

    def __str__(self):
        keys, values = '', ''
        if len(self.__dict__) > 0:
            keys = ', '.join(self.__dict__.keys())
            values = ', '.join([str(value) for value in self.__dict__.values()])
        return f'{self.__class__.__name__} ({keys}) : ({values})'
