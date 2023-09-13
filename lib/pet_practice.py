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


# ✅ 2. Add "create_table" Class Method to Create "pet_practice" Table If Doesn't Already Exist -


    @classmethod
    def create_table(cls):
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
    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS pet_practice
    """
        cursor.execute(sql)


# ✅ 4. Add "save" Instance Method to Persist New "pet_practice" Instances to DB. Instance method NOT class method.

    def save(self):
        sql = """
        INSERT INTO pet_practice (name, species, breed, temperament)
        VALUES (?, ?, ?, ?)
    """
    # persist it using cursor.execute
        cursor.execute(sql, (self.name, self.species,
                       self.breed, self.temperament))
    # commit it
        connection.commit()


# canvas daki save yontemini kullanilabilir. Check the notes below # 4.

# ✅ 5. Add "create" Class Method to Initialize and Save New "pet_practice" Instances to DB

    @classmethod
    def create(cls, name, species, breed, temperament):
        pet = cls(name, species, breed, temperament)
        pet.save()
        return pet

# her python lib/pet_practice.py run yaptigimda cornyi savannahi vebuffyi tekrar tekrar ekliyor ondan kapattim
# corny = Pet.create("Corny", "dog", "goldendoodle", "mama's boy")
# savannah = Pet.create('Savannah', 'dog', 'goldendoodle', 'traitor')

# ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet_practice" Instance w/ Attributes From DB
    @classmethod
    def new_from_db(cls, row):
        cursor.execute(
            "SELECT last_insert_rowid() FROM pet_practice").fetchone()[0]

        pet = cls(row[0], row[1], row[2], row[3], row[4])
        return pet

# ✅ 7. Add "get_all" Class Method to Retrieve All "pet_practice" Instances From DB

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM pet_practice
    """
        all = cursor.execute(sql).fetchall()
        print(all)
        # testing: result when run this file: [(1, 'Buffy', 'dog', 'mixed', 'kissy'), (2, 'Corny', 'dog', 'goldendoodle', "mama's boy"), (3, 'Savannah', 'dog', 'goldendoodle', 'traitor')]
        return [cls.new_from_db(row) for row in all]


all = Pet.get_all()
print(all)
# testing: result when file run python lib/pet_practice.py: [<__main__.Pet object at 0x10aeb2c40>, <__main__.Pet object at 0x10aeb27f0>, <__main__.Pet object at 0x10aeb2730>]

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

# 2. how to test that this init is done correctly? : under our cart add Pet.create_table() -execute our create_table classmethod- in terminal run python lib/pet_practice.py and then refresh tge resources.db at the left and pet_practice table is created. (we run the table)
# Pet.create_table()


# 3. how to test that this init is done correctly? : Pet.drop_table() yazdik. sonra terminal de python lib/pet_practice.py yazip run the code. refresh database and the table is gone.
# Pet.drop_table()

# 4. canvas daki save yontemini kullanilabilir.
#     def save(self,cursor):
#         cursor.execute(
#             'INSERT INTO pet_practice(name, species, breed, temperament) VALUES (?, ?, ?, ?)',
#             (self.name, self.species, self.breed, self.temperament)
#         )
#         connection.commit()

# 4. how to test that this init is done correctly? : add a data, dog buffy.

# buffy = Pet("Buffy", "dog", "mixed", "kissy")
# buffy.save()
