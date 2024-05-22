import React from 'react';

     const StudentProfile = ({ student }) => {
       return (
         <div className="card mb-4">
           <div className="card-body">
             <h2>{student.name}</h2>
             <p>Email: {student.email}</p>
             <p>Cohort: {student.cohort}</p>
             <p>Ranking: {student.ranking}</p>
           </div>
         </div>
       );
     };

     export default StudentProfile;