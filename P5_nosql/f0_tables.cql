Drop table artists;
Drop table castings;
Drop table users;
Drop table movies;
Drop table ratings;
Drop table dimensions;
Drop table genres;
Drop table rooms;
Drop table showings;
Drop table tickets;
Drop table ticketStates;
Drop table discounts;

CREATE TABLE artists (
    Id_artist int,
    Artist_name text,
    Artist_surname text,
    Artist_birth date,
    Artist_gender boolean,
    PRIMARY KEY (Id_artist)
);

CREATE TABLE castings (
    Artist_id int,
    Artist_name text,
    Artist_surname text,
    Role_name text,
    Movie_id int,
    Movie_title text,
    PRIMARY KEY (Movie_id, Artist_id, Role_name)
);

CREATE TABLE users (
    Id_user int,
    User_name text,
    User_surname text,
    User_email text,
    User_password text,
    User_birth date,
    User_privilege set<text>,
    PRIMARY KEY (User_surname, Id_user)
);

CREATE TABLE movies (
    Id_movie int,
    Movie_title text,
    Movie_description text,
    Movie_premiere date,
    Movie_duration int,
    Age_restriction text,
    Poster_path text,
    Tags_country set<text>,
    Tags_translation_dimension_basePrice set<tuple<text, text, double>>,
    PRIMARY KEY (Id_movie, Movie_title)
);

CREATE TABLE ratings (
    Movie_id int,
    Movie_title text,
    User_id int,
    Rating_value int,
    PRIMARY KEY (Movie_id, User_id)
);

CREATE TABLE dimensions (
    Dimension_name text,
    Dimension_basePrice double,
    PRIMARY KEY (Dimension_name)
);

CREATE TABLE discounts (
    Discount_name text,
    Dimension_name text,
    Dimension_basePrice double,
    Discount_price double,
    PRIMARY KEY (Dimension_name, Discount_name)
);

CREATE TABLE genres (
    Movie_id int,
    Movie_title text,
    Genre_name text,
    PRIMARY KEY (Movie_id, Genre_name)
);

CREATE TABLE rooms (
    Room_name text,
    Room_set_row_seatNr set<tuple<text, int>>,
    PRIMARY KEY (Room_name)
);

CREATE TABLE showings (
    Id_showing int,

    Showing_date date,
    Showing_time time,


    Movie_id int,
    Movie_title text,
    Movie_translation text,
    Movie_duration int,

    Dimension_name text,
    Dimension_basePrice double,

    Room_name text,
    Room_set_row_seatNr set<tuple<text, int>>,
    set_discountName_price set<tuple<text, double>>,
    PRIMARY KEY (Showing_date, Showing_time, Movie_id, Room_name, Id_showing)
);

CREATE TABLE tickets (
    Id_ticket int,

    Showing_id int,
    Showing_date date,
    Showing_time time,


    Movie_title text,
    Movie_translation text,

    Discount_name text,
    Dimension_name text,

    Room_name text,
    Room_row text,
    Room_seat int,

    User_id int,
    User_surname text,

    Discount_price double,
    Ticket_state text,
    Ticket_reservation int,

    PRIMARY KEY (Showing_date, Ticket_reservation, Showing_time, Showing_id, Id_ticket)
);

CREATE TABLE ticketStates (
    TicketState_timestamp timestamp,
    TicketState_name text,

    Ticket_id int,

    Room_row text,
    Room_seat int,

    Showing_id int,
    Showing_date date,
    Showing_time time,


    Movie_title text,
    User_id int,
    User_surname text,
    Ticket_reservation int,

    PRIMARY KEY ((Showing_date, Showing_id), TicketState_timestamp, Ticket_reservation, Ticket_id)
)
WITH CLUSTERING ORDER BY (TicketState_timestamp DESC);

CREATE TABLE reservations (
    Id_reservation int,

    User_id int,
    User_surname text,

    Showing_id int,
    Showing_date date,
    Showing_time time,

    Movie_id int,
    Movie_title text,
    Movie_translation text,

    Room_name text,
    Map_ticket_row_seatNr map<int, tuple<text, int>>,

    PRIMARY KEY (User_id, Showing_date, Showing_time, Room_name)
)
