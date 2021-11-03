import mysql.connector
from all_tables import AllTables
from supporting_methods import AddableToDatabase


class Connection():
    mycursor = None
    mydb = None

    def __init__(self):
        self.mydb = mysql.connector.connect(host="25.89.241.139", user="root", password="pdb_2021", database="multikino")
        self.mycursor = self.mydb.cursor()

    def add_addable_element(self, addable_element: AddableToDatabase):
        self.mycursor.execute(addable_element.sql_addable, addable_element.__dict__)
        self.mydb.commit()

    # def add_users(self, users_array):
    #     sql = "INSERT INTO User (User_name, User_surname, User_email, user_password, User_birth) VALUES (%s, %s, %s, %s, %s)"
    #     for u in users_array:
    #         val = (u.User_name, u.User_surname, u.User_email, u.User_password, u.User_birth)
    #         self.mycursor.execute(sql, val)
    #         self.mydb.commit()
    #
    #
    # def add_artists(self, artist_array):
    #     sql = "INSERT INTO Artist (Artist_name, Artist_surname, Artist_birth, Artist_gender) VALUES (%s, %s, %s, %s)"
    #     for a in artist_array:
    #         val = (a.Artist_name, a.Artist_surname, a.Artist_birth, a.Artist_gender)
    #         self.mycursor.execute(sql, val)
    #         self.mydb.commit()


if __name__ == "__main__":
    conn = Connection()

    conn.mycursor.execute("SHOW TABLES")
    for x in conn.mycursor:
        print(x)

    conn.add_users(users)
    conn.add_artists(artists)
