from database import connect_db

class Seasonal:
    def all(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM seasonal')
        flavors = cursor.fetchall()
        conn.close()
        return flavors

    def add(self, name, description, avail_start, avail_end):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO seasonal (name, description, avail_start, avail_end)
            VALUES (?, ?, ?, ?)
        ''', (name, description, avail_start, avail_end))
        conn.commit()
        conn.close()

class Inventory:
    def add(self, name, quantity):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO inventory (name, quantity)
            VALUES (?, ?)
        ''', (name, quantity))
        conn.commit()
        conn.close()

class Allergens:
    def add(self, name):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO allergens (name)
            VALUES (?)
        ''', (name,))
        conn.commit()
        conn.close()

class Suggestions:
    def add(self, flav_name, cust_name, suggestion, allergy_concerns):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO suggestions (flav_name, cust_name, suggestion, allergy_concerns)
            VALUES (?, ?, ?, ?)
        ''', (flav_name, cust_name, suggestion, allergy_concerns))
        conn.commit()
        conn.close()

class Cart:
    def add(self, prod_id, prod_name):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO cart (prod_id, prod_name)
            VALUES (?, ?)
        ''', (prod_id, prod_name))
        conn.commit()
        conn.close()
