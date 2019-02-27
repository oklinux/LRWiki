<template>
    <div class="row">
        <sidebar/>
        <div class="col-lg-8 wikilist ">
        <WikiDoc 
        v-for="doc in docs" 
        :data="doc"
        :key="doc.id"
        >
        </WikiDoc>
        </div>
    </div>
</template>

<script>
import WikiDoc from '@/components/Wikidoc.vue'
import {getdocs} from '@/api/docs.js'
import sidebar from '@/components/sidebar.vue'
export default {
    name:'wikidocs',
    components:{
        WikiDoc,
        sidebar,
    },
    created() {
        this._getdocs()
    },
    mounted(){
        if(this._isMobile){
            console.log('is mobile')
        }else{
            console.log('not is mobile')
        }
        console.log(this.$mq)
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
        },
        _isMobile(){
            if(screen.width<450){
                return true
            }else{
                return false
            }
        }
    }
}
</script>
<style>
.wikilist{
    z-index: -1;
    float: left;
}
</style>
