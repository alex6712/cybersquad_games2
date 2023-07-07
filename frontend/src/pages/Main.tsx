import React, { useState } from 'react'
import Menuitem from '../components/Menuitem'

type Props = {}

export interface Game {
   id: number,
   name: string
}

const Main = (props: Props) => {
   const [menu_games, setGames] = useState([
      { id: 1, link: 'Poker', name: 'Покер' },
      { id: 2, link: 'Roulett', name: 'Рулетка' },
      { id: 3, link: 'Blackjack', name: 'Блекджек' }
   ])

   return (
      <div>
         <div className="container">
            <div className="main__wrapper">
               <h2 className="main__title">Добро пожаловать на наш маркетплейс игр, выберите одну из игр:</h2>
               <ul className="main__menu">
                  {menu_games.map((game) =>
                     <Menuitem key={game.id} id={game.id} name={game.name} link={game.link} />
                  )}
               </ul>
            </div >
         </div >
      </div>
   )
}
// tsrfce
export default Main