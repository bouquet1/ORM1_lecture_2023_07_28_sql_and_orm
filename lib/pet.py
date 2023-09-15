# Stretch Goal: Include Association with Owner

# Pet Attributes:
# name: TEXT
# species: TEXT
# breed: TEXT
# temperament: TEXT

# Stretch Goal
# owner_id: INTEGER

import sqlite3

connection = sqlite3.connect('lib/resources.db')
cursor = connection.cursor()


class Pet:
    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__(self, name, species, breed, temperament, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament

# ✅ 2. Add "create_table" Class Method to Create "pet" Table If Doesn't Already Exist
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pet
            (id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            breed TEXT,
            temperament TEXT)
    """
        cursor.execute(sql)


# ✅ 3. Add "drop_table" Class Method to Drop "pet" Table If Exists

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pet
    """
        cursor.execute(sql)

# ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
    def save(self):
        print(self.name)
        sql = """
            INSERT INTO pet (name, species, breed, temperament)
            VALUES(?,?,?,?)
        """
        cursor.execute(sql, (self.name, self.species,
                       self.breed, self.temperament))
        connection.commit()

# ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create(cls, name, species, breed, temperament):
        pet = cls(name, species, breed, temperament)
        pet.save()
        return pet


# corny = Pet.create("Corny", "dog", "goldendoodle", "mama's boy")
# stella = Pet.create("Stella", "dog", "goldendoodle", "traitor")


# ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB

    @classmethod
    def new_from_db(cls, row):
        cursor.execute(
            "SELECT last_insert_rowid() FROM pet").fetchone()[0]

        pet = cls(row[0], row[1], row[2], row[3], row[4])
        return pet


# ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB


    @classmethod
    def get_all(cls):
        sql = """
                SELECT * FROM pet
        """
        all = cursor.execute(sql).fetchall()
        print(all)
        # testing: result when run this file: [(1, 'Buffy', 'dog', 'mixed', 'kissy'), (2, 'Corny', 'dog', 'goldendoodle', "mama's boy"), (3, 'Savannah', 'dog', 'goldendoodle', 'traitor')]
        return [cls.new_from_db(row) for row in all]


# all = Pet.get_all()
# print(all)
# testing: result when file run python lib/pet_practice.py: [<__main__.Pet object at 0x10aeb2c40>, <__main__.Pet object at 0x10aeb27f0>, <__main__.Pet object at 0x10aeb2730>]


# ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB
# If No "pet" Found, return "None"


    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM pet
            WHERE name = ?
            LIMIT 1
    """
        pet = cursor.execute(sql, (name,)).fetchone()
        # name does not exist. Return something in a way if there is nothing, the name doesn't match or doesn't exist
        if not pet:
            return None
        # print(pet)
        # test: denedik print(pet) returns (1, 'Buffy', 'dog', 'mixed', 'kissy')
        # assume pet name does exist
        return cls(pet[1], pet[2], pet[3], pet[4], pet[0])

# test icin
# pet = Pet.find_by_name("Buffy")
# print(pet)


# ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

# If No "pet" Found, return "None"


    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM pet
            WHERE id = ?
            LIMIT 1
    """
        pet = cursor.execute(sql, (id,)).fetchone()
        if not pet:
            return None
        return cls(
            id=pet[0],
            name=pet[1],
            species=pet[2],
            breed=pet[3],
            temperament=pet[4],)

# testing:
# corny = Pet.find_by_id(2)
# print(corny)


# ✅ 10. Add "find_or_create_by" Class Method to:
#  Find and Retrieve "pet" Instance w/ All Attributes
# If No "pet" Found, Create New "pet" Instance w/ All Attributes

    @classmethod
    def find_or_create_by(cls, name, species, breed, temperament):
        sql = """
                SELECT * FROM pet
                WHERE name, species, breed, temperament = (?, ?, ?, ?)
                LIMIT 1
    """
        # alternative to write sql above differently, slightly different syntax
    #    sql = """
    #         SELECT * FROM pet
    #         WHERE name = ? AND species = ? AND breed = ? AND temperament = ?
    #         LIMIT 1
    # """
        pet = cursor.execute(
            sql, (name, species, breed, temperament)).fetchone()
        # one way to write it -create() method is above and it has return statement in it that returns the pet. row 5 came with this code and tersting below.
        # if not pet:
        #     cls.create(name, species, breed, temperament)

        # we can also write like that to create new pet. testing this code created row 6.
        if not pet:
            new_pet = cls.create(name, species, breed, temperament)
            return new_pet

        return cls(
            name=pet[1],
            species=pet[2],
            breed=pet[3],
            temperament=pet[4],
            id=pet[0],
        )

# testing:
# pet = Pet.find_or_create_by("Buffy", "dog", "mixed", "kissy")
# print(pet)
# result in terminal: <__main__.Pet object at 0x101c5e7f0> it works

# testing:
# pet = Pet.find_or_create_by("Buffy", None, "mixed", "kissy")
# print(pet)

# ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes
    # Lecture instant method and clasmethod versions
    # @classmethod
    def update_c(cls):
        sql = """
        UPDATE pet 
        SET name = ?, 
        species = ?, 
        breed = ?, 
        temperament = ? 
        WHERE id = ?
    """
        pass

    # with instance method
    def update(self, name, species, breed, temperament):
        # inside the parantheses are the argument thats going to be passed down below. when we do cursor execute self.name f.e we're passing in the qualities/attributes. we can change all or any of them we want.
        self.name = name or self.name
        self.species = species or self.species
        self.breed = breed or self.breed
        self.temperament = temperament or self.temperament
        # or self.attribute kismini sadece belli attributelari degistimek istersek diye ekledik. mesela name farkli parameter olarak verildiyse update edecek degilse aynen kalacak.

        sql = """
            UPDATE pet SET name = ?, species = ?, breed = ?, temperament =? 
            WHERE id = ?
    """
        pet = cursor.execute(
            sql, (self.name, self.species, self.breed, self.temperament, self.id))
        connection.commit()


# test icin yaptim buffy scruffy oldu. sonra da buffy tekrar geri aldik.
# buffy = Pet.find_by_id(1)  first we retrieved, we grabbed the buffy then update
# # print(buffy.name)
# buffy.update("Scruffy", "cat", "persian", "annoying")
# buffy = Pet.find_by_name("Scruffy")
# buffy.update("buffy", "dog", "mixed", "kissy")
buffy = Pet.find_by_name("buffy")
buffy.update("buffy", "dog", "mixed", "silly")

# test codun attribute larini OR lu yazdiktan sonra
# buffy = Pet.find_by_name("buffy")
# buffy.update(None, None, None, "sleepy") we could put " " instead of None we could still get the same result becasue " " is falsey
# print(buffy.name)
# result: <__main__.Pet object at 0x1030e7880> and kisy changed to sleepy

# MOST OF THE TIME You will change only certain qualities/attributes from the DB not everything
