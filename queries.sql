/* Query 1 - all seanses for today */
SELECT Id_movie, Movie_name, Movie_duration, seans.*
FROM seans
INNER JOIN movie_movieversion
ON seans.Fk_movieVersion = movie_movieversion.Fk_movieVersion
INNER JOIN movie
ON movie_movieversion.Fk_movie = movie.Id_movie
WHERE seans.Seans_date = DATE(NOW())
ORDER BY seans.Seans_time;

/* Query 2 - all reserved seats for a certain showing */
SELECT *
FROM seans
INNER JOIN reservation
ON seans.Id_seans = reservation.Fk_seans
WHERE seans.Id_seans = 366
AND (reservation.Fk_reservationState = 2 OR
     reservation.Fk_reservationState = 3);

/* Query 3 - get reservations for today */
SELECT user.User_surname, reservation.Fk_seans, seans.Seans_time, ReservationState_name, COUNT(Id_ticket)
FROM reservation
INNER JOIN seans
ON reservation.Fk_seans = seans.Id_seans
INNER JOIN user on reservation.Fk_user = user.Id_user
INNER JOIN reservationstate r on reservation.Fk_reservationState = r.Id_reservationState
INNER JOIN ticket t on reservation.Id_reservation = t.Fk_reservation
WHERE seans.Seans_date = DATE(NOW())
GROUP BY Id_reservation;

/* Query 4 - get reservations by user name for today */
SELECT user.User_surname, user.User_name, reservation.*, seans.Seans_date
FROM user
INNER JOIN reservation
ON user.Id_user = reservation.Fk_user
INNER JOIN seans
ON reservation.Fk_seans = seans.Id_seans
WHERE seans.Seans_date = DATE(NOW()) AND
      user.User_surname = 'Yates';

/* Query 5 - display seats for reservation with id */
SELECT Id_reservation, Seat_row, Seat_number, Price_value, Discount_name
FROM reservation
INNER JOIN ticket
ON reservation.Id_reservation = ticket.Fk_reservation
INNER JOIN price p on ticket.Fk_price = p.Id_price
INNER JOIN discount d on ticket.Fk_discount = d.Id_discount
INNER JOIN seat s on ticket.Fk_seat = s.Id_seat
WHERE Id_reservation = 696;


/* Query temp 1 - reservation states */
SELECT * FROM reservationstate;

/* Query temp 2 - reservations */
SELECT * FROM reservation;

/* Query temp 3 - prices */
SELECT * FROM price;

/* Query temp 4 - users */
SELECT * FROM user;

/* Query temp 5 - discounts */
SELECT * FROM discount;