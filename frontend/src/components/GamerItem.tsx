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
         <div className="black__gamer-wrapper" id='black__gamer-wrapper'>
            {player.hands.map(hand =>
               <strong className="black__wrapper">
                  <p>{hand.bet}</p>
                  <div className="black__wrapper-cards">
                     {
                        hand.cards.map(card =>
                           <CardItem rank={card.rank} suit={card.suit}></CardItem>
                        )
                     }
                  </div>
               </strong>
            )}
         </div>
      </li>
   )
}

export default GamerItem