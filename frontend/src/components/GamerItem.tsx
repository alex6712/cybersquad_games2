import React from 'react'
import { Player } from '../types/Player'
import CardItem from './CardItem'

type Props = {
   player: Player
}

function GamerItem({ player }: Props) {
   let hands = player.hands
   return (
      <li className="black__gamer">
         <h1 className='black__info'><span>{player.login}</span> </h1>
         {player.hands.map(hand =>
            <div className="black__wrapper">
               <p>{hand.bet}</p>
               {
                  hand.cards.map(card =>
                     <CardItem rank={card.rank} suit={card.suit}></CardItem>
                  )
               }
            </div>
         )}
      </li>
   )
}

export default GamerItem