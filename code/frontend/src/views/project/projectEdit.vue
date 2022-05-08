<template>
  <div class="projectDetaile">
    <el-card class="box-card">
    <el-form label-width="150px" :model="projectForm" ref="addFormList">
      <el-form-item label="Project name:" prop="projectName">
        <el-input v-model="projectForm.projectName"></el-input>
      </el-form-item>
      <div class="box">
          <div class="left">
              <div class="left_top">
                  <div class="Introduction">
                    <el-form-item label="Project Introduction:" prop="Introduction">
                      <el-input v-model="projectForm.projectIntroduction" type="textarea"></el-input>
                    </el-form-item>
                  </div>
                  <div class="AppliedList">
                    <el-form-item label="Applied list:" prop="AppliedList">
                      <div class="appliedList">
                        <div  v-for="(item,index) in projectForm.appliedList" :key="index">
                            <p>{{item.name}} <span style="padding-left:1px;">({{item.eml}})</span></p>
                        </div>
                      </div>
                    </el-form-item>
                </div>
            </div>
            <el-form-item label="keywords:" prop="keywords">
              <el-input v-model="projectForm.keywords"></el-input>
            </el-form-item>
            <el-form-item label="Intended language:" prop="language">
              <el-checkbox-group v-model="projectForm.intendedLanguage" @change="intendedLanguageChange">
                  <el-checkbox label="Java">JAVA</el-checkbox>
                  <el-checkbox label="Python">Python</el-checkbox>
                  <el-checkbox label="C#">C#</el-checkbox>
                  <el-checkbox label="Javascript">Javascript</el-checkbox>
                  <el-checkbox label="Html">Html</el-checkbox>
                  <el-checkbox label="Kotlin">Kotlin</el-checkbox>
                  <el-checkbox label="PHP">PHP</el-checkbox>
              </el-checkbox-group>
            </el-form-item>
            <el-form-item label="If other:" prop="other">
              <el-input v-model="projectForm.otherLanguage"></el-input>
            </el-form-item>
            <el-form-item label="Type:" prop="Type">
              <el-checkbox-group v-model="projectForm.type"  @change='typeChange'>
                <el-checkbox label="Web">Web</el-checkbox>
                <el-checkbox label="Android">Android</el-checkbox>
                <el-checkbox label="IOS">IOS</el-checkbox>
                <el-checkbox label="Others">Others</el-checkbox>
              </el-checkbox-group>
            </el-form-item>
            <el-form-item label="Skill wanted:" prop="other">
              <div class="skillwanted">
                 <el-input v-model="projectForm.skillWanted" type="textarea"></el-input>
              </div>
             
            </el-form-item>
          </div>
          <div class="right">
            <div class="teame">
              <div class="teamBox">
                <div class="right_title">Team name:</div>
                <el-input v-model="projectForm.teamName"></el-input>
              </div>
             
              <div class="right_box">
                <div class="right_titles">Leader:</div>
                <div class="right_con"><div>{{projectForm.teamLeaderName}}</div>{{projectForm.teamLeader}}</div>
              </div>
              <div v-for="(item,index) in projectForm.teamMemName" :key='index' class="teamBox">
                <div class="right_title">Member{{index+1}}:</div>
                <div>
                  <div>{{item.name}}</div>
                  
                  <el-input v-model='projectForm.teamMemName[index].eml' :disabled="userRole==1?false:userRole==0&&item.eml.length>0&&item.choose?true:false"></el-input>
                  <i class="el-icon-delete" v-if="userRole==1" @click="deleteMember(index)"></i>
                </div>
              </div>
            <el-button type="primary" @click="addss" v-if="userRole==1">+</el-button>
            </div>
            <el-form-item class="form_btn">
              <el-button size="small" type="primary" @click="save()">Save</el-button>
            </el-form-item>
          </div>
        </div>
      </el-form>
    </el-card>
  </div>
