import datetime

import names

from f2_0_constants import *
from f2_1_supporting_methods import *
from f2_2_parent_classes import ObjectWithCounter, AddableToDatabase


class Users(ObjectWithCounter, AddableToDatabase):
    genders = {False: 'male', True: 'female'}

    def __init__(self):
        self.id_user: int = Users.next()
        gender_id = random.choice([False, True])
        self.user_name: str = names.get_first_name(gender=self.genders[gender_id])
        self.user_surname: str = names.get_last_name()
        self.user_email: str = f'{self.user_surname}.{self.user_name}.{random_string_generator(random.randrange(3, 6))}@gmail.com'.lower()
        self.user_password: str = random_string_generator(random.randrange(8, 12))
        self.user_birth: date = random_date_generator(1970, 2003)
        self.user_privilege: set[str] = set(random.choices(PRIVILAGES, weights=[100, 10, 1, 1, 1], k=random.randrange(1, 2)))


class Artists(ObjectWithCounter, AddableToDatabase):
    genders = {False: 'male', True: 'female'}

    def __init__(self):
        self.Id_artist: int = Artists.next()
        gender_id = random.choice([False, True])
        self.artist_name: str = names.get_first_name(gender=self.genders[gender_id])
        self.artist_surname: str = names.get_last_name()
        self.artist_birth: date = random_date_generator(1960, 2000)
        self.artist_gender: bool = gender_id


class Dimensions(AddableToDatabase):
    def __init__(self, dimension_name: str, dimension_base_price: int):
        self.dimension_name: str = dimension_name
        self.dimension_basePrice: float = dimension_base_price


class Movies(ObjectWithCounter, AddableToDatabase):
    # ALL_TAGS_TRANSLATION_DIMENSION: set[tuple[str, str, float]] = set([
    #     (translation, dimension, random.choice(PRICES)) for translation in TRANSLATIONS for dimension in DIMENSIONS
    # ])

    def __init__(self, title, tuples_trans_dim_price):
        self.id_movie: int = Movies.next()
        self.movie_title: str = title
            # f'Movie name {random_string_generator(5)}'
        self.movie_description: str = random_string_generator(100)
        self.movie_premiere: date = random_date_generator(2000, 2022)
        self.movie_duration: int = random.randrange(90, 200) #:Movie_duration > 0)
        self.age_restriction: str = random.choice(AGE_RESTRICTIONS)
        self.poster_path: str = f'C:\\posters\\{self.id_movie}\\{random_string_generator(4)}.tiff'
        self.tags_country: set[str] = set(random.choices(COUNTRIES, k=random.randrange(1, 3)))
        self.tags_translation_dimension_basePrice: set[tuple[str, str, float]] = \
            set(random.choices(list(tuples_trans_dim_price), k=random.randrange(1, 6)))


class Castings(ObjectWithCounter, AddableToDatabase):
    def __init__(self, artist: Artists, movie: Movies):
        self.artist_id: int = artist.Id_artist
        self.artist_name: str = artist.artist_name
        self.artist_surname: str = artist.artist_surname
        self.role_name: str = random.choices(ROLES, weights=[10, 1, 1], k=1)[0]
        self.movie_id: int = movie.id_movie
        self.movie_title: str = movie.movie_title


class Ratings(ObjectWithCounter, AddableToDatabase):
    def __init__(self, movie: Movies, user: Users):
        self.movie_id: int = movie.id_movie
        self.movie_title: str = movie.movie_title
        self.user_id: int = user.id_user
        self.rating_value: int = random.randint(1, 10) # 1 <= Rating_rate <= 10)


class Genres(ObjectWithCounter, AddableToDatabase):
    def __init__(self, movie: Movies, genre_name: str):
        self.Movie_id: int = movie.id_movie
        self.Movie_title: str = movie.movie_title
        self.Genre_name: str = genre_name


class Rooms(ObjectWithCounter, AddableToDatabase):
    NR_OF_SEATS = 15

    def __init__(self, room_sign: str):
        self.room_name: str = room_sign
        self.room_set_row_seatNr: set[tuple[str, int]] = set([
            (row, i)
            for row in SEAT_ROWS
            for i in range(self.NR_OF_SEATS)])


