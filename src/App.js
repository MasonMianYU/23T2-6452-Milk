import React from 'react';
import { MemoryRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Login from './pages/Login';
import Input from './pages/Input';
import Info from './pages/info';
import Product from './pages/Product';
import Adduser from './pages/Adduser';

const App = () => {
  return (
    <Router>
      <Link to="/"></Link>
      <Link to="/input"></Link>
      <Link to="/info"></Link>
      <Link to="/add"></Link>
      <Link to="/product"></Link>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/input" element={<Input />} />
        <Route path="/info" element={<Info />} />
        <Route path="/add" element={<Adduser />} />
        <Route path="/product" element={<Product />} />
      </Routes>
    </Router>
  );
};

export default App;
