<template>
  <div class="row">
    <div class="col-lg-offset-2 col-lg-8 col-sm-offset-2 col-sm-8">
      <div v-html="docMarkdown"></div>
      <button v-if='doc.author === this.username' style="float : right;">
        <router-link :to="{name:'docsediter',params:{docid :this.docid}}">edit</router-link>
      </button>
    </div>
  </div>
</template>

<<script>
import marked from "marked";
import {getdoc} from '@/api/docs.js'
export default {
    name : 'DetailDoc',
    props :[
        'docid',
    ],
    data() {
        return {
            doc:[],
            docMarkdown:'',
            username:'',
        }
    },
    created() {
        console.log('created');
        this._getdoc(this.docid)
        if (this.$store.state.authentication.status.loggedIn){
            this.username = JSON.parse(localStorage.tokendata)['user_id'];
        }
    },
    methods: {
        _getdoc(_id){
            getdoc(_id).then(
                (res)=>{
                    this.docMarkdown =  marked(res.data.text, { sanitize: true });
                    this.doc = res.data;
                }
            )
        }
    },
}
</script>