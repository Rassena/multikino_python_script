import datetime

import cassandra
from cassandra.cluster import Cluster, ResponseFuture, ResultSet
from f2_creating_all_objects import AllMultikinoEntities
from f1_tables_as_classes import AddableToDatabase


def print_error(message):
    print(f'\033[91m{message}\033[0m')


class Connection:
    def __init__(self):
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
            return e

    def init_tables(self, filename):
        all_init_commands = []
        with open(filename, 'r', encoding='utf-8') as f:
            full_command = []
            for command in f.readlines():
                full_command.append(command.replace('\n', ''))
                if full_command[-1].endswith(';'):
                    all_init_commands.append('\n'.join(full_command))
                    full_command = []

        for init_command in all_init_commands:
            print(init_command)
            try:
                self.__session.execute(init_command)
            except Exception as e:
                print_error(e.__str__())


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    conn = Connection()
    # conn.init_tables('f0_tables.cql')

    all_tables = AllMultikinoEntities().all_entities

    current = 0
    for element in all_tables:
        res = conn.add_entity(element)
        if res is None:
            current += 1
        else:
            print_error(f'ERROR for {element.__class__.__name__}:\t{res}')
        if res is None and current % 3 == 0:
            print(f'{current}: Current added {element}')

    print(len(all_tables))
    print(f'{(datetime.datetime.now() - start_time).seconds} seconds')
    # print(f'{(datetime.datetime.now() - start_time).min} minutes')
