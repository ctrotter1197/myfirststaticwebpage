import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def service():
    return render_template('SenderAsAService.html')

@app.route('/DatabaseConnection', methods=['GET', 'POST'])
def DatabaseConnection():
    if request.method == 'POST':
        student1 = request.form['studentID1']
        student2 = request.form['studentID2']
        student3 = request.form['studentID3']
        grade1 = request.form['grade1']
        grade2 = request.form['grade2']
        grade3 = request.form['grade3']
    server = "christrottersqlserver.database.windows.net"
    username = "christrotter1197"
    password = "Chris1197"
    database_name = "ChrisTrotterDatabase"

    connection = mysql.connector.connect(server, username, password, database_name)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO StudentGrades (StudentID, Grade) VALUES (%s, %s);", (int(student1), int(grade1)))
    cursor.execute("INSERT INTO StudentGrades (StudentID, Grade) VALUES (%s, %s);", (int(student2), int(grade2)))
    cursor.execute("INSERT INTO StudentGrades (StudentID, Grade) VALUES (%s, %s);", (int(student3), int(grade3)))
    cursor.execute("SELECT AVG(Grade) AS CumulativeAverage FROM StudentGrades;")

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    app.run(debug=True)
