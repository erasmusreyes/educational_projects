import sqlite3
from contextlib import closing
from business import make_transaction

conn = None

# Connect database
def connect_db():
    global conn
    if not conn:
        DB_FILE = r"C:\Users\erasm\Documents\GitHub\Python Personal Finance Tracker Final Project\data\finance_tracker.db"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        
# Close database       
def close():
    if conn:
        conn.close()
              
# View all transactions
def view_all_transactions():
    query = '''SELECT transaction_id, date, type, description, amount
                FROM transactions
                Order By transaction_id ASC'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    transactions = []
    for row in results:
        transaction = make_transaction(row)
        transactions.append(transaction)

    return transactions

# Filter by transaction type
def get_by_transaction_type(transaction_type):
    sql = '''SELECT transaction_id, date, type, description, amount
            FROM transactions
            WHERE type = ?
            ORDER BY transaction_id'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (transaction_type,))
        results = c.fetchall()
        
    return results if results else []

# Add transactions
def add_transaction(date, type_, description, amount):
    sql = '''INSERT INTO transactions
                (date, type, description, amount)
                VALUES(?,?,?,?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (date, type_, description, amount))
        conn.commit()
        return c.lastrowid

# Edit transaction
def edit_transaction(transaction_id, date, type_, description, amount):
    sql = '''UPDATE transactions
            SET date = ?, type = ?, description = ?, amount = ?
            WHERE transaction_id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (date, type_, description, amount, transaction_id ))
        conn.commit()

# Delete transaction
def delete_transaction(transaction_id):
    sql = '''DELETE FROM transactions
            WHERE transaction_id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (transaction_id,))
        conn.commit()






        



        
    




                
  
                   
