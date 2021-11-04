DROP database multikino;
Create database multikino;

USE multikino;
CREATE TABLE AgeRestriction (
    Id_ageRestriction int not null auto_increment,
    AgeRestriction_name varchar(30),
    PRIMARY KEY (Id_ageRestriction)
);

CREATE TABLE Room (
    Id_room int not null auto_increment,
    Room_sign VARCHAR(30),
    PRIMARY KEY (id_room)
);

CREATE TABLE ReservationState (
    Id_reservationState int not null auto_increment,
    ReservationState_name varchar(255),
    PRIMARY KEY (Id_reservationState)
);

CREATE TABLE Role (
    Id_role int not null auto_increment,
    Role_name varchar(255),
    PRIMARY KEY (id_role)
);

CREATE TABLE Translation (
    Id_translation int not null auto_increment,
    Translation_name varchar(255),
    PRIMARY KEY (id_translation)
);

CREATE TABLE Artist (
    Id_artist int not null auto_increment,
    Artist_name varchar(255),
    Artist_surname varchar(255),
    Artist_birth DATE ,
    Artist_gender bool,
    PRIMARY KEY (Id_artist)
);


CREATE TABLE User (
    Id_user int not null auto_increment,
    User_name varchar(255),
    User_surname varchar(255),
    User_email varchar(255) UNIQUE NOT NULL,
    user_password varchar(255) NOT NULL,
    User_birth date,
    PRIMARY KEY (id_user)
);

CREATE TABLE Seat (
    Id_seat int not null auto_increment,
    Seat_row varchar(30),
    Seat_number int CHECK (Seat_number > 0),
    Fk_room int,
    FOREIGN KEY (Fk_room) REFERENCES Room (Id_room),
    PRIMARY KEY (id_seat)
);

CREATE TABLE Movie (
    Id_movie int not null auto_increment,
    Movie_name varchar(255),
    Movie_description varchar(255),
    Movie_premiere DATE,
    Movie_duration int CHECK (Movie_duration > 0),
    Fk_ageRestriction int,
    FOREIGN KEY (Fk_ageRestriction) REFERENCES AgeRestriction(Id_ageRestriction),
    PRIMARY KEY (Id_movie)
);

CREATE TABLE CastAssignment (
    Id_castAssignment int not null auto_increment,
    Fk_artist int not null,
    Fk_movie int not null,
    Fk_role int not null,
    FOREIGN KEY (Fk_artist) REFERENCES Artist (Id_artist),
    FOREIGN KEY (Fk_movie) REFERENCES Movie (Id_movie),
    FOREIGN KEY (Fk_role) REFERENCES Role (Id_role),
    PRIMARY KEY (Id_castAssignment)
);

CREATE TABLE Country(
    Id_country int not null auto_increment,
    Country_name varchar(30),
    PRIMARY KEY (Id_country)
);

CREATE TABLE Dimension (
    Id_dimension int not null auto_increment,
    Dimension_name varchar(30),
    PRIMARY KEY (Id_dimension)
);

CREATE TABLE Discount(
    Id_discount int not null auto_increment,
    Discount_name varchar(30),
    PRIMARY KEY (Id_discount)
);

CREATE TABLE Genre (
    Id_genre int not null auto_increment,
    Genre_name varchar(30),
    PRIMARY KEY (Id_genre)
);

CREATE TABLE MovieVersion(
    Id_movieVersion int not null auto_increment,
    Fk_translation int not null,
    Fk_dimension int not null,
    FOREIGN KEY (Fk_translation) REFERENCES Translation(Id_translation),
    FOREIGN KEY (Fk_dimension) REFERENCES  Dimension(Id_dimension),
    PRIMARY KEY (Id_movieVersion)
);

CREATE TABLE Movie_Country (
    Id_movie_country int not null auto_increment,
    Fk_movie int not null,
    Fk_country int not null,
    FOREIGN KEY (Fk_movie) REFERENCES Movie (id_movie),
    FOREIGN KEY (Fk_country) REFERENCES Country (id_country),
    PRIMARY KEY (Id_movie_country)
);

