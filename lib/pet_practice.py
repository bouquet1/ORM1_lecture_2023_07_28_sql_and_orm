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
    def __init__(self, name, species, breed, temperament, id = None):
        self.id = id
        self.name = name 
        self.species = species
        self.breed = breed
        self.temperament = temperament

    
    # ✅ 2. Add "create_table" Class Method to Create "pet_practice" Table If Doesn't Already Exist - 
    @classmethod
    def create_table (cls):
        sql = """
        CREATE TABLE IF NOT EXISTS pet_practice
        (id INTEGER PRIMARY KEY,
        name TEXT,
        species TEXT,
        breed TEXT,
        temperament TEXT)
    """
        cursor.execute(sql)


# ✅ 3. Add "drop_table" Class Method to Drop "pet_practice" Table If Exists


# ✅ 4. Add "save" Instance Method to Persist New "pet_practice" Instances to DB
   
# ✅ 5. Add "create" Class Method to Initialize and Save New "pet_practice" Instances to DB
   

# ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet_practice" Instance w/ Attributes From DB

# ✅ 7. Add "get_all" Class Method to Retrieve All "pet_practice" Instances From DB

# ✅ 8. Add "find_by_name" Class Method to Retrieve "pet_practice" Instance by "name" Attribute From DB

# If No "pet" Found, return "None"

# ✅ 9. Add "find_by_id" Class Method to Retrieve "pet_practice" Instance by "id" Attribute From DB

# If No "pet_practice" Found, return "None"

# ✅ 10. Add "find_or_create_by" Class Method to:

#  Find and Retrieve "pet" Instance w/ All Attributes

# If No "pet" Found, Create New "pet" Instance w/ All Attributes

# ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes


# 1. how to test that this init is done correctly? : by giving some data and checking the result. fluffy instance is created below. in terminal => python lib/pet_practice.py yazinca => print is executed: fliffy.name=> Fluffy i gormemiz lazim ya da fluffy.temperament => calm gibi
# bukuleta@Bukets-MacBook-Pro ORM1_lecture_2023_07_28_sql_and_orm % python lib/pet_practice.py 
# Fluffy 
# calm

fluffy = Pet("Fluffy", "dog", "Pomeranian", "calm")
print(fluffy.name)
print(fluffy.temperament)