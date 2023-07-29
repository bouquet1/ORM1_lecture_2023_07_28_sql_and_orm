# ORM, Part 1 - 2023 July 28
### Instructor: Thompson Plyler

## SWABATs
- [ ] ... define what an ORM is.
- [ ] ... understand what goes into making an ORM
- [ ] ... recognize an ORM as a database tool

## SQL COMMANDS + REVIEW

* SQLITE3 Data Types - https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm

* Create a table
```sql 
CREATE TABLE <tablename>(
    id INTEGER PRIMARY KEY,
    <attribute> TEXT,
    <attribute> INTEGER
    );
```

* Select all from a table
```sql
SELECT * FROM <tablename>
```

* Show tables:
  
```sql
.tables
```

* Add value to table: 
```
INSERT INTO DOG (name, species, breed, temperament)
VALUES("Buffy", "dog", "mixed", "kissy");
```

* Change table? (What if we want to add an attribute?)
```sql
ALTER TABLE <name>
ADD COLUMN birthdate TO age;
```

* Change table? (What if we want to rename an attribute?)
```sql
ALTER TABLE <name>
RENAME COLUMN <column_name> TO <new_column_name>;
```

* Drop a table:
```sql
DROP TABLE <tablename>;
```

* Populate data:
```sql
INSERT INTO <tablename>(<attributes>)
VALUES(<corr>)
```
Example: 
```sql
INSERT INTO owner(name)
VALUES ("Jessie")
```

UPDATE <tablename>
SET <attribute> = <newinput>
WHERE <attribute_to_filter_by> = <how_we_are_filtering>

```sql
UPDATE owner
SET name = "Michael"
WHERE id = 3 
```

What if you forgot your foreign key? 
* Drop the table and start over. 
* OR https://database.guide/add-a-foreign-key-to-an-existing-table-in-sqlite/
* But seriously, just start over with the table!

## JOINS

* INNER JOIN - Gets the dog's name along with owner name and contact information:
```sql
SELECT dog.name, owner.name, owner.phone, owner.email
FROM dog
INNER JOIN owner ON dog.owner_id = owner.id;
```

* LEFT (OUTER) JOIN - Get all dogs and their owner's information, even if they don't have an owner. Absence of owner results in NULL
```sql
SELECT dog.name, owner.name, owner.phone, owner.email
FROM dog
LEFT JOIN owner ON dog.owner_id = owner.id
```

* FULL (OUTER) JOIN - Get all dogs and all owners. Absence of either will result in NULL. 
```sql
SELECT dog.name, owner.name, owner.phone, owner.email
FROM dog
FULL JOIN owner ON dog.owner_id = owner.id;
```

* NATURAL JOIN - If tables have a matching column, a natural join will join them at that column. For instance, instead of owner.id, owner.owner_id.
If there is no matching value, neither entry will appear. 
```sql 
SELCT * 
FROM dog
NATURAL JOIN owner;
```

## ORM
ORM - Object Relational Mapping


## RESOURCES
* [SQLite Data Types](https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm)
* [How to Add a Foreign Key to a Table in SQLite](https://database.guide/add-a-foreign-key-to-an-existing-table-in-sqlite/)
* [How to Install and use Postgres on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-22-04)


## CHATGPT Coding Tutor Prompt from Stan: 
"You are a coding Expert. You will serve as my personal instructor, well versed in the knowledge of CSS, HTML, and JavaScript. You have one goal and one goal only: to teach and reinforce my coding knowledge. Your motto is "I LOVE CODING!!". You are not to give me the direct answers to the questions I ask you. Rather, you will lead me in the direction of the correct answer by quizzing me and inform me of what topics to research to accomplish the given task. You will ask me all questions necessary before providing me with an outline on how to do what I need to do, EXPLICITLY without giving me code blocks. You are not to provide a code block unless responding to a statement that starts with "Provide code for:". Do you understand these rules? Do you have any questions for me that need answered?"

