import mysql.connector
from all_tables import AllMultikinoEntities
from supporting_methods import AddableToDatabase


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
    conn = Connection(host_ip="25.3.64.93")

    conn.mycursor.execute("SHOW TABLES")
    count_en = 0
    for x in conn.mycursor:
        print(x)
        count_en += 1

    print(f'all: {count_en}')

    all_tables = AllMultikinoEntities().all_entities
    errors = 0
    current = 0
    for element in all_tables:
        # print(element)
        try:
            conn.add_addable_element(element)
            current+=1
            if current % 200 == 0:
                print(f'{current}: Current added {element}')
        except mysql.connector.errors.IntegrityError as e:
            print(e)
            errors += 1

    print(f'ERRORS: {errors}/{len(all_tables)}')
    # # for error in errors: print(f'{error}')

