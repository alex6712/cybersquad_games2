import React, { useEffect, useRef, useState } from 'react'
import CardItem from '../components/CardItem'
import cards from '../cards'
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

   // if (gamers ) {
   //    for (let i = 0; i < length_players; i++) {
   //       let el = gamers[i]
   //       const hui = -2 * Math.cos(Math.PI * i / (length_players - 1))
   //       el.style.top = Math.abs(Math.cos(toRadians((length_players / 2) * angle * hui)) * delta) + 'px'
   //       el.style.transform = `rotate(${-angle * hui}deg)`
   //    }
   // }
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
         name: 'Diler', score: 10, cards: [
            { name: 'heart_11', rank: 11, suit: 'heart' },
            { name: 'heart_7', rank: 7, suit: 'heart' }
         ]
      }
   )

   const [players, setPlayers] = useState([
      {
         name: 'Alexandr', id: 0, bid: 100, state: 'game', moving: true, cards: [
            { name: 'clover_3', rank: 3, suit: 'clover' },
            { name: 'heart_3', rank: 3, suit: 'heart' }
         ]
      },
      {
         name: 'Alex', id: 1, bid: 100, state: 'game', moving: false, cards: [
            { name: 'pike_14', rank: 14, suit: 'pike' },
            { name: 'tile_14', rank: 14, suit: 'tile' }
         ]
      },
      {
         name: 'Danil', id: 2, bid: 100, state: 'game', moving: false, cards: [
            { name: 'pike_2', rank: 2, suit: 'pike' },
            { name: 'pike_3', rank: 2, suit: 'pike' }
         ]
      },
      {
         name: 'Max', id: 3, bid: 100, state: 'game', moving: false, cards: [
            { name: 'clover_12', rank: 12, suit: 'clover' },
            { name: 'clover_13', rank: 13, suit: 'clover' }
         ]
      },
      {
         name: 'Nastya', id: 4, bid: 100, state: 'game', moving: false, cards: [
            { name: 'tile_4', rank: 4, suit: 'tile' },
            { name: 'clover_8', rank: 8, suit: 'clover' }
         ]
      },
   ])

   let my_game_id = 0

   startGame(players)
   useEffect(() => {
      fetchGamers(players)
   }, [players])

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
                        my_game_id != -1
                           ?
                           <>
                              <GamerItem player={players[my_game_id]}></GamerItem>
                              <div className="black__player-info">
                                 {
                                    players[my_game_id].moving
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
                           </>
                           : <div>Игрок с вашим my_game_id отсутствует в игре, либо у вас несуществующий
                              my_game_id</div>
                     }
                     {/* ФУНКЦИОНАЛЬНЫЕ КНОПКИ */}
                  </div>
                  : // DILER
                  <div className="black__table">
                     <div className="black__table-main">
                        <div className="black__table-wrapper">
                           {diler.cards.map((card) =>
                              <CardItem name={card.name} rank={card.rank} suit={card.suit}></CardItem>
                           )}
                        </div>
                        <h1 className='black__table-info'>{diler.score}</h1>
                     </div>

                     <>{
                        players.length != 0
                           ?
                           <ul className="black__playerslist" id='black__playerslist'>
                              {players.map(player =>
                                 <GamerItem player={player}></GamerItem>
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