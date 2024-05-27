from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/project_nebula'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         name = db.Column(db.String(100), nullable=False)
         email = db.Column(db.String(100), nullable=False, unique=True)
         cohort = db.Column(db.String(50), nullable=False)
         ranking = db.Column(db.Integer, nullable=False)
         assignment_completion = db.Column(db.Integer, nullable=False)
         attendance_average = db.Column(db.Float, nullable=False)

class Attendance(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
         week_id = db.Column(db.Integer, nullable=False)
         present_days = db.Column(db.Integer, nullable=False)
         absent_days = db.Column(db.Integer, nullable=False)

@app.route('/api/student-data', methods=['GET'])
def get_student_data():
         student = Student.query.first()
         attendance_records = Attendance.query.filter_by(student_id=student.id).all()
         
         student_data = {
             'basic_details': {
                 'name': student.name,
                 'email': student.email,
                 'cohort': student.cohort,
                 'ranking': student.ranking,
             },
             'performance_metrics': {
                 'assignment_completion': student.assignment_completion,
                 'attendance_average': student.attendance_average,
             },
             'weekly_attendance': [
                 {'week_id': record.week_id, 'present_days': record.present_days, 'absent_days': record.absent_days}
                 for record in attendance_records
             ],
         }
         return jsonify(student_data)

if __name__ == '__main__':
         db.create_all()
         app.run(debug=True)