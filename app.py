from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    team = (
        'G Nikhil (22EG107A14)',
        'J R Aasrith (22EG107A18)',
        'M Shourya (22EG107A39)',
        'P Abhirama Rao (22EG107A41)',
        'P Rishi Teja (22EG107A42)',
        'P Satya Narayana (22EG107A54)',
        'S. Aftaab Uddin (22EG107A59)',
        'V Anand Vardhan (22EG107A66)',
        'K Varun (23EG507A02)',
        'S Shaad Mehraj (23EG507A06)',
        'V Laxman (23EG507A07)'
    )
    con = sqlite3.connect('books.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(name VARCHAR(32), author VARCHAR(32));")
    con.commit()
    return render_template('home.html', team=team)


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        name = request.form["book_name"]
        author = request.form['book_author']
        print(name, author, type(name), type(author))
        con = sqlite3.connect('books.db')
        cur = con.cursor()
        cur.execute("INSERT INTO books(name, author) VALUES (?, ?)", (name, author))
        con.commit()
        con.close()
    return render_template('insert.html')


@app.route('/select', methods=['GET', 'POST'])
def select():
    con = sqlite3.connect('books.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM books;")
    rows = cur.fetchall()
    return render_template('select.html', headers=('names', 'authors'), rownames=rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
