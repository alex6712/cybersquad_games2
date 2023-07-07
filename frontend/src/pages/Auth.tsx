import React, { useState } from 'react'
import Myinput from '../components/UI/Myinput'
import '../styles/auth.css'
import Mylink from '../components/UI/Mylink'
import Mybtn from '../components/UI/Mybtn'
import AuthService from '../api/authService'
import axios from 'axios'

type Props = {}




function Auth({ }: Props) {
   const [login, setLogin] = useState<string>('')
   const [password, setPassword] = useState<string>('')

   const loginHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
      setLogin(event.target.value)
   }

   const passwordHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
      setPassword(event.target.value)
   }

   const loginPressHandler = (event: React.KeyboardEvent<HTMLInputElement>) => {
      if (event.key === 'Enter') {
         console.log(login, password)
      }
   }

   const sign_in = (login: string, password: string) => {
      const requestOptions = {
         method: 'POST',
         headers: { 'Content-Type': 'application/json' },
         body: JSON.stringify({ username: login, password })
      }
      // 127.0.0.1:8080/auth/sign_in
      console.log(
         fetch('http://google.conm', requestOptions)
            .then(res => res.json())
            .then(data => console.log(data))
      )
   }

   return (
      <div className="auth">
         <Mylink inp_href='/'>Назад</Mylink>
         <div className="container">
            <div className="auth__wrapper">
               <form action="" className="auth__form">

                  <h2 className="auth__title">Войдите в аккаунт</h2>

                  <div className="auth__form-item">
                     <p className="auth__form-text">Логин</p>
                     <Myinput inp_type='text' value={login} onChange={loginHandler} mykeypress={loginPressHandler} />
                  </div>

                  <div className="auth__form-item">
                     <p className="auth__form-text">Пароль</p>
                     <Myinput inp_type='password' value={password} onChange={passwordHandler} mykeypress={loginPressHandler} />
                  </div>

                  <div className="auth__form-item">
                     {/* <Mybtn inp_type='button' style={{ width: '100%' }} onClick={sign_in}>Войти</Mybtn> */}
                     <div style={{ width: '100%' }} onClick={e => sign_in(login, password)}>Войти</div>
                  </div>

               </form>
            </div >
         </div >
      </div >
   )
}

export default Auth