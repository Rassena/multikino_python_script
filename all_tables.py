from constants import *
from tables import *


class AllTables:
    def __init__(self):
        ageRestrictions = [AgeRestriction(str_val) for str_val in AGE_RESTRICTIONS]
        rooms = [Room(str_val) for str_val in ROOMS]
        roles = [Role(str_val) for str_val in ROLES]
        artists = [Artist() for i in range(ARTIST_NUM)]
        reservationStates = [ReservationState(str_val) for str_val in RESERVATION_STATES]
        translations = [Translation(str_val) for str_val in TRANSLATIONS]
        users = [User() for i in range(USER_NUM)]
        seats = [Seat(room.Id_room) for room in rooms for i in range(45)]
        countries = [Country(str_val) for str_val in COUNTRIES]
        dimensions = [Dimension(str_val) for str_val in DIMENSIONS]
        discounts = [Discount(float_val) for float_val in DISCOUNTS]
        genres = [Genre(str_val) for str_val in CATEGORIES]
        movies = [Movie(random.choice(ageRestrictions).Id_ageRestriction) for i in range(MOVIE_NUM)]
        castAssigments = [CastAssignment(artist.Id_artist, movie.Id_movie, random.choice(roles).Id_role)
                          for movie in movies
                          for artist in random.choices(artists, k=len(roles))]
        movieVersions = [MovieVersion(translation.Id_translation, dimension.Id_dimension)
                         for translation in translations
                         for dimension in dimensions]
        movie_countries = [Movie_Country(movie.Id_movie, country.Id_country)
                           for movie in movies
                           for country in random.choices(countries, k=random.randrange(1, 3))]
        movie_genres = [Movie_Genre(movie.Id_movie, genre.Id_genre)
                        for movie in movies
                        for genre in random.choices(genres, k=random.randrange(2, 5))]
        movie_movieVersions = [Movie_MovieVersion(movie.Id_movie, movieVersion.Id_movieVersion)
                               for movie in movies
                               for movieVersion in random.choices(movieVersions, k=random.randrange(1, 4))]
        posters = [Poster(movie.Id_movie) for movie in movies]
        prices = [Price(float_val) for float_val in PRICES]
        privileges = [Privilege(str_val) for str_val in PRIVILAGES]
        workers = users[:500]
        clients = users[500:]
        privilegeAssignments = [PrivilegeAssignment(user.Id_user, privilege.Id_privilege)
                                for user in workers
                                for privilege in random.choices(privileges[2:], k=random.randrange(1, 3))] + \
                               [PrivilegeAssignment(user.Id_user, random.choice(privileges[:2]).Id_privilege)
                                for user in clients]
        raitings = [Rating(movie.Id_movie, user.Id_user)
                    for user in random.choices(clients, k=len(clients) // 3)
                    for movie in random.choices(movies, k=random.randrange(1, 8))]
        seanses = [Seans(room.Id_room, movieVersion.Id_movieVersion)
                   for room in rooms
                   for movieVersion in random.choices(movieVersions, k=len(movie_movieVersions) // 3)]
        reservations = [Reservation(seans.Id_seans, random.choice(reservationStates).Id_reservationState, user.Id_user)
                        for user in clients
                        for seans in random.choices(seanses, k=random.randrange(1, 5))]
        self.all_tables = ageRestrictions + rooms + roles + artists + reservationStates + translations + users + seats + \
                          countries + dimensions + discounts + genres + movies + castAssigments + movieVersions + \
                          movie_countries + movie_genres + movie_movieVersions + posters + prices + privileges + \
                          privilegeAssignments + raitings + seanses + reservations