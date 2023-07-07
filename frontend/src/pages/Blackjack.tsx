import React, { useEffect, useRef, useState } from 'react'
import CardItem from '../components/CardItem'
import '../styles/blackjack.css'
import GamerItem from '../components/GamerItem'
import { Player } from '../types/Player'
import Mybtn from '../components/UI/Mybtn'
import Mylink from '../components/UI/Mylink'

type Props = {}

// создатель - стол
// остальные игроки
let gamer_type = 'player' // 'diler' / 'player'
let gamestate = 'Ожидание игроков...' // 'Ожидание игроков...' / 'ИГРА ИДЕТ'
let length_players: number
let angle: number
let screen_width: number
let screen_height: number
let delta: number

function toRadians(angle: number) {
   return angle * (Math.PI / 180);
}

function fetchGamers(players: Player[]) {
   length_players = players.length
   const wrapper_g = document.getElementById('black__playerslist')
   let gamers: NodeListOf<HTMLElement> | undefined
   if (wrapper_g)
      gamers = wrapper_g!.querySelectorAll('li')
   if (length_players != 0)
      gamestate = 'ИГРА ИДЕТ'
   else
      gamestate = 'Ожидание игроков...'
   if (length_players > 1 && wrapper_g)
      // wrapper_g.style.marginTop = `-${2 * length_players}em`
      wrapper_g.style.marginTop = `-10em`
   angle = 60 / length_players;
   screen_width = window.screen.width
   screen_height = window.screen.height
   delta = 2 / 9 * screen_height

   if (gamers && players.length < 6) {
      for (let i = 0; i < length_players; i++) {
         let el = gamers[i]
         const hui = -2 * Math.cos(Math.PI * i / (length_players - 1))
         el.style.top = Math.abs(Math.cos(toRadians((length_players / 2) * angle * hui)) * delta) + 'px'
         el.style.transform = `rotate(${-angle * hui}deg)`
      }
   } else {
      if (wrapper_g && gamers) {
         wrapper_g.style.display = 'flex';
         wrapper_g.style.flexWrap = 'wrap';
         wrapper_g.style.justifyContent = 'space-around'
         for (let i = 0; i < length_players; i++) {
            let el = gamers[i]
            el.style.width = `${100 / Math.ceil(length_players / 2)}%`
            el.style.marginBottom = '20px'
         }
      }
   }
}

function exitTable() {
   console.log(123)
}

function startGame(players: Player[]) {
   fetchGamers(players)
}

function isFirstMove(player: Player): boolean {
   /*
      @TODO
      Запрос на проверку, первый ли ход у данного игрока
   */
   return true
}

function get_one_card() {

}

function isIdenticalСards(player: Player): boolean {
   return true
}

function get_oneCard_doubleDown() {

}

function splitHands(player: Player) {

}

function isDilerAce(): boolean {
   return true
}

function fold() {

}

function insurance() {

}

