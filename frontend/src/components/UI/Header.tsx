import React from 'react'
import '../../styles/header.css'

type Props = {}

function Header(props: Props) {

   const isAuth = false
   const nickname = 'player'

   function exit() {
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
                  <a className="header__link" href='/'>Главная</a>
                  <div className="header__link" >Приятной игры, {nickname}</div>
                  <a className="header__link" href='/' onClick={exit} >Выйти</a>
               </div>
               : <div className="header__wrapper">
                  <a className="header__link" href='/'>Главная</a>
                  <a className="header__link" href='/auth' >Авторизация</a>
                  <a className="header__link" href='/registration' >Регистрация</a>
               </div>
            }
         </div>
      </header>
   )
}

export default Header