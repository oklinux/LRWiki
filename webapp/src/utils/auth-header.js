export function authHeader(){
    let token = JSON.parse(localStorage.getItem('token'));
    if(token && token.access){
        return{
            'Authorization':'Bearer '+ token.access
        }
    } else{
        return {};
    }
}