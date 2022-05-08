<template>
  <div class="project_page">
    <div class="project_page_box">
      <!-- -->
      <div class="project_name">Hi, {{ this.names }}</div>
      <div class="project_header">
        <el-card shadow="always" style="width: 32%; height: 150px">
          <div class="card_content">
            <div class="card_top" v-if="teacher == false">
              <span>Group Model</span>
            </div>
            <div
              class="card_bottom"
              v-if="teacher == false"
              @click="goeditpreview"
            >
              <span>Group students with One click</span>
            </div>
            <div class="card_bottoms" v-if="teacher == true">
              Number of students w/o a group:
              <span class="number">{{ noNumber }}</span>
            </div>
          </div>
        </el-card>
        <el-card shadow="always" style="width: 32%; height: 150px">
          <div class="card_center">
            <div class="card_top" v-if="teacher == false">
              <p>Group-Formation</p>
              <p>
                Students with a group:
                <span class="number" style="color: red">{{ haveNumber }}</span>
              </p>
              <p>
                Students without a group:
                <span class="number" style="color: #409eff">{{
                  noNumber
                }}</span>
              </p>
            </div>
            <!-- <div class="card_top" v-if="teacher == true"></div> -->
            <div
              class="card_bottom"
              v-if="teacher == false"
              @click="findTeammates"
            >
              <span>Student Info</span>
            </div>
            <div class="card_bottomss" v-if="teacher == true">
              Number of Student with a group:
              <span class="number">{{ haveNumber }}</span>
            </div>
          </div>
        </el-card>
        <el-card
          shadow="always"
          style="width: 32%; height: 150px"
          v-if="teacher == false"
        >
          <div class="card_end">
            <div class="card_top">
              <div
                class="right_Annoucement"
                style="color: #409eff; font-weight: 600; margin: 0 auto"
              >
                <span style="color: #91c09d">★★★</span>

                <span style="color: #91c09d"> Announcement board</span>
                <span style="color: #91c09d">★★★</span>
              </div>
              <el-carousel height="120px">
                <el-carousel-item v-for="(item,index) in bulletinboard" :key="index">
                  <div class="card_top_text">
                    <p
                      style="
                        font-weight: 600;
                        font-size: 18px;
                        text-align: center;
                        color: #34a673;
                      "
                    >
                      {{ item.name }}
                    </p>
                    {{ item.val }}
                  </div>
                </el-carousel-item>
              </el-carousel>
            </div>
            <div class="card_top"></div>
            <div class="card_bottom">
              <span>Find Teammate</span>
            </div>
          </div>
        </el-card>
        <el-card
          shadow="always"
          style="width: 29%; height: 40px"
          v-if="teacher == true"
        >
          <div class="card_center">
            <!-- <div class="card_top" v-if="teacher == true"></div> -->
            <!-- <div
              class="card_bottom"
              v-if="teacher == false"
              @click="findTeammates"
            >
              <span>Student Info</span>
            </div> -->
            <div
              class="card_bottoms"
              v-if="teacher == true"
              @click="findTeammates"
            >
              Find Teammate
            </div>
          </div>
        </el-card>
        <!-- <div class="noGroup" v-if="teacher==true">Number of students w/o a group: <span class="number">{{ noNumber }}</span></div>
        <div class="yGroup" v-if="teacher==true">Number of Student with a group: <span class="number">{{ haveNumber }}</span></div>
        <div v-if="teacher==true">
          <el-button @click="findTeammates">Find Teammates</el-button>
        </div>
        <div class="teacher_box" v-if="teacher==false">
          <div class="teacher_left">
            <div class="teacher_left_title">Group Model</div>
            <div class="teacher_left_button" @click="goeditpreview">Group students width One click</div>
          </div>
          <div class="teacher_right">
            <div class="teacher_right_top">
              <p>Group-Formation</p>
              <p>Students with a group: <span class="number" style="color:red;">{{ haveNumber }}</span></p>
              <p>Students without a group: <span class="number" style="color:#409EFF">{{ noNumber }}</span></p>
            </div>
            <div class="teacher_right_button"><el-button @click="findTeammates">Student Info</el-button></div>
          </div>
        </div>
        <div class="teacher_box_right">
          <div class="content_right_header"  v-if="teacher==false">
            <p class="right_Annoucement" style="color:#409EFF;font-weight:600;">
              <span style="color:#352E8D;">★★★</span> {{bulletinboard.name}} <span style="color:#352E8D;">★★★</span>
            </p>
            <div class="content_right_text">{{bulletinboard.val}}</div>
          </div>
        </div> -->
      </div>
      <div class="project_content">
        <div class="content_left">
          <div class="content_left_header">
            <div style="color: #409eff; font-weight: 600">Project Rooms</div>
            <div class="seach">
              <el-input
                v-model="keyWords"
                placeholder="title,idea,keyword,skill,wanted"
                prefix-icon="el-icon-search"
              />
              <el-button type="primary" @click="fetchData">Search</el-button>
            </div>
            <div  v-if="teacher == true">
              <el-button @click="addproj()">Create new project!</el-button>
            </div>
          </div>
          <div class="content_left_button">
            <el-button type="info" round @click="button('Web')"
              >Web app</el-button
            >
            <el-button type="info" round @click="button('Android')"
              >Android</el-button
            >
            <el-button type="info" round @click="button('iOS')">iOS</el-button>
            <el-button type="info" round @click="button('Python')"
              >Python</el-button
            >
            <el-button type="info" round @click="button('C++')">C++</el-button>
            <el-button type="info" round @click="button('Java')"
              >Java</el-button
            >
            <el-button type="info" round @click="button('Others')"
              >Other languages</el-button
            >
          </div>
          <div class="content_left_content">
            <div
              v-for="(item, index) in projectList"
              :key="index"
              class="content_card"
              @click="goDetail(item)"
            >
              <p>
                Project name:<span>{{ item.projectName }}</span>
              </p>
              <p>
                Keywords:<span>{{ item.keywords | ellipsis }}</span>
              </p>
              <p>
                Type:<span v-for="(items, indexs) in item.type" :key="indexs">{{
                  items + " " + " "
                }}</span>
              </p>
              <p>
                Skill wanted:<span>{{ item.skillWanted | ellipsis }}</span>
              </p>
            </div>
          </div>
        </div>
        <!--  teacher-->
        <div :class="teacher == false ? 'content_right' : 'content_rights'">
          <div class="content_right_header" v-if="teacher == true">
            <el-card shadow="always" style="height: 380px">
              <div class="card_end">
                <div class="card_top">
                  <div
                    class="right_Annoucement"
                    style="color: #409eff; font-weight: 600; margin: 0 auto"
                  >
                    <span style="color: #91c09d">★★★</span>
                    <span style="color: #91c09d"> Announcement board</span>
                    <span style="color: #91c09d">★★★</span>
                  </div>
                  <el-carousel height="350px">
                    <el-carousel-item v-for="(item,index) in bulletinboard" :key="index">
                      <div class="card_top_text">
                        <p
                          style="
                            font-weight: 600;
                            font-size: 18px;
                            text-align: center;
                            color: #34a673;
                          "
                        >
                          {{ item.name }}
                        </p>
                        {{ item.val }}
                      </div>
                    </el-carousel-item>
                  </el-carousel>
                </div>
                <div class="card_bottom">
                  <span></span>
                </div>
              </div>
            </el-card>
          </div>
          <div class="teacher_project" v-if="teacher == false">
            <pie :id="id" :option="option"></pie>
          </div>
          <div class="content_right_content" v-else>
            <p class="right_Recommend" style="color: #409eff; font-weight: 600">
              Recommend:
            </p>
            <div class="Recommend_card">
              <div
                v-for="(item, index) in recommendLists"
                :key="index"
                class="card"
              >
                <div class="project" @click="goDetail(item)">
                  <p style="color: #0dcaf0">Project: {{ item.projectName }}</p>
                  <p style="color: #f41127">
                    Skill wanted: {{ item.skillWanted | ellipsis2 }}
                  </p>
                </div>
                <div class="card_img">
                  <img src="../../assets/avatar/tuijian.png" alt="" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import pie from "../../components/pie";
