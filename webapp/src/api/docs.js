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
