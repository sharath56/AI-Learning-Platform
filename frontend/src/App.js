import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import CreateUser from './components/CreateUser';
import FaceRecognition from './components/FaceRecognition';
import MindMap from './components/MindMap';
import './index.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/create-user" element={<CreateUser />} />
        <Route path="/face-recognition" element={<FaceRecognition />} />
        <Route path="/mind-map" element={<MindMap />} />
      </Routes>
    </Router>
  );
}

export default App;
