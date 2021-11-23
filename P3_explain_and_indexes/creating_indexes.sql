/*
+ częste wyszukiwanie seansow po dacie (szczegolnie = DATE(NOW())) (Top 10.1)
- dodawanie seansow do bazy danych odbywa sie codziennie (Top 10.10)
*/
CREATE INDEX seans_date_idx
ON seans(Seans_date)
;

/*
+ czeste sortowanie po czasie seansu (Top 10.5)
+ czeste porownywanie czasow (szczegolnie <= TIME(NOW())) (Top 10.1)
- dodawanie seansow do bazy danych odbywa sie codziennie (Top 10.10)
*/
CREATE INDEX seans_time_idx
ON seans(Seans_time)
;

/*
+ czeste wyszukiwana rezerwacji po nazwisku (Top 10.1)
- dodawanie uzytkownikow do bazy danych odbywa sie codziennie, lecz bez regularnosci (Top 10.10)
*/
CREATE INDEX user_surname_inx
ON user(User_surname)
;

/*
+ czeste porownywania stanow rezerwacji
+ brak modyfikacji (Top 10.10)
- malo elementow
*/
CREATE INDEX reservationstate_id_inx
ON ticketstate(Id_ticketState)
;

/*
+ czeste filtrowanie po gatunkach
+ praktycznie brak modyfikacji (Top 10.10)
+ stosunkowo duzo elementow
*/
CREATE INDEX genre_id_inx
ON genre(Id_genre)
;