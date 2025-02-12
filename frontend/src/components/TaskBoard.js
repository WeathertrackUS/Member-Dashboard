import React, { useState, useEffect } from 'react';

const TaskBoard = () => {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState({ title: '', status: '', dueDate: '', comments: [] });

    useEffect(() => {
        // Fetch tasks from the backend
        const fetchTasks = async () => {
            const response = await fetch('/api/tasks');
            const data = await response.json();
            setTasks(data);
        };
        fetchTasks();
    }, []);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewTask({ ...newTask, [name]: value });
    };

    const handleAddTask = async () => {
        const response = await fetch('/api/tasks', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newTask),
        });
        const addedTask = await response.json();
        setTasks([...tasks, addedTask]);
        setNewTask({ title: '', status: '', dueDate: '', comments: [] });
    };

    return (
        <div>
            <h2>Task Board</h2>
            <div>
                <input
                    type="text"
                    name="title"
                    value={newTask.title}
                    onChange={handleInputChange}
                    placeholder="Task Title"
                />
                <input
                    type="text"
                    name="status"
                    value={newTask.status}
                    onChange={handleInputChange}
                    placeholder="Task Status"
                />
                <input
                    type="date"
                    name="dueDate"
                    value={newTask.dueDate}
                    onChange={handleInputChange}
                />
                <button onClick={handleAddTask}>Add Task</button>
            </div>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>
                        <h3>{task.title}</h3>
                        <p>Status: {task.status}</p>
                        <p>Due Date: {task.dueDate}</p>
                        <div>
                            <h4>Comments:</h4>
                            <ul>
                                {task.comments.map((comment, index) => (
                                    <li key={index}>{comment}</li>
                                ))}
                            </ul>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TaskBoard;