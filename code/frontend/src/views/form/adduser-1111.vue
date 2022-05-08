<template>
  <div class="addstuinfo">
    <section class="form-container">
      <span class="title"> Add Student Information </span>
      <div>
        <el-form ref="addstinfoForm" :model="addstinfo" status-icon :rules="rules" label-width="160px" class="addstinfoForm">
          <el-row>
            <el-col :span="12">
              <el-form-item label="Name" prop="name">
                <el-input v-model="addstinfo.name" placeholder="Please input your name" />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="Skill Level" prop="skillLevel">
                <el-input v-model="addstinfo.skillLevel" placeholder="Please input your skillLevel" />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="12">
              <el-form-item label="Major" prop="major">
                <el-input v-model="addstinfo.major" placeholder="Please input your major" />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="Leadership Interest" prop="leadInt">
                <el-input v-model="addstinfo.leadInt" placeholder="Please input your leadership interest" />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="12">
              <el-form-item label="Grade" prop="grade">
                <el-select v-model="addstinfo.grade" placeholder="Please select your grade" >
                  <el-option value="Undergraduate">
                    Undergraduate
                  </el-option>
                  <el-option value="Graduate">
                    Graduate
                  </el-option>
                 </el-select> 
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="Field of Interests" prop="fieldInt">
                <el-input v-model="addstinfo.fieldInt" placeholder="Please input field of interests" />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="12">
              <el-form-item label="Type of End Product" prop="prod">
                <el-input v-model="addstinfo.prod" placeholder="Please input type of end product" />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="Related Experience" prop="exep">
                <el-input v-model="addstinfo.exep" placeholder="Please input your related experience" />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="12">
              <el-form-item label="Programming Language" prop="checkedLanguage">
                <el-checkbox-group v-model="addstinfo.checkedLanguage">
                    <el-row v-for="language in languages" :key="language">
                      <el-checkbox :label= "language" @change="languageChecked(language)"> {{language}} </el-checkbox>
                    </el-row>
                </el-checkbox-group>
                <el-input v-model="otherLanguage" placeholder="Others (if any)" />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="Who do you prefer to work with" prop="prefer">
                <el-input v-model="addstinfo.prefer" />
              </el-form-item>
              <el-form-item label="Who do you prefer NOT to work with" prop="preferNot">
                <el-input v-model="addstinfo.preferNot" />
              </el-form-item>
            </el-col> 
          </el-row>
          <el-form-item>
            <el-button type="primary" class="submit-btn" @click="onSubmitTxxx('addstinfoForm')">Submit</el-button>
          </el-form-item>
        </el-form> 
      </div> 
    </section>
  </div>
</template>

<script>
export default {
  name: 'txxx',
  data() {
    return {
      languages: ['C++', 'JAVA', 'Python'],
      otherLanguage: '',
      addstinfo: {
        name: '',
        skillLevel: '',
        major: '',
        leadInt: '',
        grade: '',
        fieldInt: '',
        prod: '',
        exep: '',
        checkedLanguage: [],
        prefer: '',
        preferNot: ''
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
        skillLevel: [
          {
            required: true,
            message: 'Skill level cannot be empty',
            trigger: 'blur'
          }
        ],
        major: [
          {
            required: true,
            message: 'Major cannot be empty',
            trigger: 'blur'
          }
        ],
        leadInt: [
          {
            required: true,
            message: 'Leadership interest cannot be empty',
            trigger: 'blur'
          }
        ],
        grade: [
          {
            required: true,
            message: 'Grade cannot be empty',
            trigger: 'blur'
          }
        ],
        fieldInt: [
          {
            required: true,
            message: 'Field of interests cannot be empty',
            trigger: 'blur'
          }
        ],
        prod: [
          {
            required: true,
            message: 'Type of end product cannot be empty',
            trigger: 'blur'
          }
        ],
        exep: [
          {
            required: true,
            message: 'Related experience cannot be empty',
            trigger: 'blur'
          }
        ],
        checkedLanguage: [
          {
            required: true,
            message: 'Programming language cannot be empty',
            trigger: 'blur'
          }
        ]
      },
      loading: false,
      redirect: undefined
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {
    languageChecked(language) {
      this.checkedLanguage = []
      this.checkedLanguage.push(language)
    },


    onSubmitTxxx(form) {
      if (this.otherLanguage.length !== 0){
        this.addstinfo.checkedLanguage.push(this.otherLanguage)
      }
      //console.log(this.addstinfo)
      this.loading = true
      // this.addstinfo
      this.$store.dispatch('user/addstinfo', this.addstinfo).then(() => {
        this.$router.push({ path: this.redirect || '/viewxx/index' }) // 跳转到查看页
        this.loading = false
      }).catch(() => {
        this.loading = false
      })
    },
    onCancel() {
      this.$message({
        message: 'cancel!',
        type: 'warning'
      })
    }
  }
}
</script>

<style scoped>
.addstuinfo {
  position: relative;
  width: 100%;
  height: 100%;
  /* background: url() no-repeat center center; */
  /* background-size: 100% 100%; */
}

.form-container {
  width: 80%;
  height: 210px;
  position: absolute;
  background-color: #fff;
  top: 5%;
  left: 10%;
  padding: 25px;
  border-radius: 5px;
  text-align: center;
}

.title {
font-family: 'Microsoft TaHei';
font-weight: bold;
font-size: 26px;
color: #C99700;
}

.addstinfoForm {
width: 100%;
margin-top: 20px;
padding: 20px 40px 20px 20px;
border-radius: 5px;
box-shadow: 0px 5px 10px #cccc;
}

.submit-btn {
width: 100%;
background-color: #72246C;
}

.line{
  text-align: center;
}
</style>


