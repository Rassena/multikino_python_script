import random

from f1_tables_as_classes import *

NUMBER_OF_ALL_ENTITIES_noSQL = 13


def print_created(class_):
    print(f'\033[96m{class_.__name__}\033[0m was created')


class AllMultikinoEntities:
    def __init__(self):
        tab_with_all_tabs: list[list[AddableToDatabase]] = [[] for i in range(NUMBER_OF_ALL_ENTITIES_noSQL)]
        users_inx, artists_inx, dimensions_inx, movies_inx, \
        castings_inx, ratings_inx, genres_inx, rooms_inx, \
        discounts_inx, showings_inx, tickets_inx, ticketstates_inx, reservations_inx \
            = range(NUMBER_OF_ALL_ENTITIES_noSQL)


        tab_with_all_tabs[artists_inx] = [Artists() for i in range(ARTIST_NUM)]
        print_created(Artists)
        tab_with_all_tabs[users_inx] = [Users() for i in range(USER_NUM)]
        print_created(Users)
        tab_with_all_tabs[rooms_inx] = [Rooms(sign) for sign in ROOMS]
        print_created(Rooms)
        tab_with_all_tabs[dimensions_inx]: Dimensions = [Dimensions(DIMENSIONS[i], PRICES[i]) for i in range(len(DIMENSIONS))]
        print_created(Dimensions)
        tuples_trans_dim_price: set[tuple[str, str, float]] = set([
            (translation, dimension.dimension_name, dimension.dimension_basePrice)
            for dimension in tab_with_all_tabs[dimensions_inx] for translation in TRANSLATIONS
        ])
        titles = []
        with open('movie_titles.txt', 'r', encoding='utf-8') as f:
            for title in f.readlines():
                titles.append(title.replace('\n', ''))
        tab_with_all_tabs[movies_inx] = [Movies(title, tuples_trans_dim_price) for title in titles]
        print_created(Movies)
        tab_with_all_tabs[castings_inx] = [Castings(random.choice(tab_with_all_tabs[artists_inx]), movie)
                                           for movie in tab_with_all_tabs[movies_inx]
                                           for i in range(random.randrange(7))]
        print_created(Castings)
        tab_with_all_tabs[ratings_inx] = [Ratings(random.choice(tab_with_all_tabs[movies_inx]), user)
                                          for user in tab_with_all_tabs[users_inx]
                                          for i in range(random.randrange(5))]
        print_created(Ratings)
        tab_with_all_tabs[genres_inx] = [Genres(movie, random.choice(CATEGORIES))
                                         for movie in tab_with_all_tabs[movies_inx]
                                         for i in range(random.randrange(4))]
        print_created(Genres)
        tab_with_all_tabs[discounts_inx] = [Discounts(discount[0], discount[1], dimension)
                                            for discount in DISCOUNTS
                                            for dimension in tab_with_all_tabs[dimensions_inx]]
        print_created(Discounts)
        tab_with_all_tabs[showings_inx] = [Showings(movie, random.choice(tab_with_all_tabs[rooms_inx]),
                                                    tab_with_all_tabs[discounts_inx])
                                           for movie in tab_with_all_tabs[movies_inx]
                                           for _ in range(random.randrange(5, 15))]
        print_created(Showings)

        for showing in tab_with_all_tabs[showings_inx]:
            for user in random.choices(tab_with_all_tabs[users_inx], k=random.randrange(0, 15)):
                reservation = Reservations(showing, user)
                ticket_list: list = []
                for row_seat in random.choices(tuple(showing.room_set_row_seatNr), k=random.randrange(1, 5)):
                    ticket_list += [Tickets(reservation, row_seat[0], row_seat[1])]
                reservation.update_tickets(ticket_list)
                tab_with_all_tabs[reservations_inx] += [reservation]
                tab_with_all_tabs[tickets_inx] += ticket_list

        print_created(Reservations)
        print_created(Tickets)

        tab_with_all_tabs[ticketstates_inx] = [TicketStates(ticket, ticketState_name)
                                                for ticket in tab_with_all_tabs[tickets_inx]
                                               for ticketState_name in random.sample(TICKET_STATES, random.randrange(1, 4))]
        print_created(TicketStates)


        self.all_entities: list[AddableToDatabase] = []
        self.tab_with_all_tabs = tab_with_all_tabs
        for x in tab_with_all_tabs:
            self.all_entities += x
