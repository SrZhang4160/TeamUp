<template>
  <div class="stinfo-container">
      <h2 align="center">
    contact us
  </h2>

<el-collapse v-model="activeNames" @change="handleChange">
  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold"> Quick access numbers</div>
    </template>
    <div>If you need any help from the Instructor, please call {{contact_info.phone_number}} </div>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold"> How can I register as an instructor?</div>
    </template>
    <div>If you are an instructor, please email to {{contact_info.email}} or call the IT help {{contact_info.support}}</div>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold"> What if I encounter some IT problem?</div>
    </template>
    <div>If you encounter some IT problem, please contact IT help {{contact_info.support}}</div>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold"> API reference</div>
    </template>
      Welcome to check our <a :href="contact_info.api" target="_blank">API reference</a>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold"> Github</div>
    </template>
    Welcome to check our <a href="https://cs421sp22-homework.github.io/project-team-05-four-z-one-x/" target="_blank">github page</a>
   <div>Repository is <a :href="contact_info.github" target="_blank">here</a></div>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold">User Manual</div>
    </template>
    <div>For more detail of how to use the app, please read <a :href="contact_info.manual" target="_blank">this</a></div>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold">Application document</div>
    </template>
     <div>For more detail of the idea of the app, please read <a :href="contact_info.doc" target="_blank">this</a></div>
  </el-collapse-item>

</el-collapse>

<div class = "darkblue_background">
  <el-footer>Designed by project-team-05-four-z-one-x</el-footer>
</div>

  </div>

  
</template>


<script>
import { getstinfo_api,query_profile_api } from '@/api/stinfoapi'

export default {
  data() {
    return {
      activeNames: ['1'],
      contact_info: {
          phone_number:'123456789',
          address:'johns hopkins',
          support:'12356789',
          api:'https://github.com/cs421sp22-homework/project-team-05-four-z-one-x/blob/main/docs/index.md',
          github:'https://github.com/cs421sp22-homework/project-team-05-four-z-one-x',
          doc:'https://docs.google.com/document/d/1-S7LHRFh2EkpVRNlLLsQ-gmJ5FrGmkZ_0Il53oyaK1w/edit#',
          manual:'https://docs.google.com/document/d/1BIOBSlkrhK4A-KTrATP1yNt82MWt9KnO0kNrsbVQAWM/edit',
          email:'aaa@jhu.edu'
      },

    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
    },


    dateFormat: function(time) {
      var date = new Date(time)
      var year = date.getFullYear()
      // eslint-disable-next-line
      var month= date.getMonth()+1<10 ? "0" +(date.getMonth()+1) : date.getMonth()+1;
      // eslint-disable-next-line
      var day=date.getDate()<10 ? "0"+date.getDate() : date.getDate();
      return year + '-' + month + '-' + day
    }

  }
}
</script>

<style scoped>
.stinfoForm {
  width: 100%;
  margin-top: 20px;
  padding: 20px 20px 1px 20px;
  /* border-radius: 5px;
  box-shadow: 0px 5px 10px #cccc; */
}

.stinfo-container{
  width: 80%;
  margin:0 auto;
  margin-top: 40px;
  margin-bottom: 40px;
  padding: 20px 20px 2px 20px;
  border-radius: 5px;
  box-shadow: 0px 5px 10px #cccc;
    /* text-align: center; */
}
.title{
   font-weight:bold;
}
a{text-decoration:underline}

.el-footer {
    color: #333;
    text-align: center;
    line-height: 80px;
  }

</style>