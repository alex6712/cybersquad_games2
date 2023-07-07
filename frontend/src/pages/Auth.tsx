import React, { useState } from 'react'
import Myinput from '../components/UI/Myinput'
import '../styles/auth.css'
import Mylink from '../components/UI/Mylink'
import Mybtn from '../components/UI/Mybtn'
import AuthService from '../api/authService'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

type Props = {}

function Auth({ }: Props) {
   const [login, setLogin] = useState<string>('')
   const [password, setPassword] = useState<string>('')
   const navigate = useNavigate();
   let data: any | null = null
   const auth: AuthService = new AuthService()

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

   async function sign_in(login: string, password: string) {
      const formData = new URLSearchParams();
      formData.append('grant_type', 'password');
      formData.append('client_id', 'XXXX-app');
      formData.append('username', login);
      formData.append('password', password);

      data = await auth.login(login, password, formData)

      if (data.code === 200) {
         localStorage.setItem('isAuth', 'true')
         window.location.href = '/'
      }

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
                     <Mybtn inp_type='button' style={{ width: '100%' }} onClick={(e: any) => sign_in(login, password)}>Войти</Mybtn>
                  </div>

               </form>
            </div >
         </div >
      </div >
   )
}

export default Auth