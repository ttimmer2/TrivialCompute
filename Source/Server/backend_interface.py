import sqlite3
import os

class backend_interface(object):
    db_path = os.path.join(os.path.dirname(os.getcwd()),"Backend","trivial_compute.db")
    _self = None

    def __new__(cls):
        """
        Create the backend interface object if no instance exists.
        else return previous object
        """
        if cls._self is None:
            cls._self = super().__new__(cls)
            cls.connection = sqlite3.connect(backend_interface.db_path)
            cls.cursor = cls.connection.cursor()
        return cls._self



    def get_categories(self):
        """
        Get the categories from the Categories table and return as a 
        list of the strings.
        """
        res = self.cursor.execute("SELECT DISTINCT Category from Categories")
        r = res.fetchall()
        if r:
            return [str(tup[0]) for tup in r]  # reformat return value
        else:
            return []
        

    def add_category(self, category):
        """
        Takes as input one category - inserts it into the category table, and commits to the database.
        We use bindings to prevent injection attacks.
        """
        res = self.cursor.execute("INSERT INTO Categories VALUES (?)",(category,))
        self.connection.commit()


    def get_question(self, category, min_index=0):
        """
        Get the categories from the Categories table and return as a 
        list of the strings.
        """
        res = self.cursor.execute(f"SELECT DISTINCT * from Questions WHERE Category LIKE '{category}' AND rowid > {min_index}")
        r = res.fetchall()
        if r:
            return r[0]  # reformat return value
        else:
            return []
        

    def add_question(self, category, question, answer):
        """
        Takes as input one category, qustion, and answer - inserts it into the Questions table, and commits to the database.
        We use bindings to prevent injection attacks.
        """
        res = self.cursor.execute("INSERT INTO Questions (\"Category\", \"Question\", \"Answer\") VALUES (?, ?, ?)",(category,question,answer,))
        self.connection.commit()    


if __name__ == "__main__":
    bi = backend_interface()
    print("GETTING CATEGORIES")
    print(bi.get_categories())
    bi.add_category("Test Category")

    print("GETTING QUESTION:")
    print(bi.get_question("History"))

    print("INSERTING QUESTION:")
    bi.add_question("Test Category","; DROP TABLE Categories","--; SELECT * FROM Schema")

