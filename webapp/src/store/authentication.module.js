import {userService} from '@/api/user.js'
import router from '@/router'

const token  = JSON.parse(localStorage.getItem('token'));
const initialState = token
    ? {status:{loggedIn:true},token}
    : {status:{},token:null}

export const authentication = {
    namespaced : true,
    state: initialState,
    actions: {
        login({commit},{username,password}){
            commit('loginRequest',{username});
            userService.login(username,password)
                .then(
                    token =>{
                        console.log('login successed')
                        commit('logginSuccess',token)
                        router.push('/')
                    },
                    error =>{
                        console.log('login failed')
                        console.log(error)
                        commit('logginFailure',error);
                    }
                )
        },
        logout({commit}){
            userService.logout()
            commit('logout')
        }
    },
    mutations:{
        loginRequest(state, token) {
            state.status = { loggingIn: true };
            state.token = token;
        },
        logginSuccess(state,token){
            state.status = { loggedIn: true };
            state.token = token;
        },
        logginFailure(state){
            state.status = {}
            state.status = null;
        },
        logout(state){
            state.status = {}
            state.token = null
        }
    }
}