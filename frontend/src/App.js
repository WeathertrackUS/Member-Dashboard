import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Calendar from './components/Calendar';
import Dashboard from './components/Dashboard';
import FileManager from './components/FileManager';
import TaskBoard from './components/TaskBoard';

function App() {
    return (
        <Router>
            <div>
                <Switch>
                    <Route path="/calendar" component={Calendar} />
                    <Route path="/dashboard" component={Dashboard} />
                    <Route path="/file-manager" component={FileManager} />
                    <Route path="/task-board" component={TaskBoard} />
                    <Route path="/" exact component={Dashboard} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;