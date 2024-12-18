import React from 'react';
import './App.css';
import Header from './components/Header';

function App() {
  return (
    <div className="App">
      <Header />
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <h2 className="text-4xl font-bold text-blue-600">Welcome to My Calendar App</h2>
      </div>
      
    </div>
  );
}

export default App;
