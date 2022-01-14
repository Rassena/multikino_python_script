/*
docker exec -it cassandra_multikino bash
cqlsh
*/
use "multikino";

Select * from artists;
Select * from castings;
Select * from users;
Select * from movies;
Select * from ratings;
Select * from dimensions;
Select * from genres;
Select * from rooms;
Select * from showings;
Select * from tickets;
Select * from ticketStates;
Select * from discounts;
select * from reservations;

Select count(*) as artists from artists;
Select count(*) as castings from castings;
Select count(*) as users from users;
Select count(*) as  movies from movies;
Select count(*) as ratings from ratings;
Select count(*) as dimensions from dimensions;
Select count(*) as genres from genres;
Select count(*) as rooms from rooms;
Select count(*) as showings from showings;
Select count(*) as tickets from tickets;
Select count(*) as ticketStates from ticketStates;
Select count(*) as discounts from discounts;
select count(*) as reservations from reservations;