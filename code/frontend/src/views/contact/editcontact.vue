<template>
  <div class="contact_info" >
    <section class="form-container">
      <div class="title"> Update Course Information </div>
      <div>
        <el-form label-position="top" ref="contact_info" :model="contact_info" status-icon :rules="rules" label-width="160px" class="contact_info">

          <el-row>
            <el-col :span="12">
              <el-form-item label="Instructor Name" prop="instructorName">
                <el-input v-model="contact_info.instructorName" style="width: 90%;"  placeholder="Please input your name" />
              </el-form-item>
            </el-col>

            <el-col :span="12">
              <el-form-item label="Instructor Email" prop="instructorEmail">
                <el-input v-model="contact_info.instructorEmail" style="width: 90%;" placeholder="Please input your email" />
              </el-form-item>
            </el-col>
          </el-row>




          <el-row>
            <el-col :span="22">
              <el-form-item label="ZoomLink" prop="zoomLink">
                  <el-input v-model="contact_info.zoomLink" style="width: 95%;" placeholder="Please input zoomlink for classes" />
              </el-form-item>
            </el-col>
          </el-row>

            <el-form-item label="Office Hour"></el-form-item>

            <el-row>
              <el-form-item
              class="Time"
              v-for="(certainofficehour, index) in contact_info.officeHour"
              :key="index"
              :prop="'Ta.' + index + '.value'"
              >
                  <el-col :span="12">
                    <el-select v-model="certainofficehour.weekDay" style="margin: 5px  5px  5px 0px; width: 90%;" placeholder="choose a weekday">
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                        :rules="{
                  required: true, message: 'officehour can not be empty', trigger: 'blur'
                }"
                        >
                      </el-option>
                    </el-select>
                  </el-col>

                  <el-col :span="12">
                    <el-time-select
                        placeholder="start time"
                        style="margin: 5px  5px  5px 0px; width: 40%;"
                        v-model="certainofficehour.start"
                        :picker-options="{
                        start: '08:00',
                        step: '00:15',
                        end: '20:00'
                        }">
                    </el-time-select>
                    <el-time-select
                        placeholder="end time"
                        style="margin: 5px; width: 40%;"
                        v-model="certainofficehour.end"
                        :picker-options="{
                        start: '08:15',
                        step: '00:15',
                        end: '20:00',
                        minTime: certainofficehour.start
                        }">
                    </el-time-select>
                     <el-button icon="el-icon-delete" circle @click.prevent="removeofficehour_admin(certainofficehour)"></el-button>
                  </el-col>
              </el-form-item>

            </el-row>
            <div class="add_btn" >
            <el-button type="primary" @click="addofficehour_admin()" >Add another officehour time</el-button>
            </div>

          <br />
          <br />
          <br />
          <el-form-item label="Ta Info"/>
          <el-divider></el-divider>
          <el-form-item
            class="Ta"
            v-for="(certain_Ta, index) in contact_info.Ta"
            :key="index"
            :prop="'Ta.' + index + '.value'"
            :rules="{
              required: true, message: 'Ta can not be empty', trigger: 'blur'
            }"
          >
          <div class="deleteTa">
          <el-button type="danger" @click.prevent="removeTa(certain_Ta)">Remove this Ta's info</el-button>
          </div>

            <el-row style="margin: 0px  0px  15px 0px;">
              <el-col :span="12">
                <!-- <el-input v-model="skill_level.skill"></el-input> -->
                <el-form-item label="Ta Name" prop="TaName">
                    <el-input v-model="certain_Ta.Name" style="width: 90%;"  placeholder="Please input Ta's name" />
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="Ta Email" prop="instructorEmail">
                    <el-input v-model="certain_Ta.Email" style="width: 90%;"  placeholder="Please input Ta's email" />
                </el-form-item>
              </el-col>
            </el-row>


            <el-form-item label="Officehour"/>

            <el-row>
              <el-form-item
              class="Time"
              v-for="(certainofficehour, index) in certain_Ta.officehour"
              :key="index"
              :prop="'Ta.' + index + '.value'"
              >
                  <el-col :span="12">
                    <el-select v-model="certainofficehour.weekDay" style="margin: 5px  5px  5px 0px; width: 90%;" placeholder="choose a weekday">
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                        :rules="{
                  required: true, message: 'officehour can not be empty', trigger: 'blur'
                }"
                        >
                      </el-option>
                    </el-select>
                  </el-col>

                  <el-col :span="12">
                    <el-time-select
                        placeholder="start time"
                        style="margin: 5px  5px  5px 0px; width: 40%;"
                        v-model="certainofficehour.start"
                        :picker-options="{
                        start: '08:00',
                        step: '00:15',
                        end: '20:00'
                        }">
                    </el-time-select>
                    <el-time-select
                        placeholder="end time"
                        style="margin: 5px; width: 40%;"
                        v-model="certainofficehour.end"
                        :picker-options="{
                        start: '08:15',
                        step: '00:15',
                        end: '20:00',
                        minTime: certainofficehour.start
                        }">
                    </el-time-select>
                     <el-button icon="el-icon-delete" circle @click.prevent="removeofficehour(certain_Ta,certainofficehour)"></el-button>
                  </el-col>

              </el-form-item>
            </el-row>
            <div class="add_btn" >
            <el-button type="primary" @click="addofficehour(certain_Ta)" >Add another officehour time</el-button>
            </div>
          <el-divider></el-divider>




          </el-form-item>
          <el-button type="primary" @click="addTa" class="add_btn">Add more Ta</el-button>




          <el-form-item style="text-align: center;">
            <el-button type="primary" class="submit-btn" @click="onSubmitTxxx('addstinfoForm')">Save</el-button>
            <el-button @click="resetForm('addstinfoForm')" >reset</el-button>
          </el-form-item>


        </el-form>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { contact_edit,contact_show } from '@/api/contact'