CREATE TABLE Movie_Genre(
    Id_movie_genre int not null auto_increment,
    Fk_movie int not null,
    Fk_genre int not null,
    FOREIGN KEY (Fk_movie) REFERENCES Movie (id_movie),
    FOREIGN KEY (Fk_genre) REFERENCES Genre (id_genre),
    PRIMARY KEY (Id_Movie_genre)
);

CREATE TABLE Movie_MovieVersion(
    Id_movie_movieVersion int not null auto_increment,
    Fk_movie int not null,
    Fk_movieVersion int not null,
    FOREIGN KEY (Fk_movie) REFERENCES Movie (id_movie),
    FOREIGN KEY (Fk_movieVersion) REFERENCES MovieVersion(Id_movieVersion),
    PRIMARY KEY (Id_movie_movieVersion)
);



CREATE TABLE Poster (
    Id_poster int not null auto_increment,
    Poster_path varchar(255),
    Fk_movie int,
    FOREIGN KEY (Fk_movie) REFERENCES Movie (Id_movie),
    PRIMARY KEY (Id_poster)
);

CREATE TABLE Price (
    Id_price int not null auto_increment,
    Price_value float CHECK (Price_value >= 0),
    Fk_dimension int,
    FOREIGN KEY (Fk_dimension) REFERENCES Dimension (Id_dimension),
    PRIMARY KEY (Id_price)
);

CREATE TABLE Privilege (
    Id_privilege int not null auto_increment,
    Privilege_name varchar(255) UNIQUE NOT NULL,
    PRIMARY KEY (Id_privilege)
);

CREATE TABLE PrivilegeAssignment (
    Id_privilegeAssignment int not null auto_increment,
    Fk_privilege int not null,
    Fk_user int not null,
    FOREIGN KEY (Fk_privilege) REFERENCES Privilege(Id_privilege),
    FOREIGN KEY (Fk_user) REFERENCES User (Id_user),
    PRIMARY KEY (Id_privilegeAssignment)
);

CREATE TABLE Rating (
    Id_rating int not null auto_increment,
    Fk_movie int not null,
    Fk_user int not null,
    Rating_rate int CHECK (1 <= Rating_rate <= 10),
    FOREIGN KEY (Fk_movie) REFERENCES Movie (Id_movie),
    FOREIGN KEY (Fk_user) REFERENCES User (Id_user),
    PRIMARY KEY (Id_rating)
);

CREATE TABLE Seans (
    Id_seans int not null auto_increment,
    Fk_room int not null,
    Fk_movieVersion int not null,
    Seans_date date not null,
    Seans_time time,
    FOREIGN KEY (Fk_room) REFERENCES Room (Id_room),
    FOREIGN KEY (Fk_movieVersion) REFERENCES MovieVersion (Id_movieVersion),
    PRIMARY KEY (id_seans)
);

CREATE TABLE Reservation (
    Id_reservation int not null auto_increment,
    Fk_seans int not null,
    Fk_reservationState int not null,
    Fk_user int,
    FOREIGN KEY (Fk_seans) REFERENCES Seans (Id_seans),
    FOREIGN KEY (Fk_reservationState) REFERENCES ReservationState (id_reservationState),
    FOREIGN KEY (Fk_user) REFERENCES User (Id_user),
    PRIMARY KEY (Id_reservation)
);

CREATE TABLE Ticket (
    Id_ticket int not null auto_increment,
    Fk_seat int not null,
    Fk_reservation int not null,
    Fk_discount int,
    Fk_price int not null,
    FOREIGN KEY (Fk_seat) REFERENCES Seat (Id_seat),
    FOREIGN KEY (Fk_reservation) REFERENCES Reservation (Id_reservation),
    FOREIGN KEY (Fk_discount) REFERENCES Discount (Id_discount),
    FOREIGN KEY (Fk_price) REFERENCES Price (Id_price),
    PRIMARY KEY (id_ticket)
);
