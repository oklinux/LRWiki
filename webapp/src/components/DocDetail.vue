<template>
    <div>
        <h1>{{doc.title}}</h1>
        {{doc.text}}
    </div>
</template>

<<script>
import {getdoc} from '@/api/docs.js'
export default {
    name : 'DetailDoc',
    props :[
        'docid',
    ],
    data() {
        return {
            doc:[],
        }
    },
    created() {
        console.log('created');
        this._getdoc(this.docid)
    },
    methods: {
        _getdoc(_id){
            getdoc(_id).then(
                (res)=>{
                    this.doc = res.data
                    console.log(res.data)
                }
            )
        }
    },
}
</script>