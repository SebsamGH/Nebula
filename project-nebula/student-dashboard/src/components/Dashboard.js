import React, { useEffect, useState } from 'react';
     import StudentProfile from './StudentProfile';
     import PerformanceMetrics from './PerformanceMetrics';
     import AttendanceList from './AttendanceList';

     const Dashboard = () => {
       const [studentData, setStudentData] = useState(null);

       useEffect(() => {
         fetch('http://localhost:5000/api/student-data')
           .then(response => response.json())
           .then(data => setStudentData(data));
       }, []);

       if (!studentData) return <div>Loading...</div>;

       return (
         <div className="container mt-4">
           <StudentProfile student={studentData.basic_details} />
           <PerformanceMetrics metrics={studentData.performance_metrics} />
           <AttendanceList attendance={studentData.weekly_attendance} />
         </div>
       );
     };

     export default Dashboard;