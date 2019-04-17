import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def update_clicks(id, clicks, db):
    conn = sqlite3.connect(BASE_DIR + '/db.sqlite3', check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE " + db + " SET clicks = (?) WHERE id = (?)",
              (str(clicks), str(id)))
    conn.commit()
    conn.close()
