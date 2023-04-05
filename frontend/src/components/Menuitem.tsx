import React from 'react'
import '../styles/main.css'

type Props = {}

function Menuitem(props: { id: number; name: string | undefined, link: string }) {

   const link = '/' + String(props.link?.toLowerCase())

   return (
      <div className='main__menu-item'>
         <a className='main__menu-link' href={link}>{props.name}</a>
      </div>
   )
}

export default Menuitem
