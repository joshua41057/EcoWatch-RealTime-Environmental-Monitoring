// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Charts from './components/Charts';
import Alerts from './components/Alerts';

const App = () => {
  return (
      <Router>
        <div>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/charts" element={<Charts />} />
            <Route path="/alerts" element={<Alerts />} />
          </Routes>
        </div>
      </Router>
  );
};

export default App;
