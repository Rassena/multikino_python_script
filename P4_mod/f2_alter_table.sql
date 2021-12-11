/* Ticket_TicketState implemented */
DROP TABLE Ticket_TicketState;
CREATE TABLE Ticket_TicketState (
    Id_ticket_ticketState int not null auto_increment,
    Fk_ticket int not null,
    Fk_ticketState int not null,
    Ticket_ticketState_date datetime NOT NULL DEFAULT NOW(),
    FOREIGN KEY (Fk_ticket) REFERENCES Ticket (Id_ticket),
    FOREIGN KEY (Fk_ticketState) REFERENCES TicketState (id_ticketstate),
    PRIMARY KEY (Id_ticket_ticketState)
);

/* Filling table with data from ticket and ticket state with current datetime */
INSERT INTO Ticket_TicketState (Fk_ticket, Fk_ticketState)
    SELECT Id_ticket, Fk_ticketState
    FROM ticket;

SELECT * FROM ticket_ticketstate;

/* Altering movie_movieVersion to contain fks */
ALTER TABLE movie_movieversion
    ADD Fk_translation int,
    ADD Fk_dimension int,
    ADD FOREIGN KEY (Fk_translation) REFERENCES Translation(Id_translation),
    ADD FOREIGN KEY (Fk_dimension) REFERENCES  Dimension(Id_dimension)
;

/* Transfer parameters to movie_movieversion from movieversion */
UPDATE movie_movieversion join movieversion m on m.Id_movieVersion = movie_movieversion.Fk_movieVersion
    SET movie_movieversion.Fk_translation = m.Fk_translation,
        movie_movieversion.Fk_dimension = m.Fk_dimension
;
/* Keys must have been null so that we can copy values, but now they should be not null */
ALTER TABLE movie_movieversion
    MODIFY Fk_translation int not null,
    MODIFY Fk_dimension int not null
;

/* Dropping unnecessary columns from movie_movieVersion */
ALTER TABLE movie_movieversion DROP FOREIGN KEY movie_movieversion_ibfk_2;
ALTER TABLE movie_movieversion DROP COLUMN Fk_movieVersion;

/* Getting rid of movie version, so that we can rename the next one*/
DROP TABLE movieversion;

/* Old movie_movieversion is now our movieVersion */
RENAME TABLE movie_movieversion TO movieVersion;
ALTER TABLE movieversion RENAME COLUMN Id_movie_movieVersion TO Id_movieVersion;

/*  Rename FOREIGN KEY and column in seans to current table name */
ALTER TABLE seans RENAME KEY Fk_movie_MovieVersion TO Fk_movieVersion;
ALTER TABLE seans RENAME COLUMN Fk_movie_MovieVersion TO Fk_movieVersion;

/* Should be gone and not work */
SELECT * FROM movie_movieversion;
DESCRIBE movie_movieversion;

SELECT * FROM movieversion;
DESCRIBE movieVersion;

SELECT * FROM seans;
DESCRIBE seans;
