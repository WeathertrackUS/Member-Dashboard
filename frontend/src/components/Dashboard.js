import React from 'react';

const Dashboard = () => {
    return (
        <div className="dashboard">
            <h1>Team Dashboard</h1>
            <div className="schedule">
                <h2>Team Schedules</h2>
                {/* Schedule display will go here */}
            </div>
            <div className="tasks">
                <h2>Tasks</h2>
                {/* Task list will go here */}
            </div>
        </div>
    );
};

export default Dashboard;