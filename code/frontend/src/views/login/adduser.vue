<template>
  <div class="register">
    <section class="form-container">
      <span class="title">Create a TeamUp Account</span>
      <el-button round style="margin-left: 80px;font-size: 22px;" @click.native.prevent="signIn">LOGIN</el-button>
      <div class="manage-tip">
        <el-form ref="registerForm" :model="registerUser" status-icon :rules="rules" label-width="100px" class="registerForm">
          <el-form-item label="Username" prop="name">
            <el-input v-model="registerUser.name" placeholder="Please input the username" />
          </el-form-item>
          <el-form-item label="Identity" prop="identity" style="display: none;">
            <el-radio-group v-model="registerUser.identity">
              <el-radio label="Instructor" value="2" />
              <el-radio label="Student" value="0" />
            </el-radio-group>
          </el-form-item>
          <el-form-item label="JHU Email" prop="email">
            <el-input v-model="registerUser.email" placeholder="Please input the email" />
          </el-form-item>
          <el-form-item label="Password" prop="password">
            <el-input v-model="registerUser.password" type="password" placeholder="Please input the password" />
          </el-form-item>
          <el-form-item label="Confirm" prop="password2">
            <el-input v-model="registerUser.password2" type="password" placeholder="Confirm the password" />
          </el-form-item>
          <el-form-item label="Select Avatar" label-width="200" style="margin-top: -10px;">
            <el-switch v-model="showAvatar" active-color="#13ce66" style="display: none;" />
          </el-form-item>
          <el-form-item v-if="showAvatar" label=" " prop="avatar" class="avatar-select-form" label-width="5" style="margin-top: -20px;">
            <el-radio-group v-model="registerUser.avatar">
              <el-radio id="mice" label="mice"><span class="avarat-radio"> <img src="@/assets/avatar/mice.png" class="avatar"></span></el-radio>
              <el-radio id="cow" label="cow"><span class="avarat-radio"> <img src="@/assets/avatar/cow.png" class="avatar"></span></el-radio>
              <el-radio id="tiger" label="tiger"><span class="avarat-radio"> <img src="@/assets/avatar/tiger.png" class="avatar"></span></el-radio>
              <el-radio id="rabbit" label="rabbit"><span class="avarat-radio"> <img src="@/assets/avatar/rabbit.png" class="avatar"></span></el-radio>
              <el-radio id="dragon" label="dragon"><span class="avarat-radio"> <img src="@/assets/avatar/dragon.png" class="avatar"></span></el-radio>
              <el-radio id="snake" label="snake"><span class="avarat-radio"> <img src="@/assets/avatar/snake.png" class="avatar"></span></el-radio>
              <el-radio id="horse" label="horse"><span class="avarat-radio"> <img src="@/assets/avatar/horse.png" class="avatar"></span></el-radio>
              <el-radio id="sheep" label="sheep"><span class="avarat-radio"> <img src="@/assets/avatar/sheep.png" class="avatar"></span></el-radio>
              <el-radio id="monkey" label="monkey"><span class="avarat-radio"> <img src="@/assets/avatar/monkey.png" class="avatar"></span></el-radio>
              <el-radio id="chicken" label="chicken"><span class="avarat-radio"> <img src="@/assets/avatar/chicken.png" class="avatar"></span></el-radio>
              <el-radio id="dog" label="dog"><span class="avarat-radio"> <img src="@/assets/avatar/dog.png" class="avatar"></span></el-radio>
              <el-radio id="pig" label="pig"><span class="avarat-radio"> <img src="@/assets/avatar/pig.png" class="avatar"></span></el-radio>
              <el-radio id="undefined" label="undefined"><span class="avarat-radio"> <img src="@/assets/avatar/undefined.png" class="avatar"></span></el-radio>
              <el-radio id="xrr" label="xrr"><span class="avarat-radio"> <img src="@/assets/avatar/xrr.png" class="avatar"></span></el-radio>
              
            </el-radio-group>
          </el-form-item>
          <el-button type="primary" class="submit-btn" @click="submitForm('registerForm')">Create new account</el-button>
          <div class="tips" style="margin-left: 5px;">
            <span style="margin-right:20px;">Already have an account?</span>
            <a class="asp" @click="signIn">LOG IN</a>
          </div>
        </el-form>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Register',
  components: {},
  data() {
    var validatePass2 = (rule, value, callback) => {
      if (value !== this.registerUser.password) {
        callback(new Error('Password does not match!'))
      } else {
        callback()
      }
    }
    var validateEmail = (rule, value, callback) => {
      const end = value.slice(value.length - 8, value.length)
      if (end !== '.jhu.com' && end !== '@jhu.com' && end !== '.jhu.edu' && end !== '@jhu.edu') {
        callback(new Error('Wrong email format: must be JHU email'))
      } else {
        callback()
      }
    }
    return {
      showAvatar: true,
      registerUser: {
        name: '',
        email: '',
        password: '',
        password2: '',
        identity: '',
        avatar: '001'
      },
      rules: {
        name: [
          {
            required: true,
            message: 'Username cannot be empty',
            trigger: 'blur'
          },
          {
            min: 5,
            max: 12,
            message: 'Range within 5 to 12 characters',
            trigger: 'blur'
          }
        ],
        email: [
          {
            type: 'email',
            required: true,
            message: 'Wrong email format',
            trigger: 'blur'
          },
          {
            validator: validateEmail,
            trigger: 'blur'
          }
        ],
        password: [
          {
            required: true,
            message: 'Password cannot be empty',
            trigger: 'blur'
          },
          {
            min: 6,
            max: 12,
            message: 'Range within 6 to 12 characters',
            trigger: 'blur'
          }
        ],
        password2: [
          {
            required: true,
            message: 'Confirm password cannot be empty',
            trigger: 'blur'
          },
          {
            min: 6,
            max: 12,
            message: 'Range within 6 to 12 characters',
            trigger: 'blur'
          },
          {
            validator: validatePass2,
            trigger: 'blur'
          }
        ]
      }
    }
  },

  methods: {
    submitForm(formName) {
      this.$confirm('Confirm registration', 'Register', {
        confirmButtonText: 'Yes',
        cancelButtonText: 'No'
      }).then(() => {
        this.$store.dispatch('user/create_student', this.registerUser).then(() => {
          this.$router.push('/login') // 跳转到查看页
          this.loading = false
        }).catch(() => {
          this.loading = false
        })
        // this.$router.push('/login')
      })
    },
    signIn() {
      this.$router.push('/login')
    }
  }
}
</script>
<style lang="scss" scoped>
$bg:#2d3a4b;
$dark_gray:#889aa4;
$light_gray:#eee;
a:hover {  color : #409EFF ; }
</style>

<style scoped>

.register {
  position: relative;
  width: 100%;
  height: 100%;
/*    background: url(url) no-repeat center center;*/
  background-size: 100% 100%;
  text-align: center;
}

.form-container {
  width: 50%;
  height: 210px;
  position: absolute;
  background-color: #fff;
  top: 2%;
  left: 30%;
  padding: 25px;
  border-radius: 5px;
  text-align: center;
}

.title {
font-family: 'Microsoft TaHei';
font-weight: bold;
font-size: 26px;
color: #C99700;
/* margin-left: -80%; */
}

.registerForm {
width: 90%;
margin-top: 20px;
padding: 20px 40px 20px 20px;
border-radius: 5px;
box-shadow: 0px 5px 10px #cccc;
/* margin-left: 40%; */
}

.submit-btn {
width: 100%;
background-color: #409EFF;
}

.log-btn {
margin-top: 30px;
width: 100%;
font-size: 20px;
}

.avatar-select-form {
width: 100%;
padding: 20px 40px 20px 20px;
border-radius: 5px;
box-shadow: 0px 5px 10px #cccc;
}

.avatar-radio {
  width: 75px;
  height : 75px;
}

.avatar {
  width:75px;
  height:75px;
  background : no-repeat center center;
}

.tips {
  font-size: 14px;
  margin-bottom: 10px;
  margin-top: 20px;

  span {
    &:first-of-type {
      margin-right: 16px;
    }
  }
  asp {
    margin-right:5px;
    cursor: pointer;
  }
}
</style>
