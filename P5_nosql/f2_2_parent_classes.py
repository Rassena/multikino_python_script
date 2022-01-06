from datetime import date


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
        example: "INSERT INTO ClassName (Atr_1, Atr_2) VALUES (Atr_1, Atr_2)"
        """
        keys = ', '.join(self.__dict__.keys())
        values = []
        for value in self.__dict__.values():
            if type(value) is str or type(value) is date:
                values.append(f'\'{value}\'')
            elif type(value) is set:
                values.append(f'{list(value)}')
            elif type(value) is bool:
                values.append(f'{value}'.lower())
            else:
                values.append(f'{value}')
        values_merged = ', '.join(values).replace('[', '{').replace(']', '}')
        return f'INSERT INTO \n{self.__class__.__name__} ({keys})\n VALUES \n({values_merged});\n'

    def __str__(self):
        keys, values = '', ''
        if len(self.__dict__) > 0:
            keys = ', '.join(self.__dict__.keys())
            values = ', '.join([str(value) for value in self.__dict__.values()])
        return f'{self.__class__.__name__} ({keys}) : ({values})'
