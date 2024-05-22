import React from 'react';

const AttendanceList = ({ attendance }) => {
  return (
    <div className="card mb-4">
      <div className="card-body">
        <h3>Weekly Attendance</h3>
        <ul>
          {attendance.map((week, index) => (
            <li key={index}>
              Week {week.week_id}: {week.present_days} days present, {week.absent_days} days absent
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AttendanceList;