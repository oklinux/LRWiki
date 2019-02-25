import axios from 'axios'
import {HOST} from '@/common/config.js'

export function login(username,password){
    const url = HOST+'token/'
    const data = {
        'username':username,
        'password':password,
    }
    axios.post
}