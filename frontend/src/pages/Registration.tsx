import React, { useState } from 'react'
import Myinput from '../components/UI/Myinput'
import '../styles/auth.css'
import Mybtn from '../components/UI/Mybtn'
import Mylink from '../components/UI/Mylink'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import AuthService from '../api/authService'

type Props = {}


function Registration({ }: Props) {
   const [login, setLogin] = useState<string>('')
   const [password, setPassword] = useState<string>('')
   const [password2, setPassword2] = useState<string>('')
   const navigate = useNavigate();
   let data: any | null = null
   const auth: AuthService = new AuthService()

   const loginHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
      setLogin(event.target.value)
   }

   const passwordHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
      setPassword(event.target.value)
   }

   const passwordHandler2 = (event: React.ChangeEvent<HTMLInputElement>) => {
      setPassword2(event.target.value)
   }

   const loginPressHandler = (event: React.KeyboardEvent<HTMLInputElement>) => {
      if (event.key === 'Enter') {
         console.log(login, password)
      }
   }

   async function register(login: string, password: string) {

      if (password === password2) {
         data = await auth.register(login, password)
      }

      if (data.code === 201) {
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

                  <h2 className="auth__title">Создайте аккаунт</h2>

                  <div className="auth__form-item">
                     <p className="auth__form-text">Логин</p>
                     <Myinput inp_type='text' value={login} onChange={loginHandler} mykeypress={loginPressHandler} />
                  </div>

                  <div className="auth__form-item">
                     <p className="auth__form-text">Пароль</p>
                     <Myinput inp_type='password' value={password} onChange={passwordHandler} mykeypress={loginPressHandler} />
                  </div>

                  <div className="auth__form-item">
                     <p className="auth__form-text">Повторите пароль</p>
                     <Myinput inp_type='password' value={password2} onChange={passwordHandler2} mykeypress={loginPressHandler} />
                  </div>

                  <div className="auth__form-item">
                     <Mybtn inp_type='button' style={{ width: '100%' }} onClick={(e: any) => register(login, password)}>Зарегестрироваться</Mybtn>
                  </div>

               </form>
            </div>
         </div>
      </div>
   )
}

export default Registration