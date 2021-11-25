CREATE INDEX Seans_date_idx
ON seans(Seans_date)
;

CREATE INDEX Movie_movieversion__movie_idx
ON movie_movieversion(Fk_movie)
;

CREATE INDEX Seat_room_idx
ON seat(Fk_room)
;

CREATE INDEX Movie_genre__movie_idx
ON movie_genre(Fk_movie)
;

CREATE INDEX Castassignment_artist_idx
ON castassignment(Fk_artist)
;
# ------------------------------------------------------------------------------------------

# /*
# +/- Wprowadzanie tak częste jak wrowadzanie nowych filmow
#  +  bardzo czeste przeszukiwania
#  */
# CREATE INDEX Movieversion__translation_dimension_idx
# ON movieversion(Fk_translation, Fk_dimension)

/*
+ czeste sortowanie po czasie seansu (Top 10.5)
+ czeste porownywanie czasow (szczegolnie <= TIME(NOW())) (Top 10.1)
- dodawanie seansow do bazy danych odbywa sie codziennie (Top 10.10)
*/
CREATE INDEX Seans_time_idx
ON seans(Seans_time)
;

/*
+ czeste wyszukiwana rezerwacji po nazwisku (Top 10.1)
- dodawanie uzytkownikow do bazy danych odbywa sie codziennie, lecz bez regularnosci (Top 10.10)
*/
CREATE INDEX User_surname_inx
ON user(User_surname)
;

/*
+ czeste porownywania stanow rezerwacji
+ brak modyfikacji (Top 10.10)
- malo elementow
*/
CREATE INDEX Ticketstate_id_inx
ON ticketstate(Id_ticketState)
;

/*
+ czeste filtrowanie po gatunkach
+ praktycznie brak modyfikacji (Top 10.10)
+ stosunkowo duzo elementow
*/
CREATE INDEX Genre_id_inx
ON genre(Genre_name)
;

/*
 - Rzadkie wyszukiwanie po nazwie, ale się pojawia
 + Praktycznie brak modyfikacji
 */
CREATE INDEX Country_id_inx
ON country(Country_name)
;

/*
 - Czeste wprowadzanie nowych danych
 + czeste przeszukiwania
 */
CREATE INDEX Reservation_id_inx
ON reservation(Fk_seans)
;

/*
 + Częste sortowanie filmów po rating
 + Rzadkie modyfikacje/dodawanie nowych filmów do repertuaru
 +/- nie za częste dodawanie nowej oceny do filmu
 */
# CREATE  INDEX rating_id_inx
# ON rating(Id_rating)
# ;