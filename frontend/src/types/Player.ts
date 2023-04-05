export type Player = {
   login: string,
   bet: number,
   id: number,
   state: string, // 'wait' or 'in_game' or 'play'
   hands: Hand[]
}

type Hand = {
   cards: Card[]
}

type Card = {
   rank: number,
   suit: string
}