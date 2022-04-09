<template>
<div>

    <el-container>
        <el-main>
            <el-header>Create Project</el-header>
            <br/>
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-position="right" label-width="150px" class="demo-ruleForm">
            <el-form-item label="Teamname" prop="teamname">
                <el-input v-model="ruleForm.teamname"></el-input>
            </el-form-item>

            <el-form-item label="Project name" prop="projectname">
                <el-input v-model="ruleForm.projectname"></el-input>
            </el-form-item>

            <el-form-item label="Project idea" prop="projectidea">
                <el-input type="textarea" v-model="ruleForm.projectidea"></el-input>
            </el-form-item>

            <el-form-item label="Keywords" prop="keywords">
                <el-input v-model="ruleForm.keywords" placeholder="Keywords for your project; e.g. Game, Education, Social media"></el-input>
            </el-form-item>

            <el-form-item label="Intended Language" prop="language">
                <el-checkbox-group v-model="ruleForm.language">
                  <el-checkbox label="Java"></el-checkbox>
                  <el-checkbox label="Python"></el-checkbox>
                  <el-checkbox label="C#"></el-checkbox>
                  <el-checkbox label="Javascript"></el-checkbox>
                  <el-checkbox label="Html"></el-checkbox>
                  <el-checkbox label="Kotlin"></el-checkbox>
                  <el-checkbox label="PHP"></el-checkbox>
                </el-checkbox-group>
            </el-form-item>

            <el-form-item label="Other Language" prop="otherlanguage">
                <el-input v-model="ruleForm.otherlanguage"></el-input>
            </el-form-item>

            <el-form-item label="App Type" prop="apptype">
              <el-checkbox-group v-model="ruleForm.apptype">
                <el-checkbox label="Web"></el-checkbox>
                <el-checkbox label="Android"></el-checkbox>
                <el-checkbox label="IOS"></el-checkbox>
                <el-checkbox label="Others"></el-checkbox>
              </el-checkbox-group>
            </el-form-item>

            <el-form-item label="Skill Wanted" prop="skillwanted">
                <el-input type="textarea" v-model="ruleForm.skillwanted" placeholder="Please seperate by comma"></el-input>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">Create</el-button>
                <el-button @click="resetForm('ruleForm')">Reset</el-button>
            </el-form-item>

            </el-form>
        </el-main>
    </el-container>
    <!-- <section class="form-container">

    </section> -->

</div>
</template>

<script>
  export default {
    data() {
      return {
        ruleForm: {
          teamname: '',
          projectname: '',
          projectidea: '',
          keywords: '',
          language: [],
          otherlanguage:'',
          apptype: [],
        //   type: [],
          skillwanted: ''
        },
        rules: {
          teamname: [
            { required: true, message: 'please input your teamname', trigger: 'blur' },
            { max: 32, message: 'The length should be less then 32', trigger: 'blur' }
          ],
          projectname: [
            { required: true, message: 'please input your projectname', trigger: 'blur' },
            { max: 32, message: 'The length should be less then 32', trigger: 'blur' }
          ],
          projectidea: [
            { required: true, message: 'please input your projectidea', trigger: 'blur' }
          ],
        //   date1: [
        //     { type: 'date', required: true, message: 'data', trigger: 'change' }
        //   ],
        //   type: [
        //     { type: 'array', required: true, message: 'at lest one type', trigger: 'change' }
        //   ],
          keywords: [
            { required: true, message: 'please input your projectidea', trigger: 'blur' }
          ],
          language: [
            { required: true, message: 'please choose your intended programming language', trigger: 'change' }
          ],
          otherlanguage: [
            { required: false }
          ],
          apptype: [
            { required: true, message: 'please choose your app type', trigger: 'change' }
          ],
          skillwanted: [
            { required: true, message: 'please input your projectidea', trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            // alert('submit!');

            this.$store.dispatch('create_project', this.ruleForm).then(() => {
            this.$router.push('/') // to the main page
            this.loading = false
            }).catch(() => {
            this.loading = false
            })

          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
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

.el-header{
    background-color: #d1e1f5;
    color: #333;
    text-align: center;
    line-height: 60px;
    font-size:30px;

  }

.el-container{
    background-color: #ffffff;
    height: 800px;
    /* position: relative; */
    position: absolute;
    width: 100%;
    height: 100%;

    top: 4%;
    /* right: 20%;
    left: 20%; */

    padding: 25px;
    border: 1px solid rgb(187, 185, 185);
    border-radius: 5px;
    text-align: center;
    /* background-size: 20% 20%; no use*/
  }
</style>
