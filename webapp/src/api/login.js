import axios from 'axios'
import {HOST} from '@/common/config.js'

export function login(username,password){
    const url = HOST+'token/'
    const data = {
        'account':username,
        'password':password,
    }
    axios.post
}