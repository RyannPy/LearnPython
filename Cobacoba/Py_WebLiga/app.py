from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
  conn = sqlite3.connect("liga.db")
  conn.row_factory = sqlite3.Row
  return conn
  
# ngetokno klasemen e
@app.route('/')
def home():
  conn = get_db_connection()
  klasemen = conn.execute("SELECT * FROM klasemen ORDER BY Point DESC, GC DESC, Goal DESC, Conceded ASC").fetchall()
  conn.close()
  return render_template("index.html", klasemen=klasemen)
  
#jupuk data
@app.route('/tambah', methods=['POST'])
def tambah():
  tim1 = request.form['tim1']
  skor1 = int(request.form['skor1'])
  tim2 = request.form['tim2']
  skor2 = int(request.form['skor2'])
  
  print(f"Tim1: {tim1}, Skor1: {skor1}, Tim2: {tim2}, Skor2: {skor2}")
  
  conn = get_db_connection()
  cursor = conn.cursor()
  
#logika menang/kalah
  if skor1 > skor2:
    winner = tim1
    loser = tim2
    pointWinner = 3
    pointLoser = 0
  elif skor1 < skor2:
    winner = tim2
    loser = tim1
    pointWinner = 3
    pointLoser = 0
  else:
    winner = loser = None
    pointWinner = pointLoser = 1
    
  #update goal/conceded
  cursor.execute("UPDATE Klasemen SET Goal = Goal + ?, Conceded = Conceded + ?, GC = Goal - Conceded WHERE Tim = ?", (skor1, skor2, tim1))
  cursor.execute("UPDATE Klasemen SET Goal = Goal + ?, Conceded = Conceded + ?, GC = Goal - Conceded WHERE Tim = ?", (skor2, skor1, tim2))
  #update win lose draw point
  if winner:
    cursor.execute("UPDATE Klasemen SET Win = Win + 1, Point = Point + ? WHERE Tim = ?", (pointWinner, winner))
    cursor.execute("UPDATE Klasemen SET Lose = Lose + 1, Point = Point + ? WHERE Tim = ?", (pointLoser, loser))
  else:
    cursor.execute("UPDATE Klasemen SET Draw = Draw + 1, Point = Point + 1 WHERE Tim = ?", (tim1, ))
    cursor.execute("UPDATE Klasemen SET Draw = Draw + 1, Point = Point + 1 WHERE Tim = ?", (tim2, ))
    
  print("Melakukan update di Database")
  conn.commit()
  conn.close()
    
  return redirect('/')
    
if __name__ == "__main__":
  app.run(debug=True, host= "0.0.0.0")