import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/student-dashboard" component={Dashboard} />
        {/* Add other existing routes here */}
      </Routes>
    </Router>
  );
};

export default App;