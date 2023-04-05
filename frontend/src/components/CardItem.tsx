import React from 'react'

type Props = {
   rank: number,
   suit: string
}

let card_rank = 0
let card_suit = ''
let card_name = ''

function CardItem({ rank, suit }: Props) {
   card_rank = rank
   card_suit = suit
   card_name = card_suit + '_' + card_rank
   return (
      <div className='table__card'>
         <img src={require(`../assets/images/cards/${card_name}.png`)} alt={card_name} className="table__card-img" />
      </div>
   )
}

export default CardItem