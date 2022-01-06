import random

from f1_tables_as_classes import *

NUMBER_OF_ALL_ENTITIES_noSQL = 12


class AllMultikinoEntities:
    def __init__(self):
        tab_with_all_tabs: list[list[AddableToDatabase]] = [[] for i in range(NUMBER_OF_ALL_ENTITIES_noSQL)]
        users_inx, artists_inx, dimensions_inx, movies_inx, \
        castings_inx, ratings_inx, genres_inx, rooms_inx, \
        discounts_inx, showings_inx, tickets_inx, ticketstates_inx \
            = range(NUMBER_OF_ALL_ENTITIES_noSQL)

        tab_with_all_tabs[artists_inx] = [Artists() for i in range(10)]
        tab_with_all_tabs[users_inx] = [Users() for i in range(1)]
        tab_with_all_tabs[rooms_inx] = [Rooms(sign) for sign in ROOMS]
        tab_with_all_tabs[dimensions_inx]: Dimensions = [Dimensions(DIMENSIONS[i], PRICES[i]) for i in range(len(DIMENSIONS))]

        tuples_trans_dim_price: set[tuple[str, str, float]] = set([
            (translation, dimension.dimension_name, dimension.dimension_basePrice)
            for dimension in tab_with_all_tabs[dimensions_inx] for translation in TRANSLATIONS
        ])
        tab_with_all_tabs[movies_inx] = [Movies(tuples_trans_dim_price) for i in range(10)]
        tab_with_all_tabs[castings_inx] = [Castings(random.choice(tab_with_all_tabs[artists_inx]), movie)
                                           for movie in tab_with_all_tabs[movies_inx]
                                           for i in range(random.randrange(7))]
        tab_with_all_tabs[ratings_inx] = [Ratings(random.choice(tab_with_all_tabs[movies_inx]), user)
                                          for user in tab_with_all_tabs[users_inx]
                                          for i in range(random.randrange(5))]
        tab_with_all_tabs[genres_inx] = [Genres(movie, random.choice(CATEGORIES))
                                         for movie in tab_with_all_tabs[movies_inx]
                                         for i in range(random.randrange(4))]
        tab_with_all_tabs[discounts_inx] = [Discounts(discount[0], discount[1], dimension)
                                            for discount in DISCOUNTS
                                            for dimension in tab_with_all_tabs[dimensions_inx]]
        tab_with_all_tabs[showings_inx] = [Showings(movie, random.choice(tab_with_all_tabs[rooms_inx]),
                                                    tab_with_all_tabs[discounts_inx])
                                           for movie in tab_with_all_tabs[movies_inx]]
        # tab_with_all_tabs[ticketstates_inx] = [Tickets()]

        self.all_entities: list[AddableToDatabase] = []
        self.tab_with_all_tabs = tab_with_all_tabs
        for x in tab_with_all_tabs:
            if len(x) > 0:
                print(x[0].sql_addable)
            self.all_entities += x
