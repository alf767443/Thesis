import logo from './logo.svg';
import React  from 'react';
import './App.css';
import { 
  HomeClass
} from './Pages/Home/Home';
import { 
  DepartmentClass 
} from './Pages/Department/Department';
import { 
  BrowserRouter as Router, 
  Route, 
  Routes, 
  NavLink
} from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App container">
        <h1 className= "d-flex justify-content-center m-3">
          React JS Frontend
        </h1>

        <nav className="navbar navbar-expand-sm bg-light navbar-dark">
          <ul className="navbar-nav">
            <li className="nav-item m1">
              <NavLink className="btn btn-light btn-outline-primary" to="/home">
                Home
              </NavLink>
            </li>
            <li className="nav-item m1">
              <NavLink className="btn btn-light btn-outline-primary" to="/department">
                Department
              </NavLink>
            </li>
          </ul>
        </nav>
        
        <Routes>
          <Route path="/home" element={<HomeClass/>}/>
          <Route path="/department" element={<DepartmentClass/>}/>
        </Routes>
        
      </div>
    </Router>
  );
}

export default App;
