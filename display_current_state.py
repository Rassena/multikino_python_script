from connecting_to_database import Connection, VIRTUAL_MACHINE
from inspect import isclass
import tables

if __name__ == '__main__':
    conn = Connection(host_ip=VIRTUAL_MACHINE)
    classes = ['AgeRestriction', 'Artist', 'CastAssignment', 'Country', 'Dimension', 'Discount', 'Genre',
               'Movie', 'MovieVersion', 'Movie_Country', 'Movie_Genre', 'Movie_MovieVersion', 'Poster',
               'Price', 'Privilege', 'PrivilegeAssignment', 'Rating', 'Reservation', 'ReservationState',
               'Role', 'Room', 'Seans', 'Seat', 'Ticket', 'Translation', 'User']
    for tab_name in classes:

        conn.mycursor.execute(f'SELECT count(*) FROM {tab_name}')
        print(f'{tab_name} : {[x for x in conn.mycursor][0][0]}')