export default {

  data() {
    return {
        options: [{
          value: 'Monday',
          label: 'Monday'
        }, {
          value: 'Tuesday',
          label: 'Tuesday'
        }, {
          value: 'Wednesday',
          label: 'Wednesday'
        }, {
          value: 'Thuesday',
          label: 'Thuesday'
        }, {
          value: 'Friday',
          label: 'Friday'
        }],


      contact_info: {
          instructorName:'',
          instructorEmail:'',
          zoomLink:'',
          Ta:[{Name:'',Email:'',officehour:[{weekDay:'',start:'',end:''}]}],
          officeHour:[{weekDay:'',start:'',end:''}],

      },

      rules: {
        name: [
          {
            required: true,
            message: 'Username cannot be empty',
            trigger: 'blur'
          },
          {
            max: 16,
            message: 'Name cannot be longer than 16 characters',
            trigger: 'blur'
          }
        ],
      },
      loading: false,
      redirect: undefined
    }
  },
  computed: {
    ...mapGetters([
      'name', 'eml', 'sex', 'type', 'avatar'
    ])
  },

  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },

//   mounted: function() {
//     // this.testGomain()
//   },


  created() {
    console.log("update page")
    this.fetchData()
  },


  methods: {
    fetchData() {
      contact_show().then(response => {
        console.log("fetch success!!!!!")
        this.contact_info = response.contactDetails
        // console.log(this.stinfo)
      })
    },

    // querySearch(queryString, cb) {
    //   var skills_list = this.skills_list;
    //   var results = queryString ? skills_list.filter(this.createFilter(queryString)) : skills_list;
    //   // callback to get the skill list filtered
    //   cb(results);
    // },
    // createFilter(queryString) {
    //   return (skill_list) => {
    //     return (skill_list.skill.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
    //   };
    // },


    resetForm(formName) {
      this.$refs[formName].resetFields();
    },


    addTa(){
      this.contact_info.Ta.push({
        Name:'',
        Email:'',
        officehour:[{weekDay:'',start:'',end:''}]
      })
    },

    removeTa(certain_Ta){
      var index = this.contact_info.Ta.indexOf(certain_Ta)
      if (index !== -1) {
        this.contact_info.Ta.splice(index, 1)
      }
    },

    addofficehour(certain_Ta) {
      certain_Ta.officehour.push({
        weekDay:'',
        start:'',
        end:''
      })
    },

    removeofficehour(certain_Ta,certainofficehour){
      var index = certain_Ta.officehour.indexOf(certainofficehour)
      if (index !== -1) {
        certain_Ta.officehour.splice(index, 1)
      }
    },



    addofficehour_admin() {
      this.contact_info.officeHour.push({
        weekDay:'',
        start:'',
        end:''
      })
    },

    removeofficehour_admin(certainofficehour){
      var index = this.contact_info.officehour.indexOf(certainofficehour)
      if (index !== -1) {
        this.contact_info.officehour.splice(index, 1)
      }
    },

    languageChecked(language) {
      this.checkedLanguage = []
      this.checkedLanguage.push(language)
    },

    onSubmitTxxx(form) {

      this.loading = true
      let params = {
        instructorName:this.contact_info.instructorName,
        instructorEmail:this.contact_info.instructorEmail,
        zoomLink:this.contact_info.zoomLink,
        Ta:this.contact_info.Ta,
        officeHour:this.contact_info.officeHour,

      }
      console.log(params)
      contact_edit(params).then(res=>{
          if(res.code==1){
              this.loading = true
              this.$message.success(res.msg)
              this.$router.push('/contact/index')
          }else{
              this.$message.success(res.msg)
          }
      })

    },
    onCancel() {
      this.$message({
        message: 'cancel!',
        type: 'warning'
      })
    },
    // testGomain() {
    //   console.log('TXXX' + this.type)
    //   if (this.type !== 0) {
    //     this.$router.push('/')
    //   }
    // }
  }
}
</script>

<style>


.interest_container{
width: 40%;
margin-right: 20px;
}

.add_btn{
margin: 30px 10px 10px 10px;
text-align: center;
display: flex;
justify-content: center;
font-size: 16px;
}

.deleteTa{
  text-align: right;

}

.form-container {
  width: 80%;
  /* height: 210px; */
  position: relative;
  background-color: #fff;
  top: 5%;
  left: 10%;
  padding: 25px;
  border-radius: 5px;
  /* text-align: center; */
}

.title {
font-family: 'Microsoft TaHei';
font-weight: bold;
font-size: 26px;
color: #C99700;
margin-bottom: 20px;
}

.addstinfoForm {
width: 100%;
margin-top: 20px;
padding: 20px 20px 20px 20px;
border-radius: 5px;
box-shadow: 0px 5px 10px #cccc;
}

.submit-btn {
/* width: 100%; */
margin-top: 30px;
background-color: #409EFF;
text-align: center;
}

.line{
  text-align: center;
}
</style>
