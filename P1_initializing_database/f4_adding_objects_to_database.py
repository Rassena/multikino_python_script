import mysql.connector
from P1_initializing_database.f3_creating_all_objects import AllMultikinoEntities
from P1_initializing_database.f2_2_parent_classes import AddableToDatabase

VIRTUAL_MACHINE = "25.3.64.93"
MICHAL = "25.89.241.139"
LOCALHOST = 'localhost'


class Connection:
    def __init__(self, host_ip):
        self.mydb = mysql.connector.connect(host=host_ip, user="root", password="pdb_2021", database="multikino")
        self.mycursor = self.mydb.cursor()

    def add_addable_element(self, addable_element: AddableToDatabase) -> None:
        """
        Method for adding entity to database.
        """

        """
        addable_element.sql_addable is a string in a form of:
            "INSERT INTO ClassName (Atr_1, Atr_2) VALUES (%(Atr_1)s, %(Atr_2)s)"
        
        addable_element.__dict__ is a dictionary in a form of:
            {'Atr_1': val1, 'Atr_2': val2}
        """
        self.mycursor.execute(addable_element.sql_addable, addable_element.__dict__)  # this should work, analogical to:
        # https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
        self.mydb.commit()


if __name__ == "__main__":
    # conn = Connection(host_ip=VIRTUAL_MACHINE)
    # conn = Connection(host_ip=MICHAL)
    conn = Connection(host_ip=LOCALHOST)

    all_tables = AllMultikinoEntities().all_entities
    errors = 0
    current = 0
    for element in all_tables:
        try:
            conn.add_addable_element(element)
            current += 1
            if current % 200 == 0:
                print(f'{current}: Current added {element}')
        except mysql.connector.errors.IntegrityError as e:
            print(e)
            errors += 1

    print(f'ERRORS: {errors}/{len(all_tables)}')
