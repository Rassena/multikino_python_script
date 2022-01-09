select * from users where user_privilege contains 'Pracownik' and user_privilege contains 'Klient' ALLOW FILTERING;


/* Query1  wszystkie seanse dzisiaj */
SELECT movie_title, dimension_name, movie_translation, showing_date, showing_time FROM tickets WHERE showing_date='2016-03-15';

/* Query2 wszystkie zajęte miejsca dla danego seansu */
SELECT room_row, room_seat FROM tickets WHERE showing_id=4 ALLOW FILTERING ;

/* Query3 wszystkie dzisiejsze bilety na dane nazwisko */
SELECT movie_title, dimension_name, movie_translation, showing_date, showing_time FROM tickets WHERE user_surname='Nowak' AND showing_date='2016-03-16' ALLOW FILTERING;


/* Query4 cena do zapłaty za rezerwację */
SELECT sum(ticket_price) AS Do_Zaplaty FROM tickets WHERE ticket_reservation=5 ALLOW FILTERING;

/* Query5 Przyszłe seanse danego filmu */
SELECT showing_date AS date, showing_time AS time, movie_title AS title, room_name AS room, dimension_name AS dimension, movie_translation AS translation, dimension_baseprice AS base_price FROM showings WHERE showing_date>='2016-03-16' AND Movie_title= 'West side story' ALLOW FILTERING ;

/* Query6 liczenie średniej ratingu dla filmów */
 SELECT Movie_name, avg(cast(Rating_value AS double)) AS Rating FROM ratings group by movie_id;

/* Query7 lista gatunków dla danego tytułu */
SELECT genre_name, movie_name FROM genres WHERE movie_name='West side story' ALLOW FILTERING;

/* Query8 lista filmów w którym dany twórca brał udział */
SELECT movie_name, artist_name, artist_surname, role_name FROM castings WHERE artist_id=0 ALLOW FILTERING;

/* Query9 historia stanów biletów użytkownika dla danego filmu (dla przyszłych seansów) */
SELECT * FROM ticketstates WHERE User_id =1 ALLOW FILTERING;

SELECT * FROM ticketstates WHERE user_id=3 AND showing_date >= '2016-03-15' ALLOW FILTERING;

/* Query10 Wyświetlanie repertuaru w wybrany dzień dla danego filmu */
SELECT showing_date, showing_time, dimension_name, movie_title FROM showings WHERE showing_date='2016-03-16' ALLOW FILTERING;

/*----------------------------------------------------------------------------------*/
select * from artists where artist_birth='2013-03-15' allow filtering;

select Artist_name, Artist_surname, Role_name from castings where movie_id=0 allow filtering;
select movie_name, Role_name from castings where artist_id=0 allow filtering;

select * from movies where Tags_translation_dimension contains ('lektor','2D') allow filtering;
select movie_name as title from movies;

select Genre_name from genres where Movie_id=1;
/* select Movie_name, Genre_name from genres group by Movie_id; */

select Room_set_row_seatNr from rooms where Room_name='room1' allow filtering;

Select showing_time as time,movie_title as title, room_name as room, dimension_name as dimension, movie_translation as translation, dimension_baseprice as base_price, room_set_row_seatnr as seats from showings;

Select showing_time as time,movie_title as title, room_name as room, dimension_name as dimension, movie_translation as translation, dimension_baseprice as base_price, room_set_row_seatnr as seats from showings where showing_date='2016-03-16' allow filtering;

Select showing_time as time,movie_title as title, room_name as room, dimension_name as dimension, movie_translation as translation, dimension_baseprice as base_price, room_set_row_seatnr as seats from showings where showing_date='2016-03-16' and Movie_title= 'West side story' allow filtering;

Select * from showings where showing_date='2016-03-16' and Showing_time>'15:30:00' allow filtering;

Select user_surname as user, movie_title as title,Showing_date as date,showing_time as time, room_name as room, room_row as row, room_seat as seat, dimension_name as dimension, movie_translation as translation, ticket_price as price, discount_name as discount, Ticket_state as state, ticket_reservation as reservation from tickets;

select * from tickets where showing_date='2016-03-15' group by ticket_reservation allow filtering;

select * from ticketstates where ticket_id=19 limit 1 allow filtering;
