<template>
  <div class="preview_warp">
    <!-- 有数据的情况下 -->
    <div class="preview_data" v-if="previewList&&previewList.length>0">
      <div class="preview_data_title">Group Result</div>
      <div class="preview_content">
        <div class="preview_list">
          <div
            v-for="(item, index) in previewList"
            :key="index"
            class="preview_listItem"
          >
            <div class="preview_listItemTitle" @click="projectNames(item)">{{item.projectName}}</div>
            <div class="preview_listItemcontent">
              <div class="preview_groupeDdata">
                <el-row :gutter="12">
                  <el-col :span="4" v-for="(items, index) in item.teamMemName" :key="index">
                    <el-card shadow="hover" @click.native="teamMemNames(items)" >
                      <div>{{items.name}}</div>
                      <div>{{items.eml}}</div>
                    </el-card>
                  </el-col>
                </el-row>
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
      v-if="previewList && previewList.length==0&&previewIsshow"
    >
      <div class="previewNull_dataSet_title">
        You havent't posted any group recommendation results!!!
      </div>
      <div class="previewNull_dataSet_btn">
        <el-button type="primary" plain>Group students with One click</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import { getList } from "@/api/preview";
export default {
  data() {
    return {
      previewList: [], //数据列表
      previewIsshow:false
    };
  },
  mounted() {
    getList().then((res) => {
     if (res.code == 1) {
        // this.$message.success(res.msg)
        this.previewList = res.projectList;
        this.previewIsshow=true
      } else {
        this.$message.error(res.msg);
      }

      //console.log(res, "ddd");
    });
  },
  methods: {
    goedit() {
         const routerJump = this.$router.resolve({
        path: "/editpreview/editpreview",
        query: {
          isTemp: 0
        }
      });
      window.open(routerJump.href, "_blank");
      // window.open(`/editpreview/editpreview?isTemp=0`);
    },
    golist(){
       const routerJump = this.$router.resolve({
        path: "/preview/preview",
        query: {
          isTemp: 0
        }
      });
      window.open(routerJump.href, "_blank");
    },
    projectNames(item){
        const routerJump = this.$router.resolve({
        path: "/projectdetail/index",
        query: {
          projectId:item.projectId
        }
      });
      window.open(routerJump.href, "_blank");
      // projectId
      // window.open(`/projectdetail/index?projectId=${item.projectId}`)
    },
    teamMemNames(item){
      // console.log(11111);
      // alert("111")
       const routerJump = this.$router.resolve({
        path: "/teammatesDetail/index",
        query: {
          email:item.eml
        }
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
.el-card__body:hover{
     background: #3AB5FF;
     color: #fff;
}
</style>

<style scoped lang="scss">
// .preview_data /deep/ .

// 有数据的情况下
.preview_warp{
  width: 100%;
  background: #DEE2E6;
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
    height: 500px;
    // border:1px solid black;
    box-sizing: border-box;
    padding: 0 20px;
    .preview_list {
      width: 100%;
      height: 100%;
      border: 3px solid #3AB5FF;
      overflow-y: scroll;
      box-sizing: border-box;
      padding: 0 10px;
      .preview_listItem:hover{
          background: #86C5EC;
          color: #fff
      }
      .preview_listItem {
        width: 100%;
        height: 150px;
        border: 3px solid #3AB5FF;
        margin-top: 10px;
        box-sizing: border-box;
        padding: 5px 5px;
        // #86C5EC

        .preview_listItemTitle {
          font-size: 30px;
        }
        .preview_listItemcontent {
          margin-top: 10px;
        }
        .preview_groupeDdata {
        }
      }
    }
  }
  .back_grouping {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 10px;
   
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