class Discounts(ObjectWithCounter, AddableToDatabase):
    def __init__(self, discount_name: str, discount_percentage: float, dimension: Dimensions):
        self.discount_name: str = discount_name
        self.dimension_name: str = dimension.dimension_name
        self.dimension_basePrice: float = dimension.dimension_basePrice
        self.discount_price: float = self.dimension_basePrice * (1 - discount_percentage)


class Showings(ObjectWithCounter, AddableToDatabase):
    def __init__(self, movie: Movies, room: Rooms, list_all_discounts: list[Discounts]):
        self.id_showing: int = Showings.next()

        self.showing_date: date = random_date_generator(2021, 2022)
        self.showing_time: time = random_time_generator()

        self.movie_id: int = movie.id_movie
        self.movie_title: str = movie.movie_title

        trans_dimension_base_price = random.choice(list(movie.tags_translation_dimension_basePrice))
        self.movie_translation: str = trans_dimension_base_price[0]
        self.movie_duration: int = movie.movie_duration

        self.dimension_name: str = trans_dimension_base_price[1]
        self.dimension_basePrice: float = trans_dimension_base_price[2]
        self.set_discountName_price: set[tuple[str, float]] = \
            set([(discount.discount_name, discount.discount_price)
                 for discount in list_all_discounts if discount.dimension_name == self.dimension_name
                 ])

        self.room_name: str = room.room_name
        self.room_set_row_seatNr: set[tuple[str, int]] = room.room_set_row_seatNr


class Reservations(ObjectWithCounter, AddableToDatabase):
    def __init__(self, showing: Showings, user: Users):
        self.Id_reservation: int = Reservations.next()

        self.Showing_id: int = showing.id_showing
        self.Showing_date: date = showing.showing_date
        self.Showing_time: time = showing.showing_time

        self.Movie_id: int = showing.movie_id
        self.Movie_title: str = showing.movie_title
        self.Movie_translation: str = showing.movie_translation
        self.Set_discountName_price: set[tuple[str, float]] = showing.set_discountName_price

        self.User_id: int = user.id_user
        self.User_surname: str = user.user_surname
        self.dimension_name: str = showing.dimension_name

        self.Room_name: str = showing.room_name
        self.Map_ticket_row_seatNr: map[int: tuple[str, int]] = {}

    def update_tickets(self, ticket_list):
        for ticket in ticket_list:
            self.Map_ticket_row_seatNr.update({ticket.id_ticket: (ticket.Room_row, ticket.Room_seat)})


class Tickets(ObjectWithCounter, AddableToDatabase):
    def __init__(self, reservation: Reservations, row: str, seat: int):
        self.id_ticket: int = Tickets.next()

        self.Showing_id: int = reservation.Showing_id
        self.Showing_date: date = reservation.Showing_date
        self.Showing_time: time = reservation.Showing_time

        self.Movie_title: str = reservation.Movie_title
        self.Movie_translation: str = reservation.Movie_translation

        discount = random.choice(list(reservation.Set_discountName_price))
        self.Discount_name: str = discount[0]
        self.Discount_price: float = discount[1]

        self.Dimension_name: str = reservation.dimension_name

        self.Room_name: str = reservation.Room_name
        self.Room_row: str = row
        self.Room_seat: int = seat

        self.User_id: int = reservation.User_id
        self.User_surname: str = reservation.User_surname

        self.Ticket_state: str = random.choices(TICKET_STATES, weights=[3, 10, 10, 1], k=1)[0]
        self.Ticket_reservation: int = reservation.Id_reservation


class TicketStates(ObjectWithCounter, AddableToDatabase):
    def __init__(self, ticket: Tickets, ticketState_name):
        self.TicketState_timestamp = f'{random_date_generator(2021, 2022)} {random_time_generator()}+0000'
        self.TicketState_name = ticketState_name #random.choices(TICKET_STATES, weights=[3, 10, 10, 1], k=1)[0]

        self.Ticket_id: int = ticket.id_ticket
        self.Room_row: str = ticket.Room_row
        self.Room_seat: int = ticket.Room_seat

        self.reservation_id: int = ticket.Showing_id
        self.Showing_date: date = ticket.Showing_date
        self.Showing_time: time = ticket.Showing_time

        self.Movie_title: str = ticket.Movie_title
        self.User_id: int = ticket.User_id
        self.User_surname: str = ticket.User_surname
        self.Ticket_reservation: int = ticket.Ticket_reservation
