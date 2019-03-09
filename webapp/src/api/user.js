import axios from 'axios'
import {Base64} from 'js-base64'
import {
  HOST
} from '@/common/config.js'
export const userService = {
  login,
  logout,
};

export function login(username, password) {
  const url = HOST + '/api/token/'
  const data = {
    'account': username,
    'password': password,
  }
  return axios.post(
    url,
    data, {
      headers: {
        'Content-Type': 'application/json'
      }
    }
  ).then(
    (res)=>{
      if (res.status==200){
        localStorage.setItem('token', JSON.stringify(res.data));
        localStorage.setItem('tokendata',resolvetoken(res.data))
      }
      return res.data
    }
  )
}
function logout(){
  localStorage.removeItem('token')
}
function resolvetoken(token){
  let token_meta_data = token['access']
  let [tokenhead,tokenpayload,signature] = token_meta_data.split('.')
  return Base64.decode(tokenpayload)
}