<template>
  <div class="row" style="margin-top:0">
    <div id="editormenu" class="col">
      <div  class="col col-lg-offset-1 col-lg-10 col-sm-offset-2 col-sm-8">
        <button class="button-primary button-purple" @click="submit()">提交</button>
        <button class="button-danger" @click="cleartext()">清空</button>
      </div>
    </div>
      <div id="editor" class="col col-lg-offset-1 col-lg-10 col-sm-offset-2 col-sm-8">
        <textarea :value="input" @input="update"></textarea>
        <div v-html="compiledMarkdown">
        </div>
      </div>
  </div>
</template>
<script>
import {postdoc} from '@/api/docs'
import marked from "marked";
import _ from "lodash";
export default {
  name: "doceditor",
  props: ["docdata"],
  data() {
    return {
      input: "hello"
    };
  },
  mounted(){
    if (this.docdata) {
      this.input=this.docdata
    }
  },
  computed: {
    compiledMarkdown: function() {
      return marked(this.input, { sanitize: true });
    }
  },
  methods: {
    update: _.debounce(function(e) {
      this.input = e.target.value;
    }, 300),
    cleartext(){
      this.input='hello'
    },
    submit(){
      postdoc(this.input).then(
        (res)=>
        console.log(res)
      )
    }
  }
};
</script>
<style lang="scss">
#editormenu {
  margin-bottom: 0;
  background-color: beige;

  button{
    float: right;
    margin-bottom: 0;
    margin-left: 1rem;
  }
}
#editor {
  height: 1000px;
  padding: 0%;
}
textarea, #editor div {
  display: inline-block;
  width: 49%;
  height: 100%;
  vertical-align: top;
  box-sizing: border-box;
  padding: 0 20px;
  background-color: #ccc;
  text-align: left;
  padding-top: 0;
  margin-left: 1%;
}
textarea {
  border: none;
  border-right: 1px solid #ccc;
  resize: none;
  outline: none;
  background-color: #f6f6f6;
  font-size: 14px;
  font-family: 'Monaco', courier, monospace;
  padding: 20px;
}
code {
  color: #f66;
}
</style>