</template>
<script>
import { projectEdit,saveEditProject } from '@/api/project'
export default {
  data() {
    return {
      projectForm: {
        projectName: "",
        projectIntroduction: "",
        teamName: "",
        teamLeader: "",
        teamMemName: [],
        appliedList: [],
        keywords: "",
        intendedLanguage: [],
        other: "",
        type: []
      },
    //   detaileList:[],
      projectId:'',
      userRole:null,
    };
  },
  created(){
      this.projectId=this.$route.query.projectId
      this.getDetail()
  },
  methods: {
    addss(){
      this.projectForm.teamMemName.push({ eml:""})
    },
      intendedLanguageChange(val){
        //   console.log(val);
          this.projectForm.intendedLanguage=val
      },
      typeChange(val){
        //   console.log(val);
          this.projectForm.type=val
      },
     getDetail(){
            let params={
                projectId:this.$route.query.projectId
            }
            projectEdit(params).then(res=>{
                this.projectForm=res.project
                let arr=[]
                res.project.teamMemName.forEach((item,indedx)=>{
                  let obj={
                    ...item,
                    choose:res.userRole==0&&item.eml.length>0?true:false
                  }
                  arr.push(obj)
                })
                res.project.teamMemName=arr

              console.log(res.project.teamMemName,"res.project");
                this.userRole=res.userRole
            })
        },
        deleteMember(index){
            this.projectForm.teamMemName.splice(index,1)
        },
    save() {
        this.projectForm.teamMemName.forEach((item,index)=>{
         delete item.choose
        })
        // return
        let params={
            projectId:this.projectId,
            projectName:this.projectForm.projectName,
            projectIntroduction:this.projectForm.projectIntroduction,
            keywords:this.projectForm.keywords,
            intendedLanguage:this.projectForm.intendedLanguage,
            otherLanguage:this.projectForm.otherLanguage,
            type:this.projectForm.type,
            skillWanted:this.projectForm.skillWanted,
            teamName:this.projectForm.teamName,
            teamMemName:this.projectForm.teamMemName,
        }
        saveEditProject(params).then(res=>{
            if(res.code==1){
                this.$message.success(res.msg)
                this.$router.push('/')
            }else{
                this.$message.success(res.msg)
            }
        })
    //   this.$router.push({ path: "/project" });
    }
  }
};
</script>
<style lang="scss" scoped>
.skillwanted{
  ::v-deep .el-textarea__inner{
    height: 180px;
    overflow-y: scroll;
    resize: none
  }
}
.projectDetaile {
    .appliedList{
        border: 1px solid #ccc;
        width:195px;
        height: 179px;
        padding:10px;
        border-radius: 5px;
        background: white;
        overflow-y:  scroll !important;
        p{
            display: flex;
            height: 16px;
            line-height: 10px;
        }
    }
  .box {
    display: flex;
    justify-content: space-between;
    .left {
      .left_top {
        display: flex;
        justify-content: space-between;
        .Introduction{
          // border: 1px solid red;
          ::v-deep .el-textarea__inner{
            width: 195px;
            height: 180px;
            overflow-y: scroll;
            resize: none;
          }
        }
      }
    }
  }
  .box-card {
    width: 80%;
    margin: 0 auto;
    margin-top: 20px;
    background: #F1F1F1;
  }
  .teamBox{
      display: flex;
      margin-top: 10px;
  }
  .teame {
    height:568px;
    width: 100%;
    margin: 0 auto;
    // height: 100px;
    padding-top: 10px;
    padding-bottom: 20px;
    padding-left: 20px;
    padding-right: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    background: #F7F7FF;
    overflow-y: scroll !important;
    .right_box{
        display: flex;
         margin-top: 15px;
    }
    .right_title{
        color: #606266;
        line-height: 40px;
        font-weight: 700;
        width:115px;
        padding-top: 7px;
    }
     .right_titles{
        color: #606266;
        line-height: 40px;
        font-weight: 700;
        width:115px;
        padding-top: 7px;

    }
    .right_con{
        line-height: 40px;
        //  padding-left:20px;
        div{
            height: 20px;
        }
    }
  }
  .el-input {
    width: 80%;
  }
  .el-textarea {
    width: 100%;
  }
  .el-icon-delete {
    font-size: 18px;
    margin-left: 10px;
    line-height: 40px;
    cursor: pointer;
  }
}
</style>
<style lang="scss">
.projectDetaile{
    .teame {
        .el-input {
            width:70%;
    // margin-left:20px;
    line-height:40px;
  }
  .el-input__inner{
      height:30px;
  }
    .el-form-item__label{

    text-align:left;
}
.el-form-item__content{
    margin-left:70px !important;
}
.el-form-item__label{
    width:80px !important;
}
.el-form-item{
    margin-bottom:10px;
}
.el-icon-delete{
   color: rgb(241, 60, 60);
}
}
.AppliedList{
    .el-form-item__label{
    text-align:right !important;
}
}
}


</style>
