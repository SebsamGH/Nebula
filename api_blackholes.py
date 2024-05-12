from flask import Flask, request, jsonify

app = Flask(__name__)

# Example student data (replace with actual data retrieval logic)
students = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "cohort": "Class A", "ranking": 1},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "cohort": "Class B", "ranking": 2}
]

# API endpoint to retrieve all students
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)

# API endpoint to retrieve a specific student by ID
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({'error': 'Student not found'}), 404

if __name__ == '_main_':
    app.run(debug=True)