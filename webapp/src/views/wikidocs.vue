<template>
    <div>
        <WikiDoc 
        v-for="doc in docs" 
        :data="doc"
        :key="doc.id"
        >
        </WikiDoc>
    </div>
</template>

<script>
import WikiDoc from '@/components/Wikidoc.vue'
import {getdocs} from '@/api/docs.js'
export default {
    name:'wikidocs',
    components:{
        WikiDoc,
    },
    created() {
        this._getdocs()
    },
    data() {
        return {
            docs:[],
        }
    },
    methods: {
        _getdocs(){
            getdocs().then(
                (res)=>{
                    this.docs=res.data
                    console.log(res.data)
                }
            )
        }
    }
}
</script>
