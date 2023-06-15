with open('myfile.txt') as file:
    data = file.read()
    # Do something awesome with the data!

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.connect()  # Acquire the database connection
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()  # Release the database connection

    def connect(self):
        print(f"Connecting to database: {self.db_name}")

    def disconnect(self):
        print(f"Disconnecting from database: {self.db_name}")

# Usage
with DatabaseConnection('mydb') as db:
    # Perform database operations here
    # The connection will be automatically released afterward