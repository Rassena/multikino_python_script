import names
from constants import *

from supporting_methods import *


class AgeRestriction(ObjectWithCounter, AddableToDatabase):
    def __init__(self, age_restriction_name: str):
        self.Id_ageRestriction: int = AgeRestriction.next()
        self.AgeRestriction_name: str = age_restriction_name


class Room(ObjectWithCounter, AddableToDatabase):
    def __init__(self, room_sign: str):
        self.Id_room: int = Room.next()
        self.Room_sign: str = room_sign


class ReservationState(ObjectWithCounter, AddableToDatabase):
    def __init__(self, reservation_state_name: str):
        self.Id_reservationState: int = ReservationState.next()
        self.ReservationState_name: str = reservation_state_name


class Role(ObjectWithCounter, AddableToDatabase):
    def __init__(self, role_name: str):
        self.Id_role: int = Role.next()
        self.Role_name: str = role_name


class Translation(ObjectWithCounter, AddableToDatabase):
    def __init__(self, translation_name: str):
        self.Id_translation: int = Translation.next()
        self.Translation_name = translation_name


class Artist(ObjectWithCounter, AddableToDatabase):
    genders = {False: 'male', True: 'female'}

    def __init__(self):
        self.Id_artist: int = Artist.next()
        gender_id = random.choice([False, True])
        self.Artist_name: str = names.get_first_name(gender=self.genders[gender_id])
        self.Artist_surname: str = names.get_last_name()
        self.Artist_birth: date = random_date_generator(1960, 2000)
        self.Artist_gender: bool = gender_id


class User(ObjectWithCounter, AddableToDatabase):
    genders = {False: 'male', True: 'female'}

    def __init__(self):
        self.Id_user: int = User.next()
        gender_id = random.choice([False, True])
        self.User_name: str = names.get_first_name(gender=self.genders[gender_id])
        self.User_surname: str = names.get_last_name()
        self.User_email: str = f'{random_string_generator(random.randrange(6, 12))}@gmail.com'
        self.User_password: str = random_string_generator(random.randrange(8, 12))
        self.User_birth: date = random_date_generator(1970, 2003)


class Seat(ObjectWithCounter, AddableToDatabase):
    MAX_SEAT_IN_ROW = 15
    rooms_seats = {}

    def __init__(self, fk_room: int):
        self.Id_seat: int = Seat.next()

        if fk_room not in Seat.rooms_seats.keys():
            Seat.rooms_seats[fk_room] = 0
        else:
            Seat.rooms_seats[fk_room] += 1

        self.Seat_row: str = Seat.rooms_seats[fk_room] // Seat.MAX_SEAT_IN_ROW + 1
        self.Seat_number: int = Seat.rooms_seats[fk_room] % Seat.MAX_SEAT_IN_ROW + 1
        # Seat_number > 0)
        self.Fk_room: int = fk_room


class Movie(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_age_restriction: int):
        self.Id_movie: int = Movie.next()

        self.Movie_name: str = f'Movie name {random_string_generator(5)}'
        self.Movie_description: str = random_string_generator(100)
        self.Movie_premiere: date = random_date_generator(2000, 2022)
        self.Movie_duration: int = random.randrange(90, 200) #:Movie_duration > 0)
        self.Fk_ageRestriction: int = fk_age_restriction


class CastAssignment(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_artist, fk_movie, fk_role):
        self.Id_castAssignment: int = CastAssignment.next()
        self.Fk_artist: int = fk_artist
        self.Fk_movie: int = fk_movie
        self.Fk_role: int = fk_role


class Country(ObjectWithCounter, AddableToDatabase):
    def __init__(self, country_name: str):
        self.Id_country = Country.next()
        self.Country_name: str = country_name


class Dimension(ObjectWithCounter, AddableToDatabase):
    def __init__(self, dimension_name: str):
        self.Id_dimension: int = Dimension.next()
        self.Dimension_name: str = dimension_name


class Discount(ObjectWithCounter, AddableToDatabase):
    def __init__(self, discount_name: str):
        self.Id_discount = Discount.next()
        self.Discount_name: str = discount_name


class Genre(ObjectWithCounter, AddableToDatabase):
    def __init__(self, genre_name: str):
        self.Id_genre: int = Genre.next()
        self.Genre_name: str = genre_name


class MovieVersion(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_translation: int, fk_dimension: int):
        self.Id_movieVersion: int = MovieVersion.next()
        self.Fk_translation = fk_translation
        self.Fk_dimension = fk_dimension


class Movie_Country(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_movie: int, fk_country: int):
        self.Id_movie_country: int = Movie_Country.next()
        self.Fk_movie = fk_movie
        self.Fk_country = fk_country


class Movie_Genre(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_movie: int, fk_genre: int):
        self.Id_movie_genre: int = Movie_Genre.next()
        self.Fk_movie = fk_movie
        self.Fk_genre = fk_genre


class Movie_MovieVersion(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_movie: int, fk_movieVersion: int):
        self.Id_movie_movieVersion: int = Movie_MovieVersion.next()
        self.Fk_movie = fk_movie
        self.Fk_movieVersion = fk_movieVersion


class Poster(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_movie: int):
        self.Id_poster: int = Poster.next()
        self.Fk_movie = fk_movie
        self.Poster_path = f'C:\\posters\\{self.Fk_movie}\\{random_string_generator(4)}.tiff'


class Price(ObjectWithCounter, AddableToDatabase):
    def __init__(self, price_value: float):
        self.Id_price = Price.next()
        self.Price_value: float = price_value


class Privilege(ObjectWithCounter, AddableToDatabase):
    def __init__(self, privilege_name: str):
        self.Id_privilege: int = Privilege.next()
        self.Privilege_name = privilege_name


class PrivilegeAssignment(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_user: int, fk_privilege: int):
        self.Id_privilegeAssignment: int = PrivilegeAssignment.next()
        self.Fk_user = fk_user
        self.Fk_privilege = fk_privilege


class Rating(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_movie: int, fk_user: int):
        self.Id_rating: int = Rating.next()
        self.Fk_movie = fk_movie
        self.Fk_user = fk_user
        self.Rating_rate = random.randint(1, 10) # 1 <= Rating_rate <= 10)


class Seans(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_room: int, fk_movieVersion: int):
        self.Id_seans: int = Seans.next()
        self.Fk_room = fk_room
        self.Fk_movieVersion = fk_movieVersion
        self.Seans_date = random_date_generator(2021, 2022)
        self.Seans_time = random_time_generator()


class Reservation(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_seans: int, fk_reservationState: int, fk_user: int):
        self.Id_reservation: int = Reservation.next()
        self.Fk_seans = fk_seans
        self.Fk_reservationState = fk_reservationState
        self.Fk_user = fk_user


class Ticket(ObjectWithCounter, AddableToDatabase):
    def __init__(self, fk_seat: int, fk_reservation: int, fk_discount: int, fk_price: int):
        self.Id_ticket: int = Ticket.next()
        self.Fk_seat = fk_seat
        self.Fk_reservation = fk_reservation
        self.Fk_discount = fk_discount
        self.Fk_price = fk_price
