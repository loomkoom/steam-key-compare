from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# DEFINE THE DATABASE CREDENTIALS
app.config['MYSQL_HOST'] = '192.168.0.48'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '5436'
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


def fetch_players():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from tennis.player''')
    rv = cur.fetchall()
    cur.close()
    return rv


@app.route('/index')
@app.route('/')
def hello_world():  # put application's code here
    return render_template("hello.html", var={'variable': "testing var"})


@app.route('/db/')
def db_base():
    return '<a href="/db/simple">Simple</a>\n' \
           '<a href="/db/table">DataTable</a>'


@app.route('/db/<template>')
def db(template):
    rv = fetch_players()
    return render_template(f"db_{template}.html", db=rv)


if __name__ == '__main__':
    app.run(debug=True)
