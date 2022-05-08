<template>
  <div class="preview_warp">
    <!-- 有数据的情况下 -->
    <div class="preview_data" v-if="previewList && previewList.length > 0">
      <div class="preview_data_title">Group Result Preview</div>
      <div class="preview_content">
        <div class="preview_list">
          <div
            v-for="(item, index) in previewList"
            :key="index"
            class="preview_listItem"
          >
            <!-- <div class="preview_listItemTitle">{{item.groupNo}}</div> -->
            <div class="preview_listItemcontent">
              <div class="preview_groupeDdata">
                <div class="preview_groupeDdata_left">{{ item.groupNo }}</div>
                <div class="preview_groupeDdata_right">
                  <div
                    class="preview_groupeDdataList"
                    v-for="(items, index) in item.teamMemName"
                    :key="index"
                  >
                    <div
                      class="contents"
                      :style="{background:color[index]}"
                      @click="teamMemNames(items)"
                    >
                      <div class="contents_left">
                        <img
                          src="@/assets/email.png"
                          style="width: 30px; height: 30px"
                          alt=""
                        />
                      </div>
                      <div class="contents_right">
                        <div>{{ items.name }}</div>
                        <div class="eml">{{ items.eml }}</div>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- <el-row :gutter="12">
                  <el-col :span="4" v-for="(items, index) in item.teamMemName" :key="index">
                    <el-card shadow="hover" @click.native="teamMemNames(items)" >
                      <div>{{items.name}}</div>
                      <div>{{items.eml}}</div>
                    </el-card>
                  </el-col>
                </el-row> -->
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="back_grouping">
        <!-- <el-button type="primary" plain @click="goedit"
          >Return to criteria page and group again</el-button
        > -->
        <div>
          <el-button type="primary" plain @click="golist"
            >Post recommendations to students</el-button
          >
        </div>
        <div>
          <el-button type="primary" plain @click="goedit"
            >Return to criteria page and group again</el-button
          >
        </div>
      </div>
    </div>
    <!-- 数据为空的时候 -->
    <div
      class="previewNull_dataSet"
      v-if="previewList && previewList.length == 0 && previewIsshow"
    >
      <div class="previewNull_dataSet_title">
        You havent't posted any group recommendation results!!!
      </div>
      <div class="previewNull_dataSet_btn">
        <el-button type="primary" plain
          >Group students with One click</el-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import { getListView, savePreview } from "@/api/preview";
export default {
  data() {
    return {
      previewList: [], //数据列表
      previewIsshow: false,
       color: {
      "0":"#FEF6E0",
      "1":"#E8EBED",
      "2":"#F0ECF9",
      "3":"#EEFDFD",
      "4":"#E8EBED",
      "5":"#FEF6E0",
      "6":"#F0ECF9",
      },
    };
  },
  mounted() {
    getListView().then((res) => {
      if (res.code == 1) {
        // this.$message.success(res.msg)
        this.previewList = res.projectList;
        this.previewIsshow = true;
      } else {
        this.$message.error(res.msg);
      }

      console.log(res, "ddd");
    });
  },
  methods: {
    golist() {
      savePreview().then((res) => {
        if (res.code == 1) {
          this.$router.push({
            path: "/postedGroup/postedGroup",
            query: {
              isTemp: 0,
            },
          });
        }
      });
    },
    goedit() {
      this.$router.push({
        path: "/editpreview/editpreview",
        query: {
          isTemp: 1,
        },
      });
    },
    projectNames(item) {
      const routerJump = this.$router.resolve({
        path: "/projectdetail/index",
        query: {
          projectId: item.projectId,
        },
      });
      window.open(routerJump.href, "_blank");
      // projectId
      // window.open(`/projectdetail/index?projectId=${item.projectId}`)
    },
    teamMemNames(item) {
      console.log(11111);
      // alert("111")
      const routerJump = this.$router.resolve({
        path: "/teammatesDetail/index",
        query: {
          email: item.eml,
        },
      });
      window.open(routerJump.href, "_blank");
      // window.open(`/teammatesDetail/index?email=${item.eml}`,"blank")

      // /teammatesDetail/index?email=XXXX%40JHU.EDU
    },
  },
};
</script>
<style>
.el-card__body {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
/* .el-card__body:hover{
     background: #3AB5FF;
     color: #fff;
} */
</style>

<style scoped lang="scss">
// .preview_data /deep/ .
.preview_warp {
  width: 92%;
  height: calc(100vh - 50px);
  background: #dee2e6;
  box-sizing: border-box;
  border-radius: 10px;
  margin: 0 auto;
  // 有数据的情况下
  .preview_data {
    width: 100%;
    height: 100%;
    // border: 1px solid red;
    .preview_data_title {
      width: 100%;
      display: flex;
      justify-content: center;
      height: 80px;
      // border: 1px solid black;
      font-size: 40px;
      align-items: center;
    }
    .preview_content {
      height: 450px;
      // border:1px solid black;
      box-sizing: border-box;
      padding: 0 20px;
      .preview_list {
        width: 100%;
        height: 100%;
        // border: 3px solid #3AB5FF;
        overflow-y: scroll;
        overflow-x: hidden;
        box-sizing: border-box;
        padding: 0 10px;
        // .preview_listItem:hover{
        //     background: #86C5EC;
        //     color: #fff
        // }
       .preview_listItem {
          width: 100%;
          height: 100px;
          background: #fff;
          // border: 1px solid red;
          margin-top: 10px;
          box-sizing: border-box;
          padding: 5px 5px;
          border-radius: 10px;
          // #86C5EC

          .preview_listItemTitle {
            font-size: 30px;
          }
          .preview_listItemcontent {
            // margin-top: 10px;
          }
          .preview_groupeDdata {
            width: 100%;
            height: 100px;
            // border: 1px solid red;
            display: flex;
            align-items: center;
            .preview_groupeDdata_left {
              margin-left: 30px;
            }
            .preview_groupeDdata_right {
              display: flex;
              .preview_groupeDdataList {
                margin-left: 10px;

                .contents {
                  width: 140px;
                  height: 60px;
                  // border: 1px solid red;
                  border-radius: 8px;
                  display: flex;
                  // flex-direction: column;
                  align-items: center;
                  justify-content: space-between;
                  box-sizing: border-box;
                  padding: 0 0 0 10px;
                  .contents_left {
                    display: flex;
                    align-items: center;
                  }
                  .contents_right {
                    width: 67%;
                    // border: 1px solid red;
                    .texts{
                      font-size: 12px;

                      word-break: break-all;
                      display: -webkit-box;
                      -webkit-line-clamp: 1;
                      -webkit-box-orient: vertical;
                      overflow: hidden;
                    }
                    .eml {
                      // width: 50px;
                      font-size: 12px;

                      word-break: break-all;
                      display: -webkit-box;
                      -webkit-line-clamp: 1;
                      -webkit-box-orient: vertical;
                      overflow: hidden;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    .back_grouping {
      width: 100%;
      display: flex;
      justify-content: center;
      margin-top: 20px;

      :nth-child(2) {
        margin-left: 10px;
      }
    }
  }
  // 无数据的样式
  .previewNull_dataSet {
    .previewNull_dataSet_title {
      width: 100%;
      display: flex;
      justify-content: center;
      margin-top: 150px;
      box-sizing: border-box;
      padding: 0 35%;
      font-size: 35px;
      // border: 1px solid red;
      text-align: center;
      line-height: 45px;
    }
    .previewNull_dataSet_btn {
      width: 100%;
      display: flex;
      justify-content: center;
      margin-top: 80px;
    }
  }
}
</style>