import {
  getList,
  HaveTeamNumber,
  noTeamNumber,
  recommendList,
  bulletin,
} from "@/api/project";
import { mapGetters } from "vuex";
// import { import } from '@babel/types';
export default {
  components: {
    pie,
  },
  filters: {
    ellipsis(value) {
      if (!value) return "";
      if (value.length > 25) {
        return value.slice(0, 23) + "...";
      }
      return value;
    },
    ellipsis2(value) {
      if (!value) return "";
      if (value.length > 15) {
        return value.slice(0, 13) + "...";
      }
      return value;
    },
  },
  data() {
    return {
      keyWords: "", // search Content
      projectList: [],
      selectwords: [],
      bulletinboard: [],
      haveNumber: null,
      noNumber: null,
      recommendLists: [],
      names: "",
      teacher: true, //是否是教师 true为否
      id: "test",
      option: {
        colors: ["red", "blue", "yellow", "pink"],
        chart: {
          type: "pie",
          options3d: {
            enabled: true,
            alpha: 60,
            beta: 0,
          },
        },
        title: {
          text: "111",
        },
        plotOptions: {
          pie: {
            allowPointSelect: true, //每个扇块能否选中
            cursor: "pointer", //鼠标指针
            depth: 35, //饼图的厚度
            dataLabels: {
              enabled: true, //是否显示饼图的线形tip
            },
          },
        },
        serice: [
          {
            type: "pie",
            data: [
              ["测试1", 12], //模块名和所占比，也可以{name: '测试1',y: 12}
              ["测试2", 23],
              ["测试3", 19],
              ["测试4", 29],
            ],
          },
        ],
      },
    };
  },
  computed: {
    ...mapGetters(["name", "eml", "sex", "type", "avatar"]),
  },
  created() {
    this.fetchData();
    this.getHaveNumber();
    //console.log(this.type);
    if (this.type == "1") {
      this.teacher = false;

    } else {
      this.teacher = true;
      this.todorecommendList();
    }
    this.names = this.name;
  },
  mounted: function () {
    this.testType();
    this.getbulletin();
    // HighCharts.chart(this.id,this.option)
  },
  methods: {
    // 点击跳转操作页面
    goeditpreview() {
      const routerJump = this.$router.resolve({
        path: "/editpreview/editpreview",
        query: {
          isTemp: 0,
        },
      });
      window.open(routerJump.href, "_blank");
      // window.location.href="http://localhost/#/editpreview/editpreview?isTemp=0"
      // window.open("http://localhost/#/editpreview/editpreview?isTemp=0", '_blank')
    },
    txxx() {
      this.$router.push("/txxx/index");
    },
    testType() {
      if (this.type === 0) {
        this.$router.push("/txxx/index");
      }
    },
    goDetail(item) {
      const routerJump = this.$router.resolve({
        path: "/projectdetail/index",
        query: {
          projectId: item.projectId,
        },
      });
      window.open(routerJump.href, "_blank");
      // this.$router.push({path:'/projectdetail',query:{projectId:item.projectId}})
    },
    addproj() {
      const routerJump = this.$router.resolve({
        path: "/addproject/index",
        query: {},
      });
      window.open(routerJump.href, "_blank");
      // this.$router.push({path:'/projectdetail',query:{projectId:item.projectId}})
    },
    findTeammates() {
      this.$router.push("/find/index");
    },
    button(val) {
      this.selectwords.push(val);
      // console.log(this.selectwords);
      this.fetchData();
      this.selectwords = [];
    },
    todorecommendList(){
      recommendList().then((response) => {
        this.recommendLists = response.projectList;
        // this.listLoading = false
      });
    },
    fetchData() {
      this.listLoading = true;
      const params = {
        inputword: this.keyWords,
        selectword: this.selectwords,
      };
      const { inputword, selectword } = params;
      // params
      //console.log("fetchData start");
      getList({
        inputword: inputword,
        selectword: selectword,
      }).then((response) => {
        this.projectList = response.projectList;
        // this.listLoading = false
      });
    },
    getHaveNumber() {
      HaveTeamNumber().then((response) => {
        this.haveNumber = response.numval;
      });
      noTeamNumber().then((response) => {
        this.noNumber = response.numval;
      });
    },
    getbulletin() {
      bulletin().then((res) => {
        //console.log(res, "dddddddd");
        this.bulletinboard = res.announcements;
      });
    },
  },
};
</script>
<style>
.el-card__body {
  /* width: 30%; */
  /* height: 70px;
   */
  border-radius: 10px;

  padding: 0px;
  /* 0 2px 12px 0 rgb(0 0 0 / 10%) */
}
.el-card {
  border: 0;
}
</style>

