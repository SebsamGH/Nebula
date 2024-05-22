from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/student-data', methods=['GET'])
def get_student_data():
         # Mock data, replace with actual database query
         student_data = {
             'basic_details': {
                 'name': 'Samuel Sebbie',
                 'email': 'sebsamstudio@gmail.com',
                 'cohort': 'Cohort 1',
                 'ranking': 1,
             },
             'performance_metrics': {
                 'assignment_completion': 10,
                 'attendance_average': 95,
             },
             'weekly_attendance': [
                 {'week_id': 1, 'present_days': 5, 'absent_days': 0},
                 {'week_id': 2, 'present_days': 4, 'absent_days': 1},
                 # Add more mock data as needed
             ],
         }
         return jsonify(student_data)

if __name__ == '__main__':
         app.run(debug=True)