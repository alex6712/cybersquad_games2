export type Player = {
   login: string,
   id: number,
   state: string, // 'wait' or 'in_game' or 'play'
   hands: Hand[]
}

type Hand = {
   bet: number,
   cards: Card[]
}

type Card = {
   rank: number,
   suit: string
}