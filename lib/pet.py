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

    pass

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


corny = Pet.create("Corny", "dog", "goldendoodle", "mama's boy")


# ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB

# ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB

# ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

# If No "pet" Found, return "None"

# ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

# If No "pet" Found, return "None"

# ✅ 10. Add "find_or_create_by" Class Method to:

#  Find and Retrieve "pet" Instance w/ All Attributes

# If No "pet" Found, Create New "pet" Instance w/ All Attributes

# ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes
