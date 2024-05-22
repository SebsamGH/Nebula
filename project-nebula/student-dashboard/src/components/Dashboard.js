import React, { useEffect, useState } from 'react';
import StudentProfile from './StudentProfile';
import PerformanceMetrics from './PerformanceMetrics';
import AttendanceList from './AttendanceList';

const Dashboard = () => {
  const [studentData, setStudentData] = useState({
    basic_details: {
      name: 'Samuel Sebbie',
      email: 'sebsamstudio@gmail.com',
      cohort: 'Cohort 1',
      ranking: 1,
    },
    performance_metrics: {
      assignment_completion: 10,
      attendance_average: 95,
    },
    weekly_attendance: [
      { week_id: 1, present_days: 5, absent_days: 0 },
      { week_id: 2, present_days: 4, absent_days: 1 },
      // Add more mock data as needed
    ],
  });

  return (
    <div className="container mt-4">
      <StudentProfile student={studentData.basic_details} />
      <PerformanceMetrics metrics={studentData.performance_metrics} />
      <AttendanceList attendance={studentData.weekly_attendance} />
    </div>
  );
};

export default Dashboard;