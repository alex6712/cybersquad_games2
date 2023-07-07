import React from 'react'
import '../styles/header.css'
import { Link } from 'react-router-dom'

type Props = {}

function Header(props: Props) {

   let isAuth = false
   const nickname = 'player'

   function exit() {
      isAuth = !isAuth
      localStorage.removeItem('nickname')
      localStorage.removeItem('key')
      localStorage.removeItem('id')
      window.location.reload()
   }

   // ngOnInit(): void {
   //    let token = localStorage.getItem('key');
   //    this.nickname = localStorage.getItem('nickname');
   //    if (token) {
   //      this.isAuth = true;
   //    }
   //    else {
   //      this.isAuth = false;
   //    }
   //  }

   return (
      <header className="header">
         <div className="container">
            {isAuth
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