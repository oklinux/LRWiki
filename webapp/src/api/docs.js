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
    var token = JSON.parse(localStorage.getItem('token'))['access']
    var data = {
        'text':text,
    }
    const url = HOST+'/api/doc/'
    return axios.post(
        url,
        data,
        {headers: {"Authorization":'Bearer ' + token}}
    )
}
export function putdoc(docid,text){
    var token = JSON.parse(localStorage.getItem('token'))['access']
    var data = {
        'text':text,
    }
    const url = HOST+'/api/doc/'+docid+'/'
    return axios.put(
        url,
        data,
        {headers: {"Authorization":'Bearer ' + token}}
    )
}