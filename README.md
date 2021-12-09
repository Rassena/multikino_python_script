# PROJEKT RELACYJNEJ BAZY DANYCH

## [Planning](P0_planning)
First draft of a database. File [multikino_database.vpp](P0_planning/multikino_database.vpp) contains class diagram.
![image](https://user-images.githubusercontent.com/61067969/143085033-d5442ea3-0b05-49d4-a622-153d75e92d6c.png)

## [Initializing database](P1_initializing_database)
- File [f1_creating_empty_tables](P1_initializing_database/f1_creating_empty_tables.sql) creates tables in SQL DDL 
according to the draft.

- File [f4_adding_objects_to_database](P1_initializing_database/f4_adding_objects_to_database.py) 
fills database with objects generated in [f3_creating_all_objects](P1_initializing_database/f3_creating_all_objects.py).

- File [f2_3_tables_as_classes](P1_initializing_database/f2_3_tables_as_classes.py) contains classes with attributes 
with the same names and in the same order as they are implemented in [SQL DDL](P1_initializing_database/f1_creating_empty_tables.sql).

ex.
```sql
CREATE TABLE TicketState (
    Id_ticketState int not null auto_increment,
    TicketState_name varchar(255),
    PRIMARY KEY (Id_ticketState)
);
```
```python
class TicketState(ObjectWithCounter, AddableToDatabase):
    def __init__(self, ticket_state_name: str):
        self.Id_ticketState: int = TicketState.next()
        self.TicketState_name: str = ticket_state_name
```

## [Queries & interfaces](P2_queries_and_interfaces)
- File [Interfejs](P2_queries_and_interfaces/Interfejs.pdf) contains a pdf version of the database interface created in Balsamiq.
- File [queries](P2_queries_and_interfaces/queries.sql) contains queries created according to the needs that came up 
while planing the interface. In the comment of each query there are numbers relating to the page number 
in the [interface file](P2_queries_and_interfaces/Interfejs.pdf).

## [Explain & indexes](P3_explain_and_indexes)

## [Modification](P4_mod)

## Other

![image](https://user-images.githubusercontent.com/61067969/143007686-e8a512b7-51b7-426e-95ff-36d25ed8ece1.png)

![image](https://user-images.githubusercontent.com/61067969/143007772-7fc56a09-fb53-426e-8cd9-df4e7de95b28.png)

![image](https://user-images.githubusercontent.com/61067969/143007839-677e516a-cbd1-40a3-8398-6ea9b7017a5d.png)
