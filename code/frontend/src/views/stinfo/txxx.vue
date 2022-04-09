<template>
  <div class="addstuinfo" style="height: 850px;overflow-y: scroll;">
    <section class="form-container">
      <span class="title" > Add Student Information </span>
      <div>
        <el-form label-position="top" ref="addstinfoForm" :model="addstinfo" status-icon :rules="rules" label-width="160px" class="addstinfoForm">

          <el-row>
            <el-col :span="12">
              <el-form-item label="Name" prop="name">
                <el-input v-model="addstinfo.name" style="width: 90%;"  placeholder="Please input your name" />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="Major" prop="major">
                <el-input v-model="addstinfo.major" style="width: 90%;" placeholder="separate by comma if multiple majors" />
              </el-form-item>
            </el-col>
          </el-row>

          <el-row>
            <el-col :span="12">
              <el-form-item label="Grade" prop="grade">
                <el-select v-model="addstinfo.grade" placeholder="Please select your grade" style="width: 90%;">
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
              <el-form-item label="Leadership Interest" prop="leadInt">
                <el-select v-model="addstinfo.leadInt" placeholder="Please input your leadership interest" style="width: 90%;">
                  <el-option label="Low" value="Low"></el-option>
                  <el-option label="Medium" value="Medium"></el-option>
                  <el-option label="High" value="High"></el-option>
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>

          <el-row>
            <el-col :span="12">
              <el-form-item label="Type of End Product" prop="prod">
                <el-select v-model="addstinfo.prod" placeholder="Please input type of end product" style="width: 90%;">
                <el-option label="Web" value="Web"></el-option>
                <el-option label="iOS" value="iOS"></el-option>
                <el-option label="Android" value="Android"></el-option>
                <el-option label="Other" value="Other"></el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="Related Experience" prop="exep">
                <el-select v-model="addstinfo.exep" placeholder="Please input your related experience" style="width: 90%;">
                <el-option label="Work Experience" value="Work Experience"></el-option>
                <el-option label="Internship" value="Internship"></el-option>
                <el-option label="Class Project" value="Class Project"></el-option>
                <el-option label="None" value="None"></el-option>
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>


          <el-row>
            <el-col :span="22">
                <el-form-item
                  class="interest_item"
                  v-for="(interest, index) in addstinfo.fieldInt"
                  :label="'Field of Interest' + index"
                  :key="index"
                  :prop="'fieldInt.' + index + '.value'"
                  :rules="{
                    required: true, message: 'Field of Interests can not be empty', trigger: 'blur'
                  }"
                >
                  <!-- <el-input v-model="skill_level.skill"></el-input> -->
                  <el-select v-model="addstinfo.fieldInt[index]" filterable placeholder="Please input field of interests" class="interest_container">
                    <el-option
                      v-for="item in interests_list"
                      :key="item.value"
                      :label="item.interest"
                      :value="item.value"
                      :rules="{
                    required: true, message: 'Field of Interests can not be empty', trigger: 'blur'
                  }"
                    >
                    </el-option>
                  </el-select>

                  <!-- <el-input v-model="skill_level.level"></el-input> -->
                  <el-button icon="el-icon-delete" circle @click.prevent="removeInterest(interest)"></el-button>
                </el-form-item>
                <el-button type="primary" @click="addInterest" class="add_btn">Add more interest</el-button>
            </el-col>
          </el-row>


          <el-row>
            <el-col :span="22">
              <!-- <el-form-item label="Skill Level" prop="skillLevel">
                <el-input v-model="addstinfo.skillLevel" placeholder="Please input your skillLevel" />
              </el-form-item> -->

                <el-form-item
                  v-for="(skill_level, index) in addstinfo.skillLevel"
                  :label="'skill' + index"
                  :key="skill_level.key"
                  :prop="'skillLevel.' + index"
                  :rules="{
                    required: true, message: 'skill can not be empty', trigger: 'blur'
                  }"
                >
                  <!-- <el-input v-model="skill_level.skill"></el-input> -->
                  <el-autocomplete
                    class="interest_container"
                    v-model="skill_level.skillName"
                    :fetch-suggestions="querySearch"
                    placeholder="input your skill"
                    @select="handleSelect"
                    :rules="{
                    required: true, message: 'skill can not be empty', trigger: 'blur'
                  }"
                  ></el-autocomplete>


                    <el-select v-model="skill_level.level"
                      placeholder="input your level"
                      class="interest_container"
                      :rules="{
                    required: true, message: 'level can not be empty', trigger: 'blur'
                  }"
                      >
                      <el-option label="Low" value="Low"></el-option>
                      <el-option label="Medium" value="Medium"></el-option>
                      <el-option label="High" value="High"></el-option>
                    </el-select>

                  <!-- <el-input v-model="skill_level.level"></el-input> -->
                  <el-button icon="el-icon-delete" circle @click.prevent="removeSkill(skill_level)"></el-button>

                </el-form-item>
                <el-button type="primary" @click="addSkill" class="add_btn" >Add more skill</el-button>
            </el-col>
          </el-row>

          <el-row>
            <el-col :span="22">
              <el-form-item label="Who do you prefer to work with" prop="prefer">
                <el-input v-model="addstinfo.prefer" placeholder="Input email, limited to one person" type="textarea" />
              </el-form-item>
            </el-col>
          </el-row>

          <el-row>
            <el-col :span="22">
              <el-form-item label="Who do you prefer NOT to work with" prop="preferNot">
                <el-input v-model="addstinfo.preferNot" placeholder="Input email, limited to one person" type="textarea" />
              </el-form-item>
            </el-col>
          </el-row>

          <el-row>
            <el-col :span="22">
              <el-form-item label="What is your mbti personality?" prop="mbti">
                <el-input v-model="addstinfo.mbti" placeholder="Input 5 letters result. e.g. INFP-T"/>
              </el-form-item>
            </el-col>
          </el-row>
          <div style="font-size: small; margin-bottom: 20px;">For more detail of mbti test, please go to <a href="https://www.16personalities.com/" target="_blank">https://www.16personalities.com/</a></div>


          <el-form-item style="text-align: center;">
            <el-button type="primary" class="submit-btn" @click="onSubmitTxxx('addstinfoForm')">Submit</el-button>
            <el-button @click="resetForm('addstinfoForm')" >reset</el-button>
          </el-form-item>


        </el-form>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  // eslint-disable-next-line
  name: 'txxx',
  data() {


    var checkskillLevel = (rule, value, callback) => {
      let overtime2 = this.$refs.overtime2.value;
      if (value && overtime2) {
        callback()
      } else {
        if (!value) {
          callback(new Error('请输入加班一个工'))
        }
        if (!overtime2) {
          callback(new Error('请输入加班半个工'))
        }
      }
    }

    return {
      // otherLanguage: '',   !!!!!!!!!!
      skills_list: [],
      interests_list:[],
      addstinfo: {
        name: '',

        skillLevel: [{skillName:'',level:''}],

        major: '',
        leadInt: '',
        grade: '',
        fieldInt: [''],
        prod: '',
        exep: '',
        // checkedLanguage: [],   !!!!!!!!!!!!!!!!
        prefer: '',
        preferNot: '',
        mbti: ''
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
        // skillLevel: [
        //   {
        //     required: true,
        //     message: 'Skill level cannot be empty',
        //     trigger: 'blur'
        //   }
        // ],
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
  mounted: function() {
    this.interests_list = this.loadAll_interests();
    this.skills_list = this.loadAll();
    this.testGomain()
  },
  methods: {

    querySearch(queryString, cb) {
      var skills_list = this.skills_list;
      var results = queryString ? skills_list.filter(this.createFilter(queryString)) : skills_list;
      // callback to get the skill list filtered
      cb(results);
    },



    createFilter(queryString) {
      return (skill_list) => {
        return (skill_list.skill.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
      };
    },

    handleSelect(item) {
      console.log(item);
    },

    loadAll() {
      return [
        { "skill": "Python", "value": "Python" },
        { "skill": "Java", "value": "Java" },
        { "skill": "C#", "value": "C#" },
        { "skill": "C++", "value": "C++" },
        { "skill": "Javascript", "value": "Javascript" },
        { "skill": "Html", "value": "Html"  },
        { "skill": "Kotlin", "value": "Kotlin"  },
        { "skill": "swift", "value": "swift"  },
        { "skill": "LUA", "value": "LUA"  },
        { "skill": "SQL", "value": "SQL"  },
        { "skill": "php", "value": "php"  },
        { "skill": "Scripting", "value": "Scripting"}
      ];
    },

    loadAll_interests() {
      return [
        { "interest": "Books", "value": "Books" },
        { "interest": "Health", "value": "Health" },
        { "interest": "Business", "value": "Business" },
        { "interest": "Music", "value": "Music" },
        { "interest": "Education", "value": "Education" },
        { "interest": "Entertainment", "value": "Entertainment"  },
        { "interest": "Grocery", "value": "Grocery"  },
        { "interest": "News", "value": "News"  },
        { "interest": "Games", "value": "Games"  },
        { "interest": "Media", "value": "Media"  },
        { "interest": "Academic", "value": "Academic"  },
        { "interest": "Social Networking", "value": "Social Networking"},
        { "interest": "Lifestyle", "value": "Lifestyle"  },
        { "interest": "Shopping", "value": "Shopping"  },
        { "interest": "Travel", "value": "Travel"  },
        { "interest": "Sports", "value": "Sports"  },
        { "interest": "Utilties", "value": "Utilties"  },
        { "interest": "Others", "value": "Others"  },
      ];
    },

    resetForm(formName) {
      this.$refs[formName].resetFields();
    },


    removeInterest(item) {
      var index = this.addstinfo.fieldInt.indexOf(item)
      if (index !== -1) {
        this.addstinfo.fieldInt.splice(index, 1)
      }
    },

    // addInterest() {
    //   this.addstinfo.fieldInt.push({
    //     value: '',
    //     key: Date.now()
    //   });
    // },

    addInterest() {
      this.addstinfo.fieldInt.push('');
    },

    removeSkill(item) {
      var index = this.addstinfo.skillLevel.indexOf(item)
      if (index !== -1) {
        this.addstinfo.skillLevel.splice(index, 1)
      }
    },
    addSkill() {
      this.addstinfo.skillLevel.push({
        skillName: '',
        level: '',
        key: Date.now()
      });
    },


    languageChecked(language) {
      this.checkedLanguage = []
      this.checkedLanguage.push(language)
    },

    onSubmitTxxx(form) {
      // if (this.otherLanguage.length !== 0) {
      //   this.addstinfo.checkedLanguage.push(this.otherLanguage)
      // }
      console.log(this.addstinfo)
      this.loading = true
      // this.addstinfo
      this.$store.dispatch('user/addstinfo', this.addstinfo).then(() => {
        // this.$router.push({ path: this.redirect || '/' }) // 跳转到main页
        this.$router.go(0)
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
    },
    testGomain() {
      console.log('TXXX' + this.type)
      if (this.type !== 0) {
        this.$router.push('/')
      }
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

.interest_container{
width: 40%;
margin-right: 20px;
}

.add_btn{
margin-bottom: 10px;
}

a{text-decoration:underline}

.interest_item{
  /* display: flex;
  justify-content: center; */
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
  /* text-align: center; */
}

.title {
font-family: 'Microsoft TaHei';
font-weight: bold;
font-size: 26px;
color: #C99700;
margin:auto;
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
background-color: #409EFF;
text-align: center;
}

.line{
  text-align: center;
}
</style>
