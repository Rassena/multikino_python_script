import datetime

import cassandra
from cassandra.cluster import Cluster, ResponseFuture, ResultSet
from f2_creating_all_objects import AllMultikinoEntities
from f1_tables_as_classes import AddableToDatabase


def print_error(message):
    print(f'\033[91m{message}\033[0m')


def print_heading(message):
    print(f'\n\033[95m{message}\033[0m')


class Connection:
    def __init__(self):
        print_heading('INITIALIZING CONNECTION WITH DATABASE')
        cluster = Cluster()
        self.__session = cluster.connect('multikino', wait_for_all_pools=True)
        self.__session.execute('USE multikino')

    def add_entity(self, entity: AddableToDatabase):
        try:
            res: ResultSet = self.__session.execute(entity.sql_addable)
            all_merged = [x for x in res]
            if len(all_merged) == 0:
                return None
            return '\n'.join(all_merged)
        except Exception as e:
            res_mes = e.__str__()
            if res_mes.find('message="') != -1:
                return res_mes.split('message="')[1].replace('">', '')
            return res_mes

    def init_tables(self, filename):
        all_init_commands = []
        with open(filename, 'r', encoding='utf-8') as f:
            full_command = []
            for command in f.readlines():
                full_command.append(command.replace('\n', ''))
                if full_command[-1].endswith(';'):
                    all_init_commands.append('\n'.join(full_command))
                    full_command = []

        print_heading(f'INITIALIZING ALL TABLES FROM FILE: {filename}')
        for init_command in all_init_commands:
            print(init_command)
            try:
                self.__session.execute(init_command)
            except Exception as e:
                print_error(e.__str__())


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    conn = Connection()
    conn.init_tables('f0_tables.cql')

    print_heading('CREATING ALL OBJECTS TO BE ADDED:')
    all_obj = AllMultikinoEntities()
    all_tables = all_obj.all_entities

    print_heading('ADDING ALL OBJECTS:')
    current = 0
    errors = 0
    for element in all_tables:
        res = conn.add_entity(element)
        if res is None:
            current += 1
        else:
            errors += 1
            print_error(f'ERROR for {element.__class__.__name__}:\t{res}')
            # print(element.sql_addable)
        if res is None and (current % 500 == 0):
            print(f'{current:05}: {element}')

    print_heading('STATS:')
    print(f'ALL ADDED:  {current: 6}/{len(all_tables)}')
    print(f'ALL ERRORS: {errors: 6}/{len(all_tables)}')
    print(f'TIME:       {(datetime.datetime.now() - start_time).seconds//60} minutes')
    print_heading('NUMBER OF ENTITIES FOF EACH TABLE:')

    for list_ in all_obj.tab_with_all_tabs:
        if len(list_) > 0:
            print(f'\033[96m{list_[0].__class__.__name__.ljust(12)}\033[0m' + len(list_).__str__().rjust(5))
    # print(f'{(datetime.datetime.now() - start_time).min} minutes')
