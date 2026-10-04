"""
Singleton design pattern : It is a creational design pattern and here class can have only one instance globally.
While we can override the __new__ in Python to achieve this.
Realtime Ex:
    Module level global variables, because python modules are natively singletons (They are cached upon first import)
"""
class Database:
    # Class variable
    _conn = None

    # override the __new__ method
    def __new__(cls):
        # Case 1: Check instance already created or not
        if cls._conn is None:
            # Case 2: Create the instance
            cls._conn = super().__new__(cls)
            print("Initializing the connection")
        else:
            print("Existing connection using.")
        return cls._conn

    def manage_connection(self, user):
        print(f"Managing user: {user}")

# Creating connection object for user1 and user2
user1 = Database()
user1.manage_connection("user1")
# Same object will be used since its singleton class
user2 = Database()
user2.manage_connection("user2")

