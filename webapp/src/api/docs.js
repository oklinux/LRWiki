import axios from 'axios'
import {HOST} from '@/common/config.js'

export function getdocs(){
    const url = HOST+'/api/doc/'
    return axios.get(url)
}

export function getdoc(docid){
    const url = HOST+'/api/doc/'+docid+'/'
    return axios.get(url)
}
export function postdoc(text){
    token = JSON.parse(localStorage.getItem('token'))['access']
    data = {
        'text':text,
    }
    const url = HOST+'/api/doc/'+docid+'/'
    return axios.post(
        url,
        data,
        {headers: {"Authorization":'Bearer ' + token}}
    )
}