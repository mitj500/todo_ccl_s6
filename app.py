from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="database-1.c7g86aoqaeg1.us-east-1.rds.amazonaws.com",
    user="admin",
    port=3306,
    password="12345678",
    database="db_ccl"
)
cursor = mydb.cursor()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        importance = int(request.form['degree'])

        query = "INSERT INTO todos (todo_name, importance) VALUES (%s, %s)"
        values = (content, importance)
        cursor.execute(query, values)
        mydb.commit()

        return redirect(url_for('index'))

    query = "SELECT todo_name, importance FROM todos"
    cursor.execute(query)
    todos1 = cursor.fetchall()

    return render_template('home.html', todos=todos1)

@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        todo_id = request.form['todo_id']

        query = "DELETE FROM todos WHERE todo_name = %s"
        values = (todo_id,)
        cursor.execute(query, values)
        mydb.commit()

        return redirect(url_for('index'))
    
# write  a code to render the sign_in.html page

@app.route("/sign_in",methods=['POST'])
def sign_in():
    return render_template('sign_in.html')

if __name__ == "__main__":
    app.run(debug=True)
