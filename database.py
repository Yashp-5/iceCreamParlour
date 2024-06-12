import sqlite3

def connect_db():
    return sqlite3.connect('ice_cream.db')

def create_tables():
    conn=connect_db()
    cursor= conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal(id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    avail_start DATE,
                    avail_end DATE)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL)''')
    cursor.execute(''' CREATE TABLE IF NOT EXISTS allergens(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL)''')
    cursor.execute(''' CREATE TABLE IF NOT EXISTS suggestions(
                    id INTEGER PRIMARY KEY,
                    flav_name TEXT NOT NULL,
                    cust_name TEXT,
                    suggestion TEXT,
                    allergy_concerns TEXT)
                    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS cart(
                    id INTEGER PRIMARY KEY,
                    prod_id INTEGER NOT NULL,
                    prod_name TEXT NOT NULL,
                    FOREIGN KEY(prod_id) REFERENCES seasonal(id))
                    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
