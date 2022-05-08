<template>
  <div class="findTeammates">
    <div class="seach">
      <p>Instructor's recommendation</p>
    </div>
    <div class="listContent">
      <div class="list" v-for="(item, index) in messagetList" :key="index">
        <div class="portrait"><img :src="item.avatar" alt="" /></div>
        <div class="content" @click="goFindDetail(item.email)">
          <p>{{ item.showVal }}</p>
        </div>
        <div class="send">
          <el-button type="primary" @click="goSendMessage(item.email)"
            >Send message</el-button
          >
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { getList, recommendation } from "@/api/message";
export default {
  data() {
    return {
      keyWords: "",
      messagetList: [],
      // images:'../../assets/avatar/',
      images: "/static/img/",
    };
  },
  created() {
    this.fetchData(0);
  },
  methods: {
    goFindDetail(email) {
      const routerJump = this.$router.resolve({
        path: "/teammatesDetail/index",
        query: {
          email: email,
        },
      });
      window.open(routerJump.href, "_blank");
    },
    fetchData(val) {
      //console.log(val);
      // if(val==1&&this.keyWords==''){
      //    this.$message.error('搜索内容不能为空')
      //    return
      // }
      const params = {
        inputword: this.keyWords,
      };
      const { inputword } = params;
      // getList({
      //     inputword: inputword
      // }).then(response => {
      //     console.log(response);
      //     if (response.code == 1) {
      //     this.$message.success(response.msg);
      //     this.messagetList = response.userlist;
      //     this.messagetList.map(item => {
      //         console.log(item.avatar);
      //         item.avatar = require(`../../assets/avatar/${item.avatar}.png`);
      //         console.log(item.avatar);
      //     });
      //     } else {
      //     this.$message.error(response.msg);
      //     }
      // });
      recommendation().then((res) => {
        if (res.code == 1) {
          // = res.userlist;
          res.userlist.forEach(item=>{
            let obj={
              ...item,
              avatar:require(`../../assets/avatar/${item.avatar}.png`)

            }
             this.messagetList.push(obj )
          })
        } else {
          this.$message.error(response.msg);
        }
      });
    },
    goSendMessage(email) {
      const routerJump = this.$router.resolve({
        path: "/message/index",
        query: {
          email: email,
        },
      });
      window.open(routerJump.href, "_blank");
    },
  },
};
</script>
<style lang="scss" scoped>
.findTeammates {
  width: 90%;
  margin: 0 auto;
  .seach {
    width: 100%;
    text-align: center;
    font-size: 28px;
    font-weight: 600;
  }
  .listContent {
    min-height: 500px;
    margin-top: 40px;
    .list {
      width: 100%;
      height: 80px;
      display: flex;
      padding: 3px 10px;
      border: 1px solid #3ab5ff;
      border-radius: 10px;
      margin-top: 20px;
      // background: #6edc7c;
      .portrait {
        width: 66px;
        height: 66px;
        // border: 1px solid #3AB5FF;
        // border-radius: 50px;
        img {
          width: 66px;
          height: 66px;
          // margin-left: 10px;
          // margin-top: 10px;
        }
      }
      .content {
        font-size: 24px;
        line-height: 29px;
        padding-left: 50px;
        color: #feb63d;
        cursor: pointer;
        p {
          padding-left: 10px;
        }
      }
      .send {
        flex: 1;
        margin-top: 16px;
        .el-button--primary {
          float: right;
          line-height: 11px;
          background: #018efe;
          border-color: #018efe;
        }
        .el-button--primary:hover {
          float: right;
          line-height: 11px;
          background: #029342;
          border-color: #029342;
        }
      }
    }
    .list:hover {
      width: 100%;
      height: 80px;
      display: flex;
      padding: 3px 10px;
      border: 3px solid #018efe;
      border-radius: 10px;
      margin-top: 20px;
      background: #86c5ec;
      .content {
        font-size: 24px;
        line-height: 29px;
        padding-left: 50px;
        color: white;
        cursor: pointer;
        p {
          padding-left: 10px;
        }
      }
    }
  }
}
</style>
<style lang="scss">
.findTeammates {
  .seach {
    .el-input__inner {
      border-radius: 20px;
    }
  }
}
</style>
