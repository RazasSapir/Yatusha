import './style/App.css';
import React from 'react';
import HomePage from './components/HomePage';
import Form from './components/Form'
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"

export default function App(){
    return (
      <div className="App">
        <Router>
          <Routes>
            <Route path="/" element={<HomePage/>} />
            <Route path="/form" element={<Form/>} />
          </Routes>
        </Router>
        {/* <footer className="app__footer">
                <p>כל הזכויות שמורות</p> 
                <a>ico1</a>
                <a>ico2</a>
                <a>ico3</a>
        </footer> */}
      </div>
    );
}
