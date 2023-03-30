import React, { useState } from 'react'
import CardItem from '../components/CardItem'
import cards from '../cards'
import '../styles/blackjack.css'

type Props = {}

// создатель - стол
// остальные игроки
let gamer_type = 'diler' // 'diler'

function toRadians(angle: number) {
   return angle * (Math.PI / 180);
}

function Blackjack({ }: Props) {
   const [diler, setDiler] = useState(
      {
         name: 'Diler', score: 10, cards: [
            { name: 'heart_11', rank: 11, suit: 'heart' },
            { name: 'heart_7', rank: 7, suit: 'heart' }
         ]
      }

   )

   const [players, setPlayers] = useState([
      {
         name: 'Alexandr', bid: 100, cards: [
            { name: 'clover_3', rank: 3, suit: 'clover' },
            { name: 'heart_3', rank: 3, suit: 'heart' }
         ]
      },
      {
         name: 'Alex', bid: 100, cards: [
            { name: 'pike_14', rank: 14, suit: 'pike' },
            { name: 'tile_14', rank: 14, suit: 'tile' }
         ]
      },
      {
         name: 'Danil', bid: 100, cards: [
            { name: 'pike_2', rank: 2, suit: 'pike' },
            { name: 'pike_3', rank: 2, suit: 'pike' }
         ]
      },
      {
         name: 'Max', bid: 100, cards: [
            { name: 'clover_12', rank: 12, suit: 'clover' },
            { name: 'clover_13', rank: 13, suit: 'clover' }
         ]
      },
      {
         name: 'Nastya', bid: 100, cards: [
            { name: 'tile_4', rank: 4, suit: 'tile' },
            { name: 'clover_8', rank: 8, suit: 'clover' }
         ]
      },
   ])

   const wrapper_g = document.getElementById('black__playerslist')
   let length_players = players.length
   let gamers
   if (wrapper_g)
      gamers = wrapper_g.querySelectorAll('li')

   const angle = 60 / length_players;

   const screen_width = window.screen.width
   const screen_height = window.screen.height
   const delta = 3 / 9 * screen_height

   if (gamers) {
      for (let i = 0; i < length_players; i++) {
         let el = gamers[i]
         const hui = -2 * Math.cos(Math.PI * i / (length_players - 1))
         el.style.top = Math.abs(Math.cos(toRadians((length_players / 2) * angle * hui)) * delta) + 'px'
         el.style.transform = `rotate(${-angle * hui}deg)`
      }
   }

   return (
      <div className='game_block'>
         <a className="back-link" href='/'>Назад</a>

         <div className="black__main">
            {
               gamer_type == 'player'
                  ? // PLAYER
                  <div className="black__player">
                     <img src="../assets/images/cards/joker.png" alt="jok" />
                  </div>
                  : // DILER
                  <div className="black__table">
                     <div className="black__table-main">
                        <div className="black__table-wrapper">
                           {diler.cards.map((card) =>
                              // <div className="">hui</div>
                              // <img src={cardd} alt="joker" />
                              <CardItem name={card.name} rank={card.rank} suit={card.suit}></CardItem>
                           )}
                        </div>
                        <h1 className='black__table-info'>{diler.score}</h1>
                     </div>
                     <ul className="black__playerslist" id='black__playerslist'>
                        {players.map(player =>
                           <li className="black__playerslist-gamer">
                              <h1 className='black__playerslist-info'><span>{player.name}</span> <span>{player.bid}</span></h1>
                              <div className="black__playerslist-wrapper">
                                 {player.cards.map((card) =>
                                    <CardItem name={card.name} rank={card.rank} suit={card.suit}></CardItem>
                                 )}
                              </div>
                           </li>
                        )}
                     </ul>
                  </div>
            }
         </div>
      </div>
   )
}

export default Blackjack