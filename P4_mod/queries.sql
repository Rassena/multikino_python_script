/* Query 1 (interface 16) - wszystkie seanse dzisiaj posortowane rosnąco po godzinie,
   w tabeli ma być informacja o tłumaczeniu i wymiarze seansu*/
EXPLAIN
SELECT Movie_name, Seans_time, (Seans_time <= NOW()) AS 'Has_started', Translation_name, Dimension_name
FROM seans
INNER JOIN movieversion m2 on seans.Fk_movieVersion = m2.Id_movieVersion
INNER JOIN movie ON m2.Fk_movie = movie.Id_movie
INNER JOIN dimension d on m2.Fk_dimension = d.Id_dimension
INNER JOIN translation t on m2.Fk_translation = t.Id_translation
WHERE seans.Seans_date = DATE(NOW())
ORDER BY seans.Seans_time;


/* Query 2 (interface 9, 17) - wszystkie zajęte miejsca dla danego seansu */
EXPLAIN
SELECT seans.Id_seans, m.Movie_name, s.Seat_row, s.Seat_number, rs.TicketState_name
FROM seans
INNER JOIN reservation ON seans.Id_seans = reservation.Fk_seans
INNER JOIN movieversion mmv on seans.Fk_movieVersion = mmv.Id_movieVersion
INNER JOIN movie m on mmv.Fk_movie = m.Id_movie
INNER JOIN ticket t on reservation.Id_reservation = t.Fk_reservation
INNER JOIN ticketstate rs on t.Fk_ticketState = rs.Id_ticketState
INNER JOIN seat s on t.Fk_seat = s.Id_seat
WHERE seans.Id_seans = :input_id_seans # 174, 62
AND (rs.Id_ticketState = 2 OR
     rs.Id_ticketState = 3);


/* Query 3 (interface 19) - wszystkie dzisiejsze rezerwacje na dane nazwisko */
EXPLAIN
SELECT user.User_surname, m.Movie_name, seans.Seans_time, COUNT(Id_ticket) AS 'Number_of_tickets'
FROM reservation
INNER JOIN seans ON reservation.Fk_seans = seans.Id_seans
INNER JOIN user on reservation.Fk_user = user.Id_user
INNER JOIN ticket t on reservation.Id_reservation = t.Fk_reservation
INNER JOIN ticketstate r on t.Fk_ticketState = r.Id_ticketState
INNER JOIN movieversion mmv on seans.Fk_movieVersion = mmv.Id_movieVersion
INNER JOIN movie m on mmv.Fk_movie = m.Id_movie
# INNER JOIN ticket_ticketstate tt2 on r.Id_ticketState = tt2.Fk_ticketState

WHERE seans.Seans_date = DATE(NOW())
AND user.User_surname = 'Smith' # Bisarra, Roberts
GROUP BY Id_reservation
;


/* Query 4 (interface 14) - cena do zapłaty za rezerwację */
EXPLAIN
SELECT Id_reservation, SUM(Price_value*(1- Discount_value)) AS Ticket_price
FROM reservation
INNER JOIN ticket ON reservation.Id_reservation = ticket.Fk_reservation
INNER JOIN price p on ticket.Fk_price = p.Id_price
INNER JOIN discount d on ticket.Fk_discount = d.Id_discount
INNER JOIN seat s on ticket.Fk_seat = s.Id_seat
WHERE Id_reservation = 696 # 696, 5
;

/* Query 5 (interface 1, 2, 3, 6) - najpopularniejsze filmy sortowane po największej
   ilości sprzedanych biletów, wyświetlamy tytuły dostępne tylko w danym dniu - do zrobienia */
EXPLAIN
SELECT  m.Movie_name, Seans_date, gr.count
FROM seans
INNER JOIN movieversion mmv on seans.Fk_movieVersion = mmv.Id_movieVersion
INNER JOIN movie m on mmv.Fk_movie = m.Id_movie
INNER JOIN (
     SELECT m.Id_movie, COUNT(m.Movie_name) AS count
     FROM ticket
     INNER JOIN reservation r on ticket.Fk_reservation = r.Id_reservation
     INNER JOIN seans on r.Fk_seans = seans.Id_seans
     INNER JOIN movieversion mmv on seans.Fk_movieVersion = mmv.Id_movieVersion
     INNER JOIN movie m on mmv.Fk_movie = m.Id_movie
     GROUP BY m.Id_movie
 ) gr on m.Id_movie = gr.Id_movie
WHERE Seans_date = DATE(NOW())
ORDER BY gr.count DESC;

/* Query 6 (interface 3, 4, 6) - liczenie średniej ratingu dla filmów i wyświetlenie w kolejności od najlepszego */
EXPLAIN
SELECT m.Movie_name, AVG(Rating_rate) AS 'Rate'
FROM rating
INNER JOIN movie m on rating.Fk_movie = m.Id_movie
GROUP BY Movie_name
HAVING Rate > 7
ORDER BY Rate DESC;

# ??
/* Query 7 (interface 19) - czy można odebrać rezerwację (jeśli miejsca nie są wykupione to można) - do zrobienia */
EXPLAIN
SELECT reservation.Id_reservation, Id_seat, (r.Id_ticketState != 3) AS 'Is_buyable'
FROM reservation
INNER JOIN seans ON reservation.Fk_seans = seans.Id_seans
INNER JOIN user on reservation.Fk_user = user.Id_user
INNER JOIN ticket t on reservation.Id_reservation = t.Fk_reservation
INNER JOIN ticketstate r on t.Fk_ticketState = r.Id_ticketState
INNER JOIN movieversion mmv on seans.Fk_movieVersion = mmv.Id_movieVersion
INNER JOIN movie m on mmv.Fk_movie = m.Id_movie
INNER JOIN seat s on t.Fk_seat = s.Id_seat
WHERE reservation.Id_reservation = :input_id_reservation; #696, 50, 127

