from initializing_database.f2_3_tables_as_classes import *


class AllMultikinoEntities:
    def __init__(self):
        tab_with_all_tabs = [[] for i in range(NUMBER_OF_ALL_ENTITIES)]
        ageRestrictions_inx, rooms_inx, reservationStates_inx, roles_inx, translations_inx, \
        artists_inx, users_inx, seats_inx, movies_inx, castAssigments_inx, countries_inx, \
        dimensions_inx, discounts_inx, genres_inx, movieVersions_inx, movie_countries_inx, \
        movie_genres_inx, movie_movieVersions_inx, posters_inx, prices_inx, privileges_inx, \
        privilegeAssignments_inx, raitings_inx, seanses_inx, reservations_inx, tickets_inx \
            = range(NUMBER_OF_ALL_ENTITIES)

        # Entities with no attributes_____________________________________________________________________
        tab_with_all_tabs[artists_inx] = [Artist() for i in range(ARTIST_NUM)]
        tab_with_all_tabs[users_inx] = [User() for i in range(USER_NUM)]

        artists: list[Artist] = tab_with_all_tabs[artists_inx]
        users: list[User] = tab_with_all_tabs[users_inx]

        workers = users[:WORKERS_NUM]
        clients = users[WORKERS_NUM:]

        # Entities with no fks____________________________________________________________________________
        tab_with_all_tabs[ageRestrictions_inx] = [AgeRestriction(str_val) for str_val in AGE_RESTRICTIONS]
        tab_with_all_tabs[rooms_inx] = [Room(str_val) for str_val in ROOMS]
        tab_with_all_tabs[roles_inx] = [Role(str_val) for str_val in ROLES]
        tab_with_all_tabs[reservationStates_inx] = [ReservationState(str_val) for str_val in RESERVATION_STATES]
        tab_with_all_tabs[translations_inx] = [Translation(str_val) for str_val in TRANSLATIONS]
        tab_with_all_tabs[dimensions_inx] = [Dimension(str_val) for str_val in DIMENSIONS]
        tab_with_all_tabs[genres_inx] = [Genre(str_val) for str_val in CATEGORIES]
        tab_with_all_tabs[countries_inx] = [Country(str_val) for str_val in COUNTRIES]
        tab_with_all_tabs[privileges_inx] = [Privilege(str_val) for str_val in PRIVILAGES]
        tab_with_all_tabs[discounts_inx] = [Discount(discount_name, float_val) for discount_name, float_val in DISCOUNTS]

        ageRestrictions: list[AgeRestriction] = tab_with_all_tabs[ageRestrictions_inx]
        rooms: list[Room] = tab_with_all_tabs[rooms_inx]
        roles: list[Role] = tab_with_all_tabs[roles_inx]
        reservationStates: list[ReservationState] = tab_with_all_tabs[reservationStates_inx]
        translations: list[Translation] = tab_with_all_tabs[translations_inx]
        dimensions: list[Dimension] = tab_with_all_tabs[dimensions_inx]
        genres: list[Genre] = tab_with_all_tabs[genres_inx]
        countries: list[Country] = tab_with_all_tabs[countries_inx]
        privileges: list[Privilege] = tab_with_all_tabs[privileges_inx]
        discounts: list[Discount] = tab_with_all_tabs[discounts_inx]

        # Entities with one fk________________________________________________________________________________
        tab_with_all_tabs[prices_inx] = [Price(PRICES[i], dimensions[i].Id_dimension) for i in range(len(dimensions))]
        tab_with_all_tabs[movies_inx] = [Movie(random.choice(ageRestrictions).Id_ageRestriction)
                                         for i in range(MOVIE_NUM)]
        tab_with_all_tabs[seats_inx] = [Seat(room.Id_room) for room in rooms for i in range(15*15)]

        prices: list[Price] = tab_with_all_tabs[prices_inx]
        movies: list[Movie] = tab_with_all_tabs[movies_inx]
        seats: list[Seat] = tab_with_all_tabs[seats_inx]
        tab_with_all_tabs[posters_inx] = [Poster(movie.Id_movie) for movie in movies]

        # Entities with two fks_______________________________________________________________________________
        tab_with_all_tabs[movie_countries_inx] = [Movie_Country(movie.Id_movie, country.Id_country)
                                                  for movie in movies
                                                  for country in random.choices(countries, k=random.randrange(1, 3))]
        tab_with_all_tabs[movie_genres_inx] = [Movie_Genre(movie.Id_movie, genre.Id_genre)
                                               for movie in movies
                                               for genre in random.choices(genres, k=random.randrange(2, 5))]
        tab_with_all_tabs[privilegeAssignments_inx] = [PrivilegeAssignment(user.Id_user, privilege.Id_privilege)
                                                       for user in workers
                                                       for privilege in random.choices(privileges[2:], k=random.randrange(1, 3))] + \
                                                      [PrivilegeAssignment(user.Id_user, random.choice(privileges[:2]).Id_privilege)
                                                       for user in clients]
        tab_with_all_tabs[raitings_inx] = [Rating(movie.Id_movie, user.Id_user)
                                           for user in random.choices(clients, k=len(clients) // 3)
                                           for movie in random.choices(movies, k=random.randrange(1, 8))]

        tab_with_all_tabs[movieVersions_inx] = [MovieVersion(translation.Id_translation, dimension.Id_dimension)
                                                for translation in translations
                                                for dimension in dimensions]
        movieVersions: list[MovieVersion] = tab_with_all_tabs[movieVersions_inx]

        tab_with_all_tabs[movie_movieVersions_inx] = [Movie_MovieVersion(movie.Id_movie, movieVersion.Id_movieVersion)
                                                      for movie in movies
                                                      for movieVersion in random.choices(movieVersions, k=random.randrange(1, 4))]
        movie_movieVersions: list[Movie_MovieVersion] = tab_with_all_tabs[movie_movieVersions_inx]

        tab_with_all_tabs[seanses_inx] = [Seans(room.Id_room, movieVersion.Id_movie_movieVersion)
                                          for room in rooms
                                          for movieVersion in random.choices(movie_movieVersions, k=len(movie_movieVersions) // 3)]
        seanses: list[Seans] = tab_with_all_tabs[seanses_inx]

        # Entities with three+ fks______________________________________________________________________________
        tab_with_all_tabs[castAssigments_inx] = [CastAssignment(artist.Id_artist, movie.Id_movie, random.choice(roles).Id_role)
                                                 for movie in movies
                                                 for artist in random.choices(artists, k=len(roles))]

        tab_with_all_tabs[reservations_inx] = [Reservation(seans.Id_seans, random.choice(reservationStates).Id_reservationState, user.Id_user)
                                               for user in clients
                                               for seans in random.choices(seanses, k=random.randrange(1, 5))]
        reservations: list[Reservation] = tab_with_all_tabs[reservations_inx]

        def price_for_reservation(r: Reservation) -> Price:
            s = [e for e in seanses if e.Id_seans == r.Fk_seans][0]
            mmv = [e for e in movie_movieVersions if e.Id_movie_movieVersion == s.Fk_movie_movieVersion][0]
            mv = [e for e in movieVersions if e.Id_movieVersion == mmv.Fk_movieVersion][0]
            d = [e for e in dimensions if e.Id_dimension == mv.Fk_dimension][0]
            p = [e for e in prices if e.Fk_dimension == d.Id_dimension][0]
            return p

        tab_with_all_tabs[tickets_inx] = [Ticket(seat.Id_seat, reservation.Id_reservation,
                                                 random.choice(discounts).Id_discount, price_for_reservation(reservation).Id_price)
                                          for reservation in reservations
                                          for seat in random.choices(seats, k=random.randrange(1, 5))]
        self.all_entities = []
        self.tab_with_all_tabs = tab_with_all_tabs
        for x in tab_with_all_tabs:
            self.all_entities += x
