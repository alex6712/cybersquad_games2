import axios from 'axios'

export default class AuthService {
   api = '192.168.1.94:8080'

   login(login: any, password: any) {
      axios.post(this.api + '/auth/sign_in').then(res => {
         return res
      })
   }

   register(login: any, password: any) {
      axios.post(this.api + '/auth/sign_up').then(res => {
         return res
      })
   }
}
