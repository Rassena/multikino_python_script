import datetime

from cassandra.cluster import Cluster
from f2_creating_all_objects import AllMultikinoEntities
from f1_tables_as_classes import AddableToDatabase


class Connection:
    def __init__(self):
        cluster = Cluster()
        self.__session = cluster.connect('multikino', wait_for_all_pools=True)
        self.__session.execute('USE multikino')

    def add_entity(self, entity: AddableToDatabase):
        return self.__session.execute(entity.sql_addable)


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    # conn = Connection()
    all_tables = AllMultikinoEntities().all_entities

    # current = 0
    # for element in all_tables:
    #     # print(element.sql_addable)
    #     # conn.add_entity(element)
    #     current += 1
    #     if current % 3 == 0:
    #         print(f'{current}: Current added {element}')

    print(len(all_tables))
    print(f'{(datetime.datetime.now() - start_time).seconds} seconds')
    # print(f'{(datetime.datetime.now() - start_time).min} minutes')
