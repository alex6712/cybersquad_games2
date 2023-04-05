import React from 'react'
import { Player } from '../types/Player'
import CardItem from './CardItem'

type Props = {
   player: Player
}

function GamerItem({ player }: Props) {
   return (
      <li className="black__gamer">
         <h1 className='black__info'><span>{player.name}</span> <span>{player.bid}</span></h1>
         <div className="black__wrapper">
            {player.cards.map((card) =>
               <CardItem name={card.name} rank={card.rank} suit={card.suit}></CardItem>
            )}
         </div>
      </li>
   )
}

export default GamerItem