<style lang="scss" scoped>
//  .el-carousel__item h3 {
//     color: #475669;
//     font-size: 14px;
//     opacity: 0.75;
//     line-height: 150px;
//     margin: 0;
//   }

//   .el-carousel__item:nth-child(2n) {
//      background-color: #99a9bf;
//   }

//   .el-carousel__item:nth-child(2n+1) {
//      background-color: #d3dce6;
//   }

.project_page_box {
  padding: 25px;
  background: #f1f1f1;
  .project_name {
    width: 100%;
    height: 40px;
    font-weight: 600;
    // border: 1px solid red;
  }
  ::-webkit-scrollbar {
    width: 0px;

    height: 0px;

    background-color: #ccc;
  }

  .project_header {
    display: flex;
    justify-content: space-between;
    // border: 1px solid red;
    box-sizing: border-box;
    // height: 150px;
    .card_content {
      height: 150px;
      border-radius: 10px;
      width: 100%;

      .card_top {
        height: 110px;
        font-size: 30px;
        // border: 1px solid red;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #d2707a;
      }

      .card_bottom {
        height: 40px;
        background: #f7d7da;
        color: #d2707a;
        text-align: center;
        line-height: 40px;
      }
      .card_bottoms {
        height: 150px;
        background: #f7d7da;
        color: #d2707a;
        text-align: center;
        line-height: 150px;
      }
      .card_bottom:hover {
        cursor: pointer;
      }
    }

    .card_center {
      width: 100%;
      .card_top {
        height: 110px;

        p {
          // line-height: 10px
          margin: 0;
          padding: 8px 0 0 10px;
        }
        // border: 1px solid red;
        // display: flex;
        // align-items: center;
        // justify-content: center;
        color: #6291cc;
      }
      .card_bottom {
        height: 40px;
        background: #cee2fe;
        color: #6291cc;
        text-align: center;
        line-height: 40px;
      }
      .card_bottomss {
        height: 150px;
        background: #cee2fe;
        color: #6291cc;
        text-align: center;
        line-height: 150px;
      }
      .card_bottom:hover {
        cursor: pointer;
      }
      .card_bottoms {
        height: 40px;
        //  background: #DBDCF8;
        // color: #737DD3;
        color: white;
        text-align: center;
        background-color: #409eff;
        border-color: #409eff;
        line-height: 40px;
      }
      .card_bottoms:hover {
        cursor: pointer;
      }
    }
    .card_end {
      width: 100%;
      .card_top {
        height: 150px;

        .right_Annoucement {
          //  width: 40%;
          display: flex;
          justify-content: center;
          background: #d5eedd;
          height: 30px;
          line-height: 30px;
        }

        .card_top_text {
          height: 120px;
          width: 100%;
          // border: 1px solid red;
          // border:1px solid red;
          overflow-y: scroll;
          padding: 0 0 0 10px;
          word-break: break-all;
          display: -webkit-box;
          // -webkit-line-clamp: 2;
          -webkit-box-orient: vertical;
          // overflow: hidden;
        }
        p {
          // line-height: 10px
          margin: 0;
          padding: 8px 0 0 10px;
        }

        color: #91c09d;
      }
    }
    .teacher_box {
      display: flex;
      width: 70%;
      .teacher_left {
        width: 400px;
        height: 170px;
        // border: 1px solid #ccc;
        border-radius: 10px;
        background: white;
        .teacher_left_title {
          text-align: center;
          padding-top: 30px;
        }
        .teacher_left_button {
          border: 1px solid #ccc;
          box-shadow: 5px 6px 5px #ccc;
          width: 90%;
          margin: 0 auto;
          height: 70px;
          line-height: 70px;
          border-radius: 10px;
          text-align: center;
          margin-top: 16px;
          cursor: pointer;
        }
      }
      .teacher_right {
        width: 400px;
        height: 180px;
        .teacher_right_top {
          width: 400px;
          height: 127px;
          margin-left: 35px;
          border-radius: 10px;
          background: white;
          padding: 5px;
          padding-left: 10px;
        }
        .teacher_right_button {
          margin-left: 166px;
          margin-top: 15px;
        }
      }
    }
    .teacher_box_right {
      width: 29%;

      .content_right_header {
        width: 100%;
        height: 181px;
        border: 2px solid white;
        background: white;
        border-radius: 10px;
        .content_right_text {
          width: 100%;
          box-sizing: border-box;
          padding: 0 10px;
        }
        .right_Annoucement {
          width: 100%;
          text-align: center;
          padding-bottom: 10px;
          border-bottom: 1px solid rgb(235, 232, 232);
        }
      }
    }
    .student_box {
    }
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
        color: #409eff;
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
      // border: 2px solid red;
      height: 610px;
      border-radius: 10px;
      background: white;
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
        height: 454px;
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
          background: #fcfee5;
          border-radius: 10px;
          color: #9fc5f8;
        }
      }
    }
    .content_rights {
      width: 29%;
      // border: 2px solid #ccc;
      // height: 600px;

      border-radius: 10px;
      margin-top: -130px;

      .content_right_header {
        width: 100%;
        // height: 200px;
        // border: 2px solid rgb(205, 22, 22);
        background: white;
        border-radius: 10px;
        .card_end {
          width: 100%;
          .card_top {
            height: 380px;
            // border:1px solid black;

            .right_Annoucement {
              //  width: 40%;
              width: 100%;
              display: flex;
              justify-content: center;
              background: #d5eedd;
              height: 30px;
              line-height: 30px;
            }

            .card_top_text {
              height: 350px;
              // border:1px solid red;
              overflow-y: scroll;
              overflow-y: scroll;
              padding: 0 0 0 10px;
              word-break: break-all;
              display: -webkit-box;
              // -webkit-line-clamp: 2;
              -webkit-box-orient: vertical;
            }
            p {
              // line-height: 10px
              margin: 0;
              padding: 8px 0 0 10px;
            }

            color: #91c09d;
          }
        }
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
        height: 339px;
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
            background: #f7f7ff;
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
              // border:1px solid red;
            }

            img {
              width: 60px;
              height: 60px;
            }
          }
        }
      }
    }
    .content_right {
      width: 29%;
      // border: 2px solid #ccc;
      height: 600px;

      border-radius: 10px;

      .content_right_header {
        width: 100%;
        height: 200px;
        border: 2px solid white;
        background: white;
        border-radius: 10px;
        .card_end {
          width: 100%;
          .card_top {
            height: 150px;

            .right_Annoucement {
              //  width: 40%;
              width: 100%;
              display: flex;
              justify-content: center;
              background: #d5eedd;
              height: 30px;
              line-height: 30px;
            }

            .card_top_text {
              height: 120px;
              // border:1px solid red;
              overflow-y: scroll;
              overflow-y: scroll;
              padding: 0 0 0 10px;
              word-break: break-all;
              display: -webkit-box;
              // -webkit-line-clamp: 2;
              -webkit-box-orient: vertical;
            }
            p {
              // line-height: 10px
              margin: 0;
              padding: 8px 0 0 10px;
            }

            color: #91c09d;
          }
        }
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
            background: #f7f7ff;
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
  .teacher_project {
    width: 100%;
    height: 400px;
  }
}
</style>
<style lang="scss">
.el-carousel__button {
  background: #ccc !important;
}
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
    color: #fff;
    background-color: #9fc5f8;
    border-color: #9fc5f8;
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
#testss .highcharts-container .highcharts-root .highcharts-legend text {
  display: none !important;
  visibility: hidden !important;
}
#testss .highcharts-container .highcharts-root .highcharts-legend rect {
  display: none !important;
  visibility: hidden !important;
}
</style>
