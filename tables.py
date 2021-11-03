import random
import string
from datetime import date, time, timedelta
from constants import *
import names


def random_string_generator(length) -> str:
    rand_signs = string.ascii_letters + string.digits
    return ''.join([random.choice(rand_signs) for i in range(length)])


def random_lowercase(length) -> str:
    rand_signs = string.ascii_lowercase
    return ''.join([random.choice(rand_signs) for i in range(length)])


def random_date_generator() -> date:
    start_date = date(2021, 1, 1)
    end_date = date(2022, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    return random_date


def random_time_generator() -> time:
    pass


class AgeRestriction:
    AgeRestriction_counter = 0

    def __init__(self, age_restriction_name: str):
        self.Id_ageRestriction: int = AgeRestriction.AgeRestriction_counter
        AgeRestriction.AgeRestriction_counter += 1
        self.AgeRestriction_name: str = age_restriction_name


class Room:
    Room_counter = 0

    def __init__(self, room_sign: str):
        self.Id_room: int = Room.Room_counter
        Room.Room_counter += 1
        self.Room_sign: str = room_sign


class ReservationState:
    ReservationState_counter = 0

    def __init__(self, reservation_state_name: str):
        self.Id_reservationState: int = ReservationState.ReservationState_counter
        ReservationState.ReservationState_counter += 1
        self.ReservationState_name: str = reservation_state_name


class Role:
    Role_counter = 0

    def __init__(self, role_name: str):
        self.Id_role: int = Role.Role_counter
        Role.Role_counter += 1
        self.Role_name: str = role_name


class Translation:
    Translation_counter = 0

    def __init__(self, translation_name: str):
        self.Id_translation: int = Translation.Translation_counter
        Translation.Translation_counter += 1
        self.Translation_name = translation_name


class Artist:
    Artist_counter = 0
    genders = {False: 'male', True: 'female'}

    def __init__(self):
        self.Id_artist: int = Artist.Artist_counter
        Artist.Artist_counter += 1
        gender_id = random.choice([False, True])
        self.Artist_name: str = names.get_first_name(gender=self.genders[gender_id])
        self.Artist_surname: str = names.get_last_name()
        self.Artist_birth: date = random_date_generator()
        self.Artist_gender: bool = gender_id


class User:
    User_counter = 0
    genders = {False: 'male', True: 'female'}

    def __init__(self):
        self.Id_use: int = User.User_counter
        User.User_counter += 1
        gender_id = random.choice([False, True])
        self.User_name: str = names.get_first_name(gender=self.genders[gender_id])
        self.User_surname: str = names.get_last_name()
        self.User_email: str = f'{random_string_generator(random.randrange(6, 12))}@gmail.com'
        self.User_password: str = random_string_generator(random.randrange(8, 12))
        self.User_birth: date = random_date_generator()


class Seat:
    Seat_counter = 0
    MAX_SEAT_IN_ROW = 15
    rooms_seats = {}

    def __init__(self, fk_room: int):
        self.Id_seat: int = Seat.Seat_counter
        Seat.Seat_counter += 1

        if fk_room not in Seat.rooms_seats.keys():
            Seat.rooms_seats[fk_room] = 0
        else:
            Seat.rooms_seats[fk_room] += 1

        self.Seat_row: str = Seat.rooms_seats[fk_room] // Seat.MAX_SEAT_IN_ROW + 1
        self.Seat_number: int = Seat.rooms_seats[fk_room] % Seat.MAX_SEAT_IN_ROW + 1
        # Seat_number > 0)
        self.Fk_room: int = fk_room


class Movie:
    Movie_counter = 0

    def __init__(self, fk_age_restriction: int):
        self.Id_movie: int = Movie.Movie_counter
        Movie.Movie_counter += 1

        self.Movie_name: str = f'Movie name {random_string_generator(5)}'
        self.Movie_description: str = random_string_generator(100)
        self.Movie_premiere: date = random_date_generator()
        self.Movie_duration: int = random.randrange(90, 200)
        #:Movie_duration > 0)
        self.Fk_ageRestriction: int = fk_age_restriction


class CastAssignment:
    CastAssignment_counter = 0

    def __init__(self, fk_artist, fk_movie, fk_role):
        self.Id_castAssignment: int = CastAssignment.CastAssignment_counter
        CastAssignment.CastAssignment_counter += 1
        self.Fk_artist: int = fk_artist
        self.Fk_movie: int = fk_movie
        self.Fk_role: int = fk_role


class Country:
    Country_counter = 0

    def __init__(self, country_name: str):
        self.Id_country = Country.Country_counter
        Country.Country_counter += 1
        self.Country_name: str = country_name


class Dimension:
    Dimension_counter = 0

    def __init__(self, dimension_name: str):
        self.Id_dimension: int = Dimension.Dimension_counter
        Dimension.Dimension_counter += 1
        self.Dimension_name: str = dimension_name


class Discount:
    Discount_counter = 0

    def __init__(self, discount_name: str):
        self.Id_discount = Discount.Discount_counter
        Discount.Discount_counter += 1
        self.Discount_name: str = discount_name


class Genre:
    Genre_counter = 0

    def __init__(self, genre_name: str):
        self.Id_genre: int = Genre.Genre_counter
        Genre.Genre_counter += 1
        self.Genre_name: str = genre_name


class MovieVersion:
    MovieVersion_counter = 0

    def __init__(self, fk_translation: int, fk_dimension: int):
        self.Id_movieVersion: int = MovieVersion.MovieVersion_counter
        MovieVersion.MovieVersion_counter += 1
        self.Fk_translation = fk_translation
        self.Fk_dimension = fk_dimension


class Movie_Country:
    Movie_Country_counter = 0

    def __init__(self, fk_movie: int, fk_country: int):
        self.Id_movie_country: int = Movie_Country.Movie_Country_counter
        Movie_Country.Movie_Country_counter += 1
        self.Fk_movie = fk_movie
        self.Fk_country = fk_country


class Movie_Genre:
    Movie_Genre_counter = 0

    def __init__(self, fk_movie: int, fk_genre: int):
        self.Id_movie_genre: int = Movie_Genre.Movie_Genre_counter
        Movie_Genre.Movie_Genre_counter += 1
        self.Fk_movie = fk_movie
        self.Fk_genre = fk_genre


class Movie_MovieVersion:
    Movie_MovieVersion_counter = 0

    def __init__(self, fk_movie: int, fk_movieVersion: int):
        self.Id_movie_movieVersion: int = Movie_MovieVersion.Movie_MovieVersion_counter
        Movie_MovieVersion.Movie_MovieVersion_counter += 1
        self.Fk_movie = fk_movie
        self.Fk_movieVersion = fk_movieVersion


class Poster:
    Poster_counter = 0

    def __init__(self, fk_movie: int):
        self.Id_poster: int = Poster.Poster_counter
        Poster.Poster_counter += 1
        self.Fk_movie = fk_movie
        self.Poster_path = f'C:\posters\{self.Fk_movie}\{random_string_generator(4)}.tiff'


class Price:
    Price_counter = 0

    def __init__(self, price_value: float):
        self.Id_price = Price.Price_counter
        Price.Price_counter += 1
        self.Price_value: float = price_value


class Privilege:
    Privlege_counter = 0

    def __init__(self, privilege_name: str):
        self.Id_privilege: int = Privilege.Privlege_counter
        Privilege.Privlege_counter += 1
        self.Privilege_name = privilege_name


class PrivilegeAssignment:
    PrivilegeAssignment_counter = 0

    def __init__(self, fk_user: int, fk_privilege: int):
        self.Id_privilegeAssignment: int = PrivilegeAssignment.PrivilegeAssignment_counter
        PrivilegeAssignment.PrivilegeAssignment_counter += 1
        self.Fk_user = fk_user
        self.Fk_privilege = fk_privilege


class Rating:
    Rating_counter = 0

    def __init__(self, fk_movie: int, fk_user: int):
        self.Id_rating: int = Rating.Rating_counter
        Rating.Rating_counter += 1
        self.Fk_movie = fk_movie
        self.Fk_user = fk_user
        self.Rating_rate = random.randint(1, 10) # 1 <= Rating_rate <= 10)


class Seans:
    Seans_counter = 0

    def __init__(self, fk_room: int, fk_movieVersion: int):
        self.Id_seans: int = Seans.Seans_counter
        Seans.Seans_counter += 1
        self.Fk_room = fk_room
        self.Fk_movieVersion = fk_movieVersion
        self.Seans_date = random_date_generator()


class Reservation:
    Reservation_count = 0

    def __init__(self, fk_seans: int, fk_reservationState: int, fk_user: int):
        self.Id_reservation: int = Reservation.Reservation_count
        Reservation.Reservation_count += 1
        self.Fk_seans = fk_seans
        self.Fk_reservationState = fk_reservationState
        self.Fk_user = fk_user


class Ticket:
    # Id_ticket: int
    Fk_seat: int
    Fk_reservation: int
    Fk_discount: int
    Fk_price: int

    def __init__(self):
        # self.
        self.Fk_seat = random.randint(1, SEAT)
        self.Fk_reservation = random.randint(1, RESERVATION)
        self.Fk_discount = random.randint(1, len(DISCOUNTS))
        self.Fk_price = random.randint(1, len(PRICE))