/* Query 8 (interface 16) - lista obecnie trwających seansów (mamy datę rozpoczęcia i czas trwania filmu)*/
EXPLAIN
SELECT m.Movie_name, Seans_time, (Seans_time <= TIME(NOW())) AS 'Rozpoczal sie', t.Translation_name, d.Dimension_name
FROM seans
INNER JOIN movieversion mmv on seans.Fk_movieVersion = mmv.Id_movieVersion
INNER JOIN translation t on mmv.Fk_translation = t.Id_translation
INNER JOIN dimension d on mmv.Fk_dimension = d.Id_dimension
INNER JOIN movie m on mmv.Fk_movie = m.Id_movie
WHERE Seans_date = DATE(NOW())
ORDER BY Seans_time, m.Movie_name;

/* Query 9 (interface ) - lista gatunków dla danego tytułu - do zrobienia */
EXPLAIN
SELECT Genre_name
FROM movie_genre
INNER JOIN genre g on movie_genre.Fk_genre = g.Id_genre
INNER JOIN movie m on movie_genre.Fk_movie = m.Id_movie
WHERE Id_movie = :input_id_movie; #46, 120

/* Query 10 (interface 5) - lista filmów w którym dany twórca brał udział,
   w tabeli informacja o roli (reżyser/aktor/scenarzysta)*/
EXPLAIN
SELECT movie.Movie_name, r.Role_name
FROM movie
INNER JOIN castassignment c on movie.Id_movie = c.Fk_movie
INNER JOIN artist a on c.Fk_artist = a.Id_artist
INNER JOIN role r on c.Fk_role = r.Id_role
WHERE a.Id_artist = :input_id_artist # 4, 6, 10
ORDER BY r.Role_name, Movie_name;

# FIXME: poprawka ze względu na reservationState -> ticketState
/* Query 11 (interface 8) - Wszystkie bieżące rezerwacje dla danego konta - do zrobienia */
# EXPLAIN
# SELECT Seans_date, Seans_time, m.Movie_name
# FROM seans
# INNER JOIN movie_movieversion mmv on seans.Fk_movie_MovieVersion = mmv.Id_movie_movieVersion
# INNER JOIN movie m on mmv.Fk_movie = m.Id_movie
# INNER JOIN reservation r on seans.Id_seans = r.Fk_seans
# INNER JOIN reservationstate r2 on r.Fk_reservationState = r2.Id_reservationState
# INNER JOIN user u on r.Fk_user = u.Id_user
# WHERE (Seans_date > DATE(NOW()) OR (Seans_date = DATE(NOW()) AND Seans_time > TIME(NOW())))
# AND (r2.Id_reservationState = 2 OR r2.Id_reservationState = 3)
# AND u.Id_user = :input_id_user # 572, 663, 610
# ;

/* Query 12 (interface 4) - Wyświetlanie repertuaru w wybrany dzień dla danego filmu */
EXPLAIN
SELECT Seans_time, d.Dimension_name, t.Translation_name
FROM seans
INNER JOIN movieversion mv on seans.Fk_movieVersion = mv.Id_movieVersion
    INNER JOIN dimension d on mv.Fk_dimension = d.Id_dimension
INNER JOIN movie m on mv.Fk_movie = m.Id_movie
INNER JOIN translation t on mv.Fk_translation = t.Id_translation
WHERE
       m.Movie_name = 'Movie name AGO0x'
  AND
      Seans_date = DATE('2021-11-19')
;

/* Query 13 - wydlad sali do pokazania wolnych i zajętych miejsc */
EXPLAIN
SELECT *
FROM seat
join room r on seat.Fk_room = r.Id_room
join seans s on r.Id_room = s.Fk_room
WHERE Id_seans = 69
;

/* Query 14 - stan obecy rezerwacji */
SELECT t.Fk_seat, t2.TicketState_name
FROM reservation
JOIN ticket t on reservation.Id_reservation = t.Fk_reservation
JOIN ticketstate t2 on t2.Id_ticketState = t.Fk_ticketState
WHERE reservation.Id_reservation = 4
;


# EXPLAIN
# SELECT *
# FROM ticket
#     inner join reservation r on ticket.Fk_reservation = r.Id_reservation
#     inner join seans s2 on r.Fk_seans = s2.Id_seans
# right JOIN seat s on ticket.Fk_seat = s.Id_seat
# WHERE
# #       ticket.Id_ticket is null and
#       Id_seans = 69
# ;

/* Query 15 - historia stanów biletów uzytkownika dla danego filmu */

SELECT tt.Fk_ticket, tt.Ticket_ticketState_date, t2.TicketState_name, m2.Movie_name
FROM ticket_ticketstate as tt
INNER JOIN ticket t on tt.Fk_ticket = t.Id_ticket
INNER JOIN reservation r on t.Fk_reservation = r.Id_reservation
INNER JOIN seans s on r.Fk_seans = s.Id_seans
INNER JOIN movieversion m on s.Fk_movieVersion = m.Id_movieVersion
INNER JOIN movie m2 on m.Fk_movie = m2.Id_movie
INNER JOIN user u on r.Fk_user = u.Id_user
INNER JOIN ticketstate t2 on t.Fk_ticketState = t2.Id_ticketState
WHERE Id_user = 24352 and m2.Movie_name = 'Movie name 3Z7Zi'
ORDER BY tt.Ticket_ticketState_date;