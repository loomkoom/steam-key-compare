from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# DEFINE THE DATABASE CREDENTIALS
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5436'
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route('/index')
@app.route('/')
def hello_world():  # put application's code here
    return render_template("hello.html", var={'variable': "testing var"})


@app.route('/db')
def db():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from tennis.player''')
    rv = cur.fetchall()
    cur.close()
    return render_template("db.html", db=rv)


if __name__ == '__main__':
    app.run(debug=True)
