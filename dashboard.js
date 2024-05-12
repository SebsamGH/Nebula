document.addEventListener("DOMContentLoaded", function() {
    // Sample data for academic performance
    var academicData = {
        labels: ["Assignment 1", "Assignment 2", "Assignment 3", "Assignment 4"],
        datasets: [{
            label: "Grade",
            data: [85, 78, 92, 88],
            backgroundColor: 'rgba(0, 123, 255, 0.2)',
            borderColor: 'rgba(0, 123, 255, 1)',
            borderWidth: 1
        }]
    };

    // Sample data for weekly attendance
    var attendanceData = {
        labels: ["Week 1", "Week 2", "Week 3", "Week 4"],
        datasets: [{
            label: "Present",
            data: [4, 5, 4, 5],
            backgroundColor: 'rgba(40, 167, 69, 0.2)',
            borderColor: 'rgba(40, 167, 69, 1)',
            borderWidth: 1
        }, {
            label: "Absent",
            data: [1, 0, 1, 0],
            backgroundColor: 'rgba(255, 0, 0, 0.2)',
            borderColor: 'rgba(255, 0, 0, 1)',
            borderWidth: 1
        }]
    };

    // Render academic performance chart
    var academicChart = document.getElementById('academic-chart').getContext('2d');
    new Chart(academicChart, {
        type: 'bar',
        data: academicData,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

    // Render weekly attendance chart
    var attendanceChart = document.getElementById('attendance-chart');
    new Chart(attendanceChart, {
        type: 'bar',
        data: attendanceData,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});