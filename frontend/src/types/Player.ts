export type Player = {
   name: string,
   bid: number,
   id: number,
   state: string, // 'wait' or 'game'
   moving: boolean,
   cards: Card[]
}

type Card = {
   name: string,
   rank: number,
   suit: string
}