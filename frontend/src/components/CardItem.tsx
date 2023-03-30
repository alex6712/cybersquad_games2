import React from 'react'

type Props = {
   name: string,
   rank: number,
   suit: string
}

let card_rank = 0
let card_suit = ''

function CardItem({ name, rank, suit }: Props) {
   card_rank = rank
   card_suit = suit
   return (
      <div className='table__card'>
         <img src={require(`../assets/images/cards/${name}.png`)} alt={name} className="table__card-img" />
      </div>
   )
}

export default CardItem