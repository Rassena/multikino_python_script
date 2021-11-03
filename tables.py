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


class ObjectWithCounter:
    counter = 0


class AgeRestriction(ObjectWithCounter):
    def __init__(self, age_restriction_name: str):
        self.Id_ageRestriction: int = AgeRestriction.counter
        AgeRestriction.counter += 1
        self.AgeRestriction_name: str = age_restriction_name


class Room(ObjectWithCounter):
    def __init__(self, room_sign: str):
        self.Id_room: int = Room.counter
        Room.counter += 1
        self.Room_sign: str = room_sign


class ReservationState(ObjectWithCounter):
    def __init__(self, reservation_state_name: str):
        self.Id_reservationState: int = ReservationState.counter
        ReservationState.counter += 1
        self.ReservationState_name: str = reservation_state_name


class Role(ObjectWithCounter):
    def __init__(self, role_name: str):
        self.Id_role: int = Role.counter
        Role.counter += 1
        self.Role_name: str = role_name


class Translation(ObjectWithCounter):
    def __init__(self, translation_name: str):
        self.Id_translation: int = Translation.counter
        Translation.counter += 1
        self.Translation_name = translation_name


class Artist(ObjectWithCounter):
    genders = {False: 'male', True: 'female'}

    def __init__(self):
        self.Id_artist: int = Artist.counter
        Artist.counter += 1
        gender_id = random.choice([False, True])
        self.Artist_name: str = names.get_first_name(gender=self.genders[gender_id])
        self.Artist_surname: str = names.get_last_name()
        self.Artist_birth: date = random_date_generator()
        self.Artist_gender: bool = gender_id


class User(ObjectWithCounter):
    genders = {False: 'male', True: 'female'}

    def __init__(self):
        self.Id_use: int = User.counter
        User.counter += 1
        gender_id = random.choice([False, True])
        self.User_name: str = names.get_first_name(gender=self.genders[gender_id])
        self.User_surname: str = names.get_last_name()
        self.User_email: str = f'{random_string_generator(random.randrange(6, 12))}@gmail.com'
        self.User_password: str = random_string_generator(random.randrange(8, 12))
        self.User_birth: date = random_date_generator()


class Seat(ObjectWithCounter):
    MAX_SEAT_IN_ROW = 15
    rooms_seats = {}

    def __init__(self, fk_room: int):
        self.Id_seat: int = Seat.counter
        Seat.counter += 1

        if fk_room not in Seat.rooms_seats.keys():
            Seat.rooms_seats[fk_room] = 0
        else:
            Seat.rooms_seats[fk_room] += 1

        self.Seat_row: str = Seat.rooms_seats[fk_room] // Seat.MAX_SEAT_IN_ROW + 1
        self.Seat_number: int = Seat.rooms_seats[fk_room] % Seat.MAX_SEAT_IN_ROW + 1
        # Seat_number > 0)
        self.Fk_room: int = fk_room


class Movie(ObjectWithCounter):
    def __init__(self, fk_age_restriction: int):
        self.Id_movie: int = Movie.counter
        Movie.counter += 1

        self.Movie_name: str = f'Movie name {random_string_generator(5)}'
        self.Movie_description: str = random_string_generator(100)
        self.Movie_premiere: date = random_date_generator()
        self.Movie_duration: int = random.randrange(90, 200)
        #:Movie_duration > 0)
        self.Fk_ageRestriction: int = fk_age_restriction


class CastAssignment(ObjectWithCounter):
    def __init__(self, fk_artist, fk_movie, fk_role):
        self.Id_castAssignment: int = CastAssignment.counter
        CastAssignment.counter += 1
        self.Fk_artist: int = fk_artist
        self.Fk_movie: int = fk_movie
        self.Fk_role: int = fk_role


class Country(ObjectWithCounter):
    def __init__(self, country_name: str):
        self.Id_country = Country.counter
        Country.counter += 1
        self.Country_name: str = country_name


class Dimension(ObjectWithCounter):
    def __init__(self, dimension_name: str):
        self.Id_dimension: int = Dimension.counter
        Dimension.counter += 1
        self.Dimension_name: str = dimension_name


