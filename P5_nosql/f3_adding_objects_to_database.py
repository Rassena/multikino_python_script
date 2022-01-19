import datetime
import os
import threading

from cassandra.cluster import Cluster, ResultSet
from f2_creating_all_objects import AllMultikinoEntities
from f1_tables_as_classes import AddableToDatabase


def print_error(message):
    print(f'\033[91m{message}\033[0m')


def print_heading(message):
    print(f'\n\033[95m{message}\033[0m')


class Connection:
    def __init__(self, thread_name: str=""):
        print_heading(f'{thread_name} INITIALIZING CONNECTION WITH DATABASE')
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

exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, part_of_table):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.part_of_table = part_of_table
        self.current = 0
        self.errors = 0
        self.conn: Connection
    def run(self):
        self.conn = Connection(self.name)
        self.add_to_database()
        print("Exiting " + self.name)

    def add_to_database(self):
        for element in self.part_of_table:
            res = self.conn.add_entity(element)
            if res is None:
                self.current += 1
            else:
                self.errors += 1
                print_error(f'{self.name}: ERROR for {element.__class__.__name__}:\t{res}')
                # print(element.sql_addable)
            if res is None and (self.current % 1000 == 0):
                print(f'{self.name}: {self.current:05}: {element}')

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
    threads_count = os.cpu_count()

    part_of_table = int(len(all_tables)/threads_count)

    print(f'GENERATED:  {len(all_tables): 6} ELEMENTS')

    threads: myThread = [myThread(i, f'Thread-{i}', all_tables[part_of_table*i:part_of_table*(i+1)]) for i in range(threads_count-1)]
    threads += [myThread(threads_count-1, f'Thread-{threads_count-1}', all_tables[part_of_table*(threads_count-1):])]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print_heading('STATS:')
    for thread in threads:
        current = current + thread.current
        errors = errors + thread.errors
        print(f'{thread.name} ADDED:  {thread.current: 6}/{len(thread.part_of_table)}')
        print(f'{thread.name} ERRORS: {thread.errors: 6}/{len(thread.part_of_table)}')

    print(f'ALL ADDED:  {current: 6}/{len(all_tables)}')
    print(f'ALL ERRORS: {errors: 6}/{len(all_tables)}')
    print(f'TIME:       {(datetime.datetime.now() - start_time).seconds//60} minutes')
    print_heading('NUMBER OF ENTITIES FOF EACH TABLE:')

    for list_ in all_obj.tab_with_all_tabs:
        if len(list_) > 0:
            print(f'\033[96m{list_[0].__class__.__name__.ljust(12)}\033[0m' + len(list_).__str__().rjust(5))
    # print(f'{(datetime.datetime.now() - start_time).min} minutes')