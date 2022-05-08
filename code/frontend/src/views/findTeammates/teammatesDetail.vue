<template>
  <div class="teammatesDetail" >
    <el-card class="box-card" >
      <div class="content" style="width: 100%;">
        <el-row style="width: 100%;">
          <el-col :span="10" style="width: 100%;">
            <span>Name:</span>
            <span>{{detailList.name}}</span>
          </el-col>
        </el-row>
        <el-row style="width: 100%;">
          <el-col :span="10" style="width: 100%;">
            <span>Major:</span>
            <span>{{detailList.major}}</span>
          </el-col>
        </el-row>
        <el-row style="width: 100%;">
          <el-col :span="19" style="width: 100%;">
            <div style="font-weight:600">Skills:</div>
            <div class="skillsList">
              <div v-for="(ite,ind) in detailList.skillLevel" :key="ind" style="padding-left:40px">
                <span>{{ind+1}}.</span>
                <span>{{ite.skillName}}</span>
                <span>({{ite.level}})</span>
              </div>
            </div>
          </el-col>
        </el-row>
        <el-row style="width: 100%;">
          <el-col :span="10" style="width: 100%;">
            <span>Leadership Interst:</span>
            <span>{{detailList.leadInt}}</span>
          </el-col>
        </el-row>
        <el-row style="width: 100%;">
          <el-col :span="10" style="width: 100%;">
            <span>Filed of Intersts:</span>
            <span v-for="(itm,inx) in detailList.fieldInt" :key="inx"><span style="padding-left:5px; padding-right:5px;"
                v-if="inx!==0">/</span>{{itm}}</span>
          </el-col>
        </el-row>
        <el-row style="width: 100%;">
          <el-col :span="10" style="width: 100%;">
            <span>Type of End Product:</span>
            <!-- <span v-for="(itm,inx) in detailList.prod" :key="inx"><span style="padding-left:5px; padding-right:5px;"
                v-if="inx!==0">/</span>{{itm}} </span> -->
            <span>{{detailList.prod}}</span>
          </el-col>
        </el-row>
        <el-row style="width: 100%;">
          <el-col :span="10" style="width: 100%;">
            <span>Related Experience:</span>
            <span>{{detailList.expe}}</span>
          </el-col>
        </el-row>
        <el-row style="width: 100%;">
          <el-col :span="10" style="width: 100%;">
            <span>MBTI Result:</span>
            <span>{{detailList.mbti}}</span>
          </el-col>
        </el-row>
        <el-row style="width: 100%;">
          <el-col :span="10" style="width: 100%;">
            <span>Project:</span>
            <span class="goProject" @click="goProject(projectlList.projectId)"
              v-if="projectlList.projectName">{{projectlList.projectName}}</span>
          </el-col>
        </el-row>
      </div>
      <div class="send">
        <el-button type="primary" @click="goSendMessage(detailList.email)">Send message</el-button>
      </div>
    </el-card>
  </div>
</template>
<script>
  import {
    getDetail
  } from '@/api/message'
  export default {
    data() {
      return {
        detailList: {},
        projectlList: {},
      };
    },
    created() {
      this.getListDetail()
    },
    methods: {
      getListDetail() {
        const params = {
          email: this.$route.query.email,
        }
        const {
          email
        } = params
        getDetail({
          email: email
        }).then(res => {
          //console.log(res);
          this.detailList = res.userDetails
          this.projectlList = res.userProject

        })
      },
      goProject(id) {
        const routerJump = this.$router.resolve({
          path: '/projectdetail/index',
          query: {
            projectId: id
          }
        })
        window.open(routerJump.href, '_blank')
      },
      goSendMessage(email) {
        const routerJump = this.$router.resolve({
          path: '/message/index',
          query: {
            email: email
          }
        })
        window.open(routerJump.href, '_blank')
      },
    },

  };
</script>
<style lang="scss" scoped>
  .teammatesDetail {
    .box-card {
      width: 70%;
      margin: 0 auto;
      margin-top: 20px;
      padding-left: 50px;
      padding-right: 50px;
      background: #f1f1f1;

      .content {
        font-size: 20px;
      }
    }

    .el-col-10 {
      line-height: 70px;

      span:nth-child(1) {
        font-weight: 600;
      }

      span:nth-child(2) {
        padding-left: 40px;
      }

      .goProject {
        color: #018EFE;
        cursor: pointer;
      }
    }

    .el-col-19 {
      display: flex;
      margin-top: 23px;
    }

    .send {
      width: 200px;
      margin: 0 auto;

      .el-button--primary {
        background: #018EFE;
        border-color: #018EFE;

      }

      .el-button--primary:hover {
        background: #029342;
        border-color: #029342;
      }
    }

    .skillsList {
      line-height: 60px;

      div:nth-child(1) {
        line-height: 20px;
      }
    }
  }
</style>