class Discount(ObjectWithCounter):
    def __init__(self, discount_name: str):
        self.Id_discount = Discount.counter
        Discount.counter += 1
        self.Discount_name: str = discount_name


class Genre(ObjectWithCounter):
    def __init__(self, genre_name: str):
        self.Id_genre: int = Genre.counter
        Genre.counter += 1
        self.Genre_name: str = genre_name


class MovieVersion(ObjectWithCounter):
    def __init__(self, fk_translation: int, fk_dimension: int):
        self.Id_movieVersion: int = MovieVersion.counter
        MovieVersion.counter += 1
        self.Fk_translation = fk_translation
        self.Fk_dimension = fk_dimension


class Movie_Country(ObjectWithCounter):
    def __init__(self, fk_movie: int, fk_country: int):
        self.Id_movie_country: int = Movie_Country.counter
        Movie_Country.counter += 1
        self.Fk_movie = fk_movie
        self.Fk_country = fk_country


class Movie_Genre(ObjectWithCounter):
    def __init__(self, fk_movie: int, fk_genre: int):
        self.Id_movie_genre: int = Movie_Genre.counter
        Movie_Genre.counter += 1
        self.Fk_movie = fk_movie
        self.Fk_genre = fk_genre


class Movie_MovieVersion(ObjectWithCounter):
    def __init__(self, fk_movie: int, fk_movieVersion: int):
        self.Id_movie_movieVersion: int = Movie_MovieVersion.counter
        Movie_MovieVersion.counter += 1
        self.Fk_movie = fk_movie
        self.Fk_movieVersion = fk_movieVersion


class Poster(ObjectWithCounter):
    def __init__(self, fk_movie: int):
        self.Id_poster: int = Poster.counter
        Poster.counter += 1
        self.Fk_movie = fk_movie
        self.Poster_path = f'C:\posters\{self.Fk_movie}\{random_string_generator(4)}.tiff'


class Price(ObjectWithCounter):
    def __init__(self, price_value: float):
        self.Id_price = Price.counter
        Price.counter += 1
        self.Price_value: float = price_value


class Privilege(ObjectWithCounter):
    def __init__(self, privilege_name: str):
        self.Id_privilege: int = Privilege.counter
        Privilege.counter += 1
        self.Privilege_name = privilege_name


class PrivilegeAssignment(ObjectWithCounter):
    def __init__(self, fk_user: int, fk_privilege: int):
        self.Id_privilegeAssignment: int = PrivilegeAssignment.counter
        PrivilegeAssignment.counter += 1
        self.Fk_user = fk_user
        self.Fk_privilege = fk_privilege


class Rating(ObjectWithCounter):
    def __init__(self, fk_movie: int, fk_user: int):
        self.Id_rating: int = Rating.counter
        Rating.counter += 1
        self.Fk_movie = fk_movie
        self.Fk_user = fk_user
        self.Rating_rate = random.randint(1, 10) # 1 <= Rating_rate <= 10)


class Seans(ObjectWithCounter):
    def __init__(self, fk_room: int, fk_movieVersion: int):
        self.Id_seans: int = Seans.counter
        Seans.counter += 1
        self.Fk_room = fk_room
        self.Fk_movieVersion = fk_movieVersion
        self.Seans_date = random_date_generator()


class Reservation(ObjectWithCounter):
    def __init__(self, fk_seans: int, fk_reservationState: int, fk_user: int):
        self.Id_reservation: int = Reservation.counter
        Reservation.counter += 1
        self.Fk_seans = fk_seans
        self.Fk_reservationState = fk_reservationState
        self.Fk_user = fk_user


class Ticket(ObjectWithCounter):
    def __init__(self, fk_seat: int, fk_reservation: int, fk_discount: int, fk_price: int):
        self.Id_ticket: int = Ticket.counter
        Ticket.counter += 1
        self.Fk_seat = fk_seat
        self.Fk_reservation = fk_reservation
        self.Fk_discount = fk_discount
        self.Fk_price = fk_price
