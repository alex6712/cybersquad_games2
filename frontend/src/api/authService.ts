import axios from 'axios'

export default class AuthService {
   api = '192.168.1.94:8080'

   async login(login: any, password: any, formData: URLSearchParams) {
      return await axios.post('http://localhost:8080/auth/sign_in', formData)
         .then(res => {
            localStorage.setItem('access_token', res.data.access_token)
            return res.data
         })
         .catch(e => {
            console.log(e)
         })
   }

   async register(login: any, password: any) {
      return await axios.post('http://localhost:8080/auth/sign_up', { username: login, password })
         .then(res => {
            return res.data
         })
         .catch(e => {
            console.log(e)
         })
   }
}