function Blackjack({ }: Props) {
   const [diler, setDiler] = useState(
      {
         login: 'Diler', score: 10, hands: [
            { rank: 11, suit: 'heart' },
            { rank: 7, suit: 'heart' }
         ]
      }
   )

   const [players, setPlayers] = useState([
      {
         login: 'Alexandr', id: 0, state: 'play', hands: [
            {
               bet: 100,
               cards: [
                  { rank: 3, suit: 'clover' },
                  { rank: 3, suit: 'heart' }
               ]
            },
            {
               bet: 100,
               cards: [
                  { rank: 4, suit: 'clover' },
                  { rank: 5, suit: 'heart' }
               ]
            }
         ]
      },
      {
         login: 'Alex', id: 1, bet: 100, state: 'in_game', hands: [
            {
               bet: 100,
               cards: [
                  { rank: 14, suit: 'pike' },
                  { rank: 14, suit: 'tile' }
               ]
            },
            {
               bet: 100,
               cards: [
                  { rank: 4, suit: 'clover' },
                  { rank: 5, suit: 'heart' }
               ]
            }
         ]
      },
      {
         login: 'Danil', id: 2, bet: 100, state: 'in_game', hands: [
            {
               bet: 100,
               cards: [
                  { rank: 2, suit: 'pike' },
                  { rank: 2, suit: 'pike' }
               ]
            },
            {
               bet: 100,
               cards: [
                  { rank: 4, suit: 'clover' },
                  { rank: 5, suit: 'heart' }
               ]
            }
         ]
      },
      {
         login: 'Max', id: 3, bet: 100, state: 'in_game', hands: [
            {
               bet: 100,
               cards: [
                  { rank: 12, suit: 'clover' },
                  { rank: 13, suit: 'clover' }
               ]
            },
            {
               bet: 100,
               cards: [
                  { rank: 4, suit: 'clover' },
                  { rank: 5, suit: 'heart' }
               ]
            }
         ]
      },
      {
         login: 'Nastya', id: 4, bet: 100, state: 'in_game', hands: [
            {
               bet: 100,
               cards: [
                  { rank: 4, suit: 'tile' },
                  { rank: 8, suit: 'clover' }
               ]
            },
            {
               bet: 100,
               cards: [
                  { rank: 4, suit: 'clover' },
                  { rank: 5, suit: 'heart' }
               ]
            }
         ]
      },
   ])

   const [handCount, setHandCount] = useState(0)

   let my_game_id = 0

   const switchHands = (event: any, idx: number) => {
      const wrap = document.getElementById('black__gamer-wrapper')
      console.log(wrap)
      let hands: NodeListOf<HTMLElement> | undefined
      if (wrap) {
         hands = wrap.querySelectorAll('strong')
      }
      if (idx == 1 && hands) {
         console.log(1, idx, hands)
         hands[0].style.position = 'absolute'
         hands[0].style.transform = 'translateX(-100%)'

         hands[1].style.position = 'static'
         hands[1].style.transform = 'translateX(0%)'

         console.log(handCount)
         setHandCount(1)
         console.log(handCount)
      } else if (idx == 0 && hands) {
         console.log(0, idx, hands)
         hands[0].style.position = 'static'
         hands[0].style.transform = 'translateX(0%)'

         hands[1].style.position = 'absolute'
         hands[1].style.transform = 'translateX(100%)'

         console.log(handCount)
         setHandCount(0)
         console.log(handCount)
      }
      console.log(hands)
   }


   startGame(players)
   useEffect(() => {
      fetchGamers(players)
   }, [players])

   // useEffect(() => {
   //    switchHands(null, -1)
   //    console.log('useeffect', handCount)
   // }, [handCount])

   return (
      <div className='game_block'>
         <div className="back-links">
            <Mylink inp_href='/'>Назад</Mylink>
            <p className="back-gamestate">{gamestate}</p>
            {
               gamer_type == 'diler'
                  ? <Mybtn inp_type='button' disabled={!!length_players}
                     onClick={exitTable}>Закрыть стол</Mybtn>
                  : <></>
            }
         </div>

         <div className="black__main">
            {
               gamer_type == 'player'
                  ? // PLAYER
                  <div className="black__player">
                     {
                        players[my_game_id].state == 'in_game' || players[my_game_id].state == 'play'
                           ?
                           <>
                              <GamerItem key={players[my_game_id].login} player={players[my_game_id]}></GamerItem>
                              <div className="black__player-switches">
                                 <button
                                    className='black__player-switch'
                                    type='button'
                                    disabled={!handCount || players[my_game_id].hands.length == 1}
                                    onClick={e => switchHands(e, 0)}>
                                 </button>

                                 <button
                                    className='black__player-switch'
                                    type='button'
                                    disabled={!!handCount || players[my_game_id].hands.length == 1}
                                    onClick={e => switchHands(e, 1)}>
                                 </button>
                              </div>
                              {
                                 players[my_game_id].state == 'play'
                                    ?
                                    <div className="black__player-info">
                                       {
                                          players[my_game_id].state == 'play'
                                             ?
                                             <ul className="black__player-funclist">
                                                <li className="black__player-funcitem">
                                                   <Mybtn inp_type='button' style={{ width: '100%' }} onClick={get_one_card}>Взять еще 1 карту</Mybtn>
                                                </li>

                                                {
                                                   isFirstMove(players[my_game_id])
                                                      ?
                                                      <li className="black__player-funcitem">
                                                         <Mybtn inp_type='button' style={{ width: '100%' }} onClick={get_oneCard_doubleDown}>Взять 1 карту и удвоить ставку</Mybtn>
                                                      </li>
                                                      : <></>
                                                }

                                                {
                                                   isIdenticalСards(players[my_game_id])
                                                      ?
                                                      <li className="black__player-funcitem">
                                                         <Mybtn inp_type='button' style={{ width: '100%' }} onClick={splitHands}>Разделить на 2 руки</Mybtn>
                                                      </li>
                                                      : <></>
                                                }


                                                <li className="black__player-funcitem">
                                                   <Mybtn inp_type='button' style={{ width: '100%' }} onClick={fold}>Фолд</Mybtn>
                                                </li>

                                                {
                                                   isDilerAce()
                                                      ?
                                                      <li className="black__player-funcitem">
                                                         <Mybtn inp_type='button' style={{ width: '100%' }} onClick={insurance}>Страховка</Mybtn>
                                                      </li>
                                                      : <></>
                                                }

                                             </ul>
                                             : <></>
                                       }

                                    </div>
                                    : <></>
                              }

                           </>
                           : <div style={{ textAlign: "center" }}>Пожалуйста подождите, пока текущий игровой кон закончится</div>
                     }
                     {/* ФУНКЦИОНАЛЬНЫЕ КНОПКИ */}
                  </div>
                  : // DILER
                  <div className="black__table">
                     <div className="black__table-main">
                        <div className="black__table-wrapper">
                           {diler.hands.map((card) =>
                              <CardItem key={players[my_game_id].id} rank={card.rank} suit={card.suit}></CardItem>
                           )}
                        </div>
                        <h1 className='black__table-info'>{diler.score}</h1>
                     </div>

                     <>{
                        players.length != 0
                           ?
                           <ul className="black__playerslist" id='black__playerslist'>
                              {players.map(player =>
                                 <GamerItem key={players[my_game_id].id} player={player}></GamerItem>
                              )}
                           </ul>
                           : <div>ОЖИДАНИЕ ИГРОКОВ</div>
                     }</>
                  </div>
            }
         </div>
      </div>
   )
}

export default Blackjack