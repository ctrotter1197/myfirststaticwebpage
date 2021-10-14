from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def page():
    return render_template('GradeStudentIDInfo.html')

@app.route('/GradeReceiver', methods=['GET', 'POST'])
def GradeReceiver():
    if request.method == 'GET':
        student1 = request.form['studentID1']
        student2 = request.form['studentID2']
        student3 = request.form['studentID3']
        grade1 = request.form['grade1']
        grade2 = request.form['grade2']
        grade3 = request.form['grade3']
        average = ((int(grade1) + int(grade2) + int(grade3)) / 3)
        output = "Student ID: %s      Grade: %s" \
                 "Student ID: %s      Grade: %s" \
                 "Student ID: %s      Grade: %s" \
                 "The cumulative average grade is %s"

        return output % (int(student1), int(grade1), int(student2), int(grade2), int(student3),
                         int(grade3), int(average))

if __name__ == '__main__':
    app.run(debug=True)


