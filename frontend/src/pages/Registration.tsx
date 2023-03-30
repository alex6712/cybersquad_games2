import React from 'react'
import Myinput from '../components/UI/Myinput'
import '../styles/auth.css'

type Props = {}

const login = ''
const password = ''
const password1 = ''
const req = ''

//   constructor(private router: Router, private service: AuthService) { }

function register() {
   //  this.service.register(this.login, this.password).subscribe(value => {
   //    this.req = value
   //    console.log(this.req)
   //    if (this.req.response) {
   //      this.router.navigate(['auth'])
   //    }
   //  })
   window.location.href = '/'
}

function Registration({ }: Props) {
   return (
      <div className="auth">
         <a className="auth__back-link" href='/'>Назад</a>
         <div className="container">
            <div className="auth__wrapper">
               <form action="" className="auth__form">

                  <h2 className="auth__title">Создайте аккаунт</h2>

                  <div className="auth__form-item">
                     <p className="auth__form-text">Логин</p>
                     <Myinput inp_type='text' />
                  </div>

                  <div className="auth__form-item">
                     <p className="auth__form-text">Пароль</p>
                     <Myinput inp_type='password' />
                  </div>

                  <div className="auth__form-item">
                     <p className="auth__form-text">Повторите пароль</p>
                     <Myinput inp_type='password' />
                  </div>

                  <div className="auth__form-item">
                     <button type="button" className="auth__form-btn" onClick={register}>Зарегестрироваться</button>
                  </div>

               </form>
            </div>
         </div>
      </div>
   )
}

export default Registration