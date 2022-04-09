<template>
  <div class="project_page">
    <div class="project_page_box">
      <div class="project_header">
        <!-- <el-button >Number of students w/o a group</el-button>
                <el-button >Number of Student width a group</el-button> -->
        <div class="noGroup">Number of students w/o a group: <span class="number">{{ noNumber }}</span></div>
        <div class="yGroup">Number of Student with a group: <span class="number">{{ haveNumber }}</span></div>
        <div>
          <el-button>Find Teammate</el-button>
        </div>
      </div>
      <div class="project_content">
        <div class="content_left">
          <div class="content_left_header">
            <div style="color:#409EFF;font-weight:600;">Project Rooms</div>
            <div class="seach">
              <el-input v-model="keyWords" placeholder="title,idea,keyword,skill,wanted" prefix-icon="el-icon-search" />
              <el-button type="primary" @click="fetchData">Search</el-button>
            </div>
            <div>
              <el-button @click="addproj()">Create new project!</el-button>
            </div>
          </div>
          <div class="content_left_button">
            <el-button type="info" round @click="button('Web app')">Web app</el-button>
            <el-button type="info" round @click="button('Android')">Android</el-button>
            <el-button type="info" round @click="button('iOS')">iOS</el-button>
            <el-button type="info" round @click="button('Python')">Python</el-button>
            <el-button type="info" round @click="button('C++')">C++</el-button>
            <el-button type="info" round @click="button('Java')">Java</el-button>
            <el-button type="info" round @click="button('Other languages')">Other languages</el-button>
          </div>
          <div class="content_left_content">
            <div v-for="(item, index) in projectList" :key="index" class="content_card" @click="goDetail(item)">
              <p>project name:<span>{{ item.projectName }}</span></p>
              <p>keywords:<span>{{ item.keywords }}</span></p>
              <p>type:<span v-for="(items,indexs) in item.type" :key="indexs">{{ items+' '+' ' }}</span></p>
              <p>Skill wanted:<span>{{ item.skillWanted }}</span></p>
            </div>
          </div>
        </div>
        <div class="content_right">
          <div class="content_right_header">
            <p class="right_Annoucement" style="color:#409EFF;font-weight:600;">
              <span style="color:#352E8D;">★★★</span> Annoucement board <span style="color:#352E8D;">★★★</span>
            </p>
          </div>
          <div class="content_right_content">
            <p class="right_Recommend" style="color:#409EFF;font-weight:600;">Recommend:</p>
            <div class="Recommend_card">
              <div v-for="(item, index) in recommendLists" :key="index" class="card">
                <div class="project" @click="goDetail(item)">
                  <p style="color:#0dcaf0;">Project: {{ item.projectName }}</p>
                  <p style="color:#f41127;">Skill wanted: {{ item.skillWanted }}</p>
                </div>
                <div class="card_img"><img src="../../assets/avatar/tuijian.png" alt=""></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {
  getList,
  HaveTeamNumber,
  noTeamNumber,
  recommendList
} from '@/api/project'
export default {
  data() {
    return {
      keyWords: '', // search Content
      projectList: [],
      selectwords: [],
      haveNumber: null,
      noNumber: null,
      recommendLists: []
    }
  },
  created() {
    this.fetchData()
    this.getHaveNumber()
  },
  methods: {
    goDetail(item) {
      const routerJump = this.$router.resolve({
        path: '/projectdetail/index',
        query: {
          projectId: item.projectId
        }
      })
      window.open(routerJump.href, '_blank')
      // this.$router.push({path:'/projectdetail',query:{projectId:item.projectId}})
    },
    addproj() {
      const routerJump = this.$router.resolve({
        path: '/addproject/index',
        query: {}
      })
      window.open(routerJump.href, '_blank')
      // this.$router.push({path:'/projectdetail',query:{projectId:item.projectId}})
    },
    button(val) {
      this.selectwords.push(val)
      // console.log(this.selectwords);
      this.fetchData()
      this.selectwords = []
    },
    fetchData() {
      this.listLoading = true
      const params = {
        inputword: this.keyWords,
        selectword: this.selectwords
      }
      const { inputword, selectword } = params
      // params
      console.log('fetchData start')
      getList({
        inputword: inputword,
        selectword: selectword
      }).then(response => {
        this.projectList = response.projectList
        // this.listLoading = false
      })
      recommendList().then(response => {
        this.recommendLists = response.projectList
        // this.listLoading = false
      })
    },
    getHaveNumber() {
      HaveTeamNumber().then(response => {
        this.haveNumber = response.numval
      })
      noTeamNumber().then(response => {
        this.noNumber = response.numval
      })
    }
  }
}
</script>
<style lang="scss" scoped>
  .project_page_box {
    padding: 50px;
    background: #F1F1F1;

    ::-webkit-scrollbar {

      width: 0px;

      height: 0px;

      background-color: #ccc;

    }

    .project_header {
      display: flex;

      .noGroup {
        width: 320px;
        height: 50px;
        //   border: 1px solid #ccc;
        line-height: 47px;
        padding-left: 20px;
        border-radius: 10px;
        background: white;

        //   display: flex;
        .number {
          //   text-align: center;
          padding-left: 10px;
          font-size: 24px;
          color: red;
          //   padding-top: 15px;
        }
      }

      .yGroup {
        width: 320px;
        height: 50px;
        //   border: 1px solid #ccc;
        line-height: 47px;
        padding-left: 20px;
        border-radius: 10px;
        margin-left: 20px;
        margin-right: 20px;
        background: white;

        .number {
          padding-left: 10px;
          font-size: 24px;
          color: #409EFF;
          //   padding-top: 15px;
        }
      }
    }

    .project_content {
      display: flex;
      justify-content: space-between;
      margin-top: 40px;

      .content_left {
        width: 70%;
        //   border: 2px solid #ccc;
        height: 545px;
        border-radius: 10px;
        background: white;
        ;

        .content_left_header {
          display: flex;
          padding: 20px;
          justify-content: space-between;

          .seach {
            display: flex;
            width: 500px;
            margin-left: 20px;
          }
        }

        .content_left_button {
          display: flex;
          //   justify-content: space-between;
          padding: 20px;
          padding-top: 0px;
        }

        .content_left_content {
          width: 95%;
          border: 1px solid #ccc;
          margin: 0 auto;
          height: 377px;
          border-radius: 5px;
          overflow: scroll;
          display: flex;
          justify-content: space-around;
          flex-wrap: wrap;
          padding-bottom: 20px;

          .content_card {
            width: 40%;
            height: 150px;
            //   border: 1px solid #FCFEE5;
            border: 2px solid #0dcaf0;
            padding-left: 20px;
            margin-top: 26px;
            cursor: pointer;
            background: #FCFEE5;
            border-radius: 10px;
            color: #9FC5F8;
          }
        }
      }

      .content_right {
        width: 29%;
        //   border: 2px solid #ccc;
        height: 545px;
        border-radius: 10px;

        .content_right_header {
          width: 100%;
          height: 200px;
          border: 2px solid white;
          background: white;
          border-radius: 10px;

          .right_Annoucement {
            width: 100%;
            text-align: center;
            padding-bottom: 10px;
            border-bottom: 1px solid rgb(235, 232, 232);
          }
        }

        .content_right_content {
          width: 100%;
          border: 2px solid white;
          margin-top: 20px;
          height: 323px;
          border-radius: 10px;
          padding-left: 10px;
          background: white;

          .right_Recommend {
            font-size: 20px;
            line-height: 7px;
          }

          .Recommend_card {
            .card {
              height: 80px;
              //   border: 1px solid #ccc;
              border-left: 2px solid #0dcaf0;
              width: 95%;
              margin-left: 5px;
              display: flex;
              justify-content: space-between;
              padding-left: 10px;
              margin-top: 10px;
              border-radius: 10px;
              background: #F7F7FF;
              cursor: pointer;

              .project {
                p {
                  font-size: 18px;
                  line-height: 15px;

                }
              }

              .card_img {
                width: 80px;
                margin-top: 12px;
              }

              img {
                width: 60px;
                height: 60px;
              }
            }

          }
        }
      }
    }
  }
</style>
<style lang="scss">
  .project_page_box {
    .seach {
      .el-input--prefix .el-input__inner {
        width: 400px;
        border-radius: 50px;
      }

      .el-button--primary {
        height: 35px;
        line-height: 1px;
      }
    }

    .el-button--info {
      color: #FFF;
      background-color: #9FC5F8;
      border-color: #9FC5F8;
    }
  }
</style>
<style>
  .el-button:active {
    background: #126c9e !important;
    font-weight: bold;
  }
  /*按钮悬浮*/
  .el-button:hover {
    background: #126c9e !important;
    color: white !important;
    font-weight: bold;
    border-color: #01a8f9 !important;
  }
  /*按钮点击*/
  .el-button:focus {
    background: #126c9e !important;
    color: white !important;
    font-weight: bold;
    border-color: #01a8f9 !important;
  }
</style>
