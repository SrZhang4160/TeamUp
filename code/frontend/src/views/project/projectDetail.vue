<template>
  <div class="projectDetaile">
    <el-card class="box-card">
      <el-form ref="addFormList" label-width="150px" :model="detaileList">
        <div class="title">Project name:{{ detaileList.projectName }}</div>
        <div class="box">
          <div class="left">
            <div class="left_top">
              <div class="left_top_title">Project Introduction:</div>
              <!-- <div>{{detaileList.Introduction}}</div> -->
              <div class="left_top_content">
                {{ detaileList.projectIntroduction }}
              </div>
            </div>
            <el-form-item label="keywords:" prop="keywords">
              <!-- <el-input v-model="detaileList.keywords"></el-input> -->
              <div>{{ detaileList.keywords }}</div>
            </el-form-item>
            <el-form-item label="Intended language:" prop="language">
              <span v-for="(item,index) in detaileList.intendedLanguage" :key="index">{{ item }}
                <span>&#8194;&#8194;</span>
              </span>
            </el-form-item>
            <el-form-item label="Type:" prop="Type">
              <span v-for="(item,index) in detaileList.type" :key="index">{{ item }}
                <span>&#8194;&#8194;</span>
              </span>
            </el-form-item>
            <el-form-item label="Skill wanted:" prop="wanted">
              <!-- <el-input v-model="detaileList.other"></el-input> -->
              <div>{{ detaileList.skillWanted }}</div>
            </el-form-item>
          </div>
          <div class="right">
            <div class="teame">
              <div class="teamBox">
                <div class="right_title">Team name:</div>
                <div class="right_con">{{ detaileList.teamName }}</div>
              </div>
              <div class="teamBox">
                <div class="right_titles">Leader:</div>
                <div class="right_con">
                  <div>{{ detaileList.teamLeaderName }}</div>
                  {{ detaileList.teamLeader }}
                </div>
              </div>
              <div v-for="(item,index) in detaileList.teamMemName" :key="index" class="teamBox">
                <!-- <el-input v-model="detaileList.Member1"></el-input><i class="el-icon-delete"></i> -->
                <div class="right_titles">Member{{ index+1 }}:</div>
                <div class="right_con"><div>{{ item.name }}</div>{{ item.eml }}</div>
              </div>
            </div>
            <el-form-item class="form_btn">
              <el-button v-if="userRole==1||userRole==2" size="small" type="primary" @click="edit()">Edit</el-button>
              <el-button v-if="userRole==2" size="small" type="primary" @click="leave()">Leave Group</el-button>
              <el-button v-if="userRole==3||userRole==4" size="small" type="primary" @click="join()">Apply</el-button>
              <el-button v-if="userRole==1" size="small" type="primary" @click="terminate()">Terminate</el-button>
            </el-form-item>
          </div>
        </div>
      </el-form>
    </el-card>
  </div>
</template>
<script>
import { projectDetails, erminateProject, joinProject, leaveProject } from '@/api/project'
export default {
  data() {
    return {
      // detaileList:{
      //     projectName:'',
      //     Introduction:'',
      //     teamName:'',
      //     Leader:'',
      //     MemberOne:'',
      //     AppliedList:'srzhang@jhu.edu',
      //     keywords:'',
      //     language:1,
      //     other:'',
      //     Type:1,
      //     wanted:'',
      // },
      projectId: '',
      detaileList: {},
      userRole: null
    }
  },
  created() {
    this.projectId = this.$route.query.projectId
    this.getDetail()
  },
  methods: {
    edit() {
      this.$router.push(
        { path: '/projectEdit/index', query: { projectId: this.projectId }}
      )
    },
    join() {
      const params = {
        projectId: this.projectId
      }
      joinProject(params).then(res => {
        if (res.code === 1) {
          this.$message.success(res.msg)
          // this.$router.push({path:'/project'})
        } else {
          this.$message.error(res.msg)
        }
      })
    },
    leave() {
      this.$confirm('Confirm leave project', 'Register', {
        confirmButtonText: 'Yes',
        cancelButtonText: 'No'
      }).then(() => {
        const params = {
          projectId: this.projectId
        }
        leaveProject(params).then(res => {
          if (res.code === 1) {
            this.$message.success(res.msg)
            this.$router.push('/')
            // this.$router.push({path:'/project'})
          } else {
            this.$message.error(res.msg)
          }
        })
      })
    },
    terminate() {
      this.$confirm('Confirm terminate project', 'Register', {
        confirmButtonText: 'Yes',
        cancelButtonText: 'No'
      }).then(() => {
        const params = {
          projectId: this.projectId
        }
        erminateProject(params).then(res => {
          if (res.code === 1) {
            this.$message.success(res.msg)
            this.$router.push('/')
          } else {
            this.$message.error(res.msg)
          }
        })
      })
    },
    getDetail() {
      const params = {
        projectId: this.projectId
      }
      projectDetails(params).then(res => {
        this.detaileList = res.project
        this.userRole = res.userRole
      })
    }
  }
}
</script>
<style lang="scss" scoped>
.projectDetaile{
    .title{
        font-size: 29px;
        font-weight: 600;
        text-align: center;
    }
    .box{
        display: flex;
        justify-content: space-between;
        margin-top: 20px;
        .left{
            width:60%;
            .left_top{
                width: 100%;
                height: 330px;
                // border: 2px solid #ccc;
                border-radius: 10px;
                background: #F7F7FF;
                .left_top_title{
                    padding-top: 10px;
                    padding-left: 10px;
                    font-size: 28px;
                    text-align: center;

                }
                .left_top_content{
                    padding:10px;
                    line-height: 25px;
                }
            }
        }
    }
    .box-card{
        width:70%;
        margin:0 auto;
        margin-top: 20px;
        padding-left:50px;
        padding-right:50px;
        background: #F1F1F1;
    }
    .teame{
        background: #F7F7FF;
        width: 100%;
        margin: 0 auto;
        // height: 100px;
        padding-top: 20px;
        padding-bottom: 20px;
        border-radius: 10px;
        margin-bottom:20px;
        height: 500px;
        padding: 20px;
        .teamBox{
            display: flex;
            // margin-top: 15px;
            .right_title{
                color: #606266;
                line-height: 40px;
                font-weight: 700;
                // padding-top: 20px;

            }
            .right_titles{
                color: #606266;
                line-height: 40px;
                font-weight: 700;
                padding-top: 11px;

            }
            .right_con{
                line-height: 40px;
                padding-left:20px;
                div{
                    height:20px;
                }
            }
        }
    }
    .el-input{
        width:90%;
    }
    .el-textarea{
        width:90%;
    }
    .el-icon-delete{
        font-size: 18px;
        margin-left: 10px;
        cursor: pointer;
    }

}
</style>
<style lang="scss">
.projectDetaile{
    .teame{
        .el-form-item__label{
        text-align: left;
    }
    }
    .form_btn{
        .el-form-item__content{
            margin-left:100px !important;
        }
    }
}
</style>
