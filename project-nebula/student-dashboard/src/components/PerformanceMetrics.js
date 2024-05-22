import React from 'react';

     const PerformanceMetrics = ({ metrics }) => {
       return (
         <div className="card mb-4">
           <div className="card-body">
             <h3>Performance Metrics</h3>
             <p>Assignments Completed: {metrics.assignment_completion}</p>
             <p>Attendance Average: {metrics.attendance_average}%</p>
           </div>
         </div>
       );
     };

     export default PerformanceMetrics;