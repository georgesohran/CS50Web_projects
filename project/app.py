from fastapi import FastAPI
import sqlite3

app = FastAPI()

db = sqlite3.connect("database.db")
cur = db.cursor()

cur.execute("INSERT INTO subjects (name) VALUES (history);")
db.commit()

@app.get("/")
def index():
    return "aa"
