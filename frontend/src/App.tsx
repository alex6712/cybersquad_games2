import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Header from './components/UI/Header';
import Auth from './pages/Auth';
import Blackjack from './pages/Blackjack';
import Main from './pages/Main';
import Poker from './pages/Poker';
import Registration from './pages/Registration';
import Roulett from './pages/Roulett';

const App: React.FC = () => {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Main />,
      children: [],
    },
    {
      path: "/auth",
      element: <Auth />,
      children: [],
    },
    {
      path: "/registration",
      element: <Registration />,
      children: [],
    },
    {
      path: "/poker",
      element: <Poker />,
      children: [],
    },
    {
      path: "/roulett",
      element: <Roulett />,
      children: [],
    },
    {
      path: "/blackjack",
      element: <Blackjack />,
      children: [],
    },
  ]);
  return (
    <div>
      <Header />
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
