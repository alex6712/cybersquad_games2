import React from 'react';
import Header from './components/Header';
import Auth from './pages/Auth';
import Blackjack from './pages/Blackjack';
import Main from './pages/Main';
import Poker from './pages/Poker';
import Registration from './pages/Registration';
import Roulett from './pages/Roulett';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';

const App: React.FC = () => {
  return (
    <div>
      <Router>
        <Header />

        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/auth" element={<Auth />} />
          <Route path="/registration" element={<Registration />} />
          <Route path="/blackjack" element={<Blackjack />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
