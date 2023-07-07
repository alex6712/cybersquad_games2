import React, { useEffect } from 'react'
import '../styles/header.css'
import { Link } from 'react-router-dom'
import AuthService from '../api/authService'

type Props = {}

function Header(props: Props) {

   let isAuth = localStorage.getItem('isAuth')
   const nickname = 'player'

   useEffect(() => {
      isAuth = localStorage.getItem('isAuth')
   }, [, isAuth])


   function exit() {
      isAuth = 'false'
      localStorage.setItem('isAuth', 'false')
      localStorage.removeItem('nickname')
      localStorage.removeItem('key')
      localStorage.removeItem('id')
      window.location.reload()
   }

   return (
      <header className="header">
         <div className="container">
            {isAuth === 'true'
               ? <div className="header__wrapper">
                  <Link className="header__link" to={`/`}>Главная</Link>
                  <div className="header__link" >Удачи, {nickname}</div>
                  <Link className="header__link" to={`/`} onClick={exit}>Выйти</Link>
               </div>
               : <div className="header__wrapper">
                  <Link className="header__link" to={`/`}>Главная</Link>
                  <Link className="header__link" to={`/auth`}>Авторизация</Link>
                  <Link className="header__link" to={`/registration`}>Регистрация</Link>
               </div>
            }
         </div>
      </header>
   )
}

export default Header