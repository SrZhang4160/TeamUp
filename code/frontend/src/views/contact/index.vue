<template>
  <div class="stinfo-container">
      <h2 align="center">
    contact us
  </h2>

<el-collapse v-model="activeNames" @change="handleChange">
  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold"> Course info</div>
    </template>
<!--
    <div>If you need any help from the Instructor, please call {{contact_info.phone_number}} </div> -->

    <el-form label-position="top" ref="contact_info" :model="contact_info" status-icon :rules="rules" label-width="160px" class="contact_info">

      <el-row>
        <el-col :span="12">
          <el-form-item label="Instructor Name" prop="instructorName">
             {{contact_info.instructorName}}
          </el-form-item>
        </el-col>

        <el-col :span="12">
          <el-form-item label="Instructor Email" prop="instructorEmail">
            {{contact_info.instructorEmail}}
          </el-form-item>
        </el-col>
      </el-row>
      <el-divider></el-divider>
      <el-row>
        <el-col :span="22">
          <el-form-item label="ZoomLink" prop="zoomLink">
              {{contact_info.zoomLink}}
          </el-form-item>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="22">
          <el-form-item label="Officehour" prop="Officehour">
              <span v-for="certainoh in contact_info.officeHour" style="margin: 0px 10px 0px 0px;">{{certainoh.weekDay}} {{certainoh.start}} - {{certainoh.end}}        </span>
          </el-form-item>
        </el-col>
      </el-row>

      <el-divider></el-divider>
      <el-row>
          <el-form-item label="Ta info">
          </el-form-item>
      </el-row>


      <el-row>
        <el-col :span="22">
            <el-form-item
              class="Ta"
              v-for="(certain_Ta, index) in contact_info.Ta"
              :key="index"
              :prop="'Ta.' + index + '.value'"

            >
              <div>
                <el-row>
                  <el-col :span="12">
                      <b>Name</b> : {{certain_Ta.Name}}
                  </el-col>

                  <el-col :span="12">
                      <b>Email</b> : {{certain_Ta.Email}}
                  </el-col>
                </el-row>

                <el-row>
                  <b>Office hour</b> :
                  <span
                  v-for="(officeHour, index) in certain_Ta.officehour"
                  :key="index"
                  style="margin: 0px 10px 0px 0px;"
                  >
                  {{officeHour.weekDay}} {{officeHour.start}} - {{officeHour.end}}
                  </span>
                </el-row>
                <el-divider></el-divider>
              </div>
            </el-form-item>
        </el-col>
      </el-row>

    </el-form>




  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold"> How can I register as an instructor?</div>
    </template>
    <div>If you are an instructor, please email to {{email}} or call the IT help {{support}}</div>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold"> What if I encounter some IT problem?</div>
    </template>
    <div>If you encounter some IT problem, please contact IT help {{support}}</div>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold"> API reference</div>
    </template>
      Welcome to check our <a :href="api" target="_blank">API reference</a>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold"> Github</div>
    </template>
    Welcome to check our <a href="https://cs421sp22-homework.github.io/project-team-05-four-z-one-x/" target="_blank">github page</a>
   <div>Repository is <a :href="github" target="_blank">here</a></div>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold">User Manual</div>
    </template>
    <div>For more detail of how to use the app, please read <a :href="manual" target="_blank">this</a></div>
  </el-collapse-item>

  <el-collapse-item>
    <template slot="title" class = "title">
     <div style="font-weight:bold">Application document</div>
    </template>
     <div>For more detail of the idea of the app, please read <a :href="doc" target="_blank">this</a></div>
  </el-collapse-item>

</el-collapse>

<div v-if="isteacher == true" class="changebtn">
  <el-button class="button" @click="changeInfo()">change the course info here</el-button>
</div>

<div class = "darkblue_background">
  <el-footer>Designed by project-team-05-four-z-one-x</el-footer>
</div>

  </div>


</template>


<script>

import { contact_edit,contact_show } from '@/api/contact'
import { mapGetters } from "vuex";


export default {
  data() {
    return {
      isteacher:true,
      activeNames: ['1'],
      phone_number:'123456789',
      address:'johns hopkins',
      support:'12356789',
      api:'https://github.com/cs421sp22-homework/project-team-05-four-z-one-x/blob/main/docs/index.md',
      github:'https://github.com/cs421sp22-homework/project-team-05-four-z-one-x',
      doc:'https://docs.google.com/document/d/1-S7LHRFh2EkpVRNlLLsQ-gmJ5FrGmkZ_0Il53oyaK1w/edit#',
      manual:'https://docs.google.com/document/d/1BIOBSlkrhK4A-KTrATP1yNt82MWt9KnO0kNrsbVQAWM/edit',
      email:'aaa@jhu.edu',
      contact_info: {
          instructorName:'',
          instructorEmail:'',
          zoomLink:'',
          Ta:[{Name:'',Email:'',officehour:[{weekDay:'',start:'',end:''}]}],
          officeHour:[{weekDay:'',start:'',end:''}]

      },

    }
  },

  computed: {
    ...mapGetters(["name", "eml", "sex", "type", "avatar"]),
  },

  created() {
    if(this.type=="1"){
      this.isteacher=true

    }else{
      this.isteacher=false
    }

    this.fetchData()
  },
  methods: {
    fetchData() {
      contact_show().then(response => {
      this.contact_info = response.contactDetails;
    })
    },

  changeInfo()
  {
     this.$router.push('/editcontact/index')
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
.contact_info {
  width: 100%;
  margin-top: 0px;
  padding: 20px 20px 1px 20px;
  /* border-radius: 5px;
  box-shadow: 0px 5px 10px #cccc; */
}

.el-form-item {
  width: 100%;
  margin:0px 0px 0px 0px;
  padding: 0px 0px 1px 0px;
  /* border-radius: 5px;
  box-shadow: 0px 5px 10px #cccc; */
}
.changebtn{
  display: flex;
  justify-content: center;
}
.button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 10px 10px;
  margin: 10px;
  text-align: center;
  text-decoration: none;
  display: flex;
  justify-content: center;
  font-size: 16px;
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
    color: #9e9f98;
    text-align: center;
    line-height: 80px;
  }

</style>
