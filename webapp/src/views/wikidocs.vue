<template>
    <div class="row">
        <sidebar/>
        <div class="col-lg-8 wikilist">
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
<style>
#wikilist{
    display: flex;
}
</style>
