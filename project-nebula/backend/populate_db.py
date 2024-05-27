from app import db, Student, Attendance

db.create_all()

student = Student(
         name='Samuel Sebbie',
         email='sebsamstudio@gmail.com',
         cohort='Cohort 1',
         ranking=1,
         assignment_completion=10,
         attendance_average=95.0
     )
db.session.add(student)
db.session.commit()

attendance_records = [
         Attendance(student_id=student.id, week_id=1, present_days=5, absent_days=0),
         Attendance(student_id=student.id, week_id=2, present_days=4, absent_days=1),
         # Add more records as needed
     ]
db.session.bulk_save_objects(attendance_records)
db.session.commit()