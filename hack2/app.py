from flask import Flask, render_template, request, redirect
import pymysql.cursors

app = Flask(__name__)

# mydb=mysql.connector.connect(host='172.17.0.2',user='root',password='123456',database='mydb')

connection = pymysql.connect(host='localhost',user='root',password='123456',db='mydb')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        salary=userDetails['salary']
        job_desc=userDetails['job_desc']
        try:
            with connection.cursor() as cursor:
                sql="INSERT INTO myguests(name, email, salary, job_desc) VALUES(%s, %s, %s, %s)",(name, email, salary, job_desc)
                cur = connection.cursor()
                cur.execute("INSERT INTO myguests(name, email, salary, job_desc) VALUES(%s, %s, %s, %s)",(name, email, salary, job_desc))
                connection.commit()
                cur.close()
        except:
            print()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = connection.cursor()
    resultValue = cur.execute("SELECT * FROM myguests")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
