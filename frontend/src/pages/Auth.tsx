import React from 'react'
import Myinput from '../components/UI/Myinput'
import '../styles/auth.css'

type Props = {}

const login = ''
const password = ''
const req = ''

// constructor(private router: Router, private service: AuthService) { }

function get_l() {
   // this.service.get_login(this.login, this.password).subscribe(value => {
   //    this.req = value
   //    if (this.req.response) {
   //       localStorage.setItem('nickname', this.login)
   //       localStorage.setItem('id', this.req.items[0].id)
   //       localStorage.setItem('key', this.req.items[0].key)
   //       this.router.navigate(['menu'])
   //    }
   // })
   window.location.href = '/'
}

function Auth({ }: Props) {
   return (
      <div className="auth">
         <a className="auth__back-link" href='/'>Назад</a>
         <div className="container">
            <div className="auth__wrapper">
               <form action="" className="auth__form">

                  <h2 className="auth__title">Войдите в аккаунт</h2>

                  <div className="auth__form-item">
                     <p className="auth__form-text">Логин</p>
                     <Myinput inp_type='text' />
                  </div>

                  <div className="auth__form-item">
                     <p className="auth__form-text">Пароль</p>
                     <Myinput inp_type='password' />
                  </div>

                  <div className="auth__form-item">
                     <button type="button" className="auth__form-btn" onClick={get_l}>Войти</button>
                  </div>

               </form>
            </div >
         </div >
      </div >
   )
}

export default Auth