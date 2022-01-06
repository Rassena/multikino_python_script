from datetime import date, time


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
            if type(value) is str or type(value) is date or type(value) is time:
                values.append(f'\'{value}\'')
            elif type(value) is set:
                values.append(f'{list(value)}')
            else:
                values.append(f'{value}')
        values_merged = ', '.join(values).replace('[', '{').replace(']', '}')
        return f'INSERT INTO \n{self.__class__.__name__} ({keys})\n VALUES \n({values_merged});\n'

    def __str__(self):
        all_merged = '\t'.join(f'{key}: \033[94m{self.__dict__[key]}\033[0m' for key in self.__dict__.keys())
        class_ = f'\033[96m{self.__class__.__name__.ljust(11)}\033[0m'
        return  f'{class_} {all_merged}'
