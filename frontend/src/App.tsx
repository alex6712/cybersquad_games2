import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Header from './components/Header';
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
      errorElement: <Main />
    },
    {
      path: "/auth",
      element: <Auth />,
      children: [],
      errorElement: <Main />
    },
    {
      path: "/registration",
      element: <Registration />,
      children: [],
      errorElement: <Main />
    },
    {
      path: "/poker",
      element: <Poker />,
      children: [],
      errorElement: <Main />
    },
    {
      path: "/roulett",
      element: <Roulett />,
      children: [],
      errorElement: <Main />
    },
    {
      path: "/blackjack",
      element: <Blackjack />,
      children: [],
      errorElement: <Main />
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
