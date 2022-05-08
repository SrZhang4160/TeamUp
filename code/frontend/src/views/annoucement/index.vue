<template>
  <div class="message">
    <div class="messageBox">
      <div class="leftMessage">
        <el-form :model="form" :rules="rules" ref="form">
          <div class="topSend">
            <!-- <div>Send to:</div><el-input v-model="keyWords" ></el-input> -->
          </div>
          <div class="inputs">
            <el-input v-model="input" placeholder="Name"></el-input>
          </div>
          <div class="bottomSend">
            
            <el-input v-model="content" type="textarea" :rows="20" placeholder="Content*:"></el-input>
          </div>
          <div class="senButton">
            <el-button type="primary" @click="send">Add new announcement</el-button>
          </div>
        </el-form>
      </div>
      <!-- @scroll="rightMessageScroll()" -->
      <div
        class="rightMessage"
        ref="rightMessage"
        
      >
      <div class="rightMessage_Title" style="font-size:20px;">Announcement History:</div>
        <div
          class="box"
          v-for="(item, index) in projectList"
          :key="index"
          @click="checkRecord(item,index)"
        >
          <div class="chattingList" @click="handleChange(index)">
            {{ item.name }} {{item.releaseTime}}
            <span v-if="activeIndex == index"
              ><i class="el-icon-remove-outline"></i
            ></span>
            <span v-else><i class="el-icon-circle-plus-outline"></i></span>
          </div>
          <div
            class="chattingContent"
            v-if="activeIndex == index"
            ref="bscroll"
          >
            <div class="content">
            {{messageList.val}}
              <!-- <div
                :class="item.isme == 0 ? 'leftContent' : 'rightContent'"
                v-for="(item, index) in messageList"
                :key="index"
              >
                <div class="img"><img :src="item.avatar" alt="" /></div>
                <div>
                  <span style="font-size:12px; color:#ccc;">{{item.sendTime}}</span>
                <p class="dialogue">{{ item.message }}</p>
                </div>
              </div> -->
            </div>
          </div>
          <!-- <el-badge
            is-dot
            class="item"
            v-if="item.unread >= 1"
          ></el-badge> -->
          <!-- <span v-if="item.unread == 0"></span> -->
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import BScroll from "better-scroll";
import {
  getMessageList,
  getMessagerecord,
  getSendMessage,
  sendnotice,//发送公告
  noticelist,//公告列表
  noticedetail,//公告详情


} from "@/api/message";
import { isInnerEmail } from "../../api/utils.js";
import { log } from "util";
export default {
  data() {
    return {
      form: {
        keyWords: "",
      },
      hongdian: true,
      content: "",
      show: true,
      activeIndex: -1,
      activeIndexs:-1,
      activeName: "",
      isme: "1",
      projectList: [],
      messageList: {},
      input:"",
      rules: {
        keyWords: [
          {
            required: true,
            message: "Please enter email address",
            trigger: ["blur", "change"],
          },
          {
            type: "email",
            message: "Please enter the correct email address",
            trigger: ["blur", "change"],
          },
          { validator: isInnerEmail, trigger: "blur" },
        ],
      },
    };
  },
  created() {
    this.getList();
    if (this.$route.query.email) {
      this.form.keyWords = this.$route.query.email;
    }
  },
  methods: {
    
    handleChange(val) {
      // this.show=!this.show
      this.activeIndex = this.activeIndex == val ? -1 : val;
    },
    getList() {
      noticelist({}).then((res) => {
        if (res.code == 1) {
          // this.$message.success(res.msg)
          this.projectList = res.announcements;
        } else {
          this.$message.error(res.msg);
        }
      });
    },
    checkRecord(val,index) {
      // this.projectList.forEach((item)=>{
      //   console.log(item,index);
      //   this.projectList[index].unread=0
      // })
      const params = {
        id: val.id,
        page: 1,
        size: 20,
      };
      const { id, page, size } = params;
      noticedetail({ id}).then((res) => {
        if (res.code == 1) {
          this.messageList = res.announcement;
          // this.messageList.map((item) => {
          //   item.avatar = require(`../../assets/avatar/${item.avatar}.png`);
          // });
        } else {
          this.$message.error(res.msg);
        }
      });
    },
    send() {

      if (this.input && this.content) {
        
  
        const params = {
          sendTo: this.input,
          sendMessage: this.content,
        };
        const { sendTo, sendMessage } = params;
        sendnotice({ name: sendTo, val: sendMessage }).then(
          (res) => {
            if (res.code == 1) {
              this.$message.success(res.msg);
              this.content = "";
              this.input=""
              this.getList()
            } else {
              this.$message.error(res.msg);
            }
          }
        );
      } else if (this.input && !this.content) {
        this.$message.error("An empty message cannot be sent");
      } else {
        this.$message.error("Please check the required message");
      }
    },
  },
};
</script>
<style lang="scss" scoped>
.inputs{
width: 90%;
box-sizing: border-box;
margin: 0 auto;
border:1px solid #3AB5FF;
border-radius: 5px;



}
.message {
  .messageBox {
    width: 90%;
    height: 550px;
    margin: 0 auto;
    display: flex;
    margin-top: 40px;
    .leftMessage {
      width: 40%;
      border: 1px solid #ccc;
      // border-radius: 10px;
      .topSend {
        // display: flex;
        margin-top: 20px;
        .el-form-item__label {
          width: 100px;
          line-height: 40px;
          font-size: 20px;
          font-weight: 600;
          padding-left: 20px;
        }
        .el-input {
          width: 70%;
        }
      }
      .bottomSend {
        width: 90%;
        margin: 0 auto;
        border: 2px solid #3ab5ff;
        border-radius: 10px;
        height: 450px;
        margin-top: 20px;
      }
      .senButton {
        width: 215px;
        margin: 0 auto;
        margin-top: 20px;
        margin-bottom: 20px;
      }
    }
    .rightMessage {
      width: 60%;
      border: 1px solid #ccc;
      border-left: none;
      padding: 20px 30px;
      // height: 740px;
      overflow-y: scroll;
      .box {
        position: relative;
      }
      .chattingList {
        width: 100%;
        height: 50px;
        border: 1px solid #86c5ec;
        line-height: 50px;
        padding: 0px 20px;
        font-size: 20px;
        text-align: center;
        margin-top: 20px;
        background: #86c5ec;
        color: white;
        cursor: pointer;
        i {
          font-size: 24px;
          float: right;
          line-height: 47px;
        }
      }
      .chattingContent {
        min-height: 200px;
        border: 3px solid #3AB5FF;
        border-top: none;
        // background: #fcfee5;

        // position: absolute;
        top: 40px;
        padding: 10px;
        img {
          width: 50px;
          height: 50px;
        }
        .leftContent {
          display: flex;
          flex-direction: row;
          .dialogue {
            max-width: 477px;
            min-height: 50px;
            word-wrap: break-word;
            border: 1px solid #ccc;
            margin-left: 10px;
            padding: 10px;
            margin-top: 3px;
            // line-height: 23px;
          }
        }
        .rightContent {
          display: flex;
          flex-direction: row-reverse;

          .dialogue {
            max-width: 477px;
            min-height: 50px;
            word-wrap: break-word;
            border: 1px solid #ccc;
            margin-right: 10px;
            padding: 10px;
            margin-top: 3px;
            // line-height: 23px;
          }
        }
      }
    }
  }
}
</style>
<style lang="scss">
.bottomSend {
  .el-textarea__inner {
    width: 100%;
    // line-height: 18 !important;
    border: none;
  }
}
.rightMessage {
  .el-collapse-item {
    padding-top: 10px;
  }
  .el-collapse-item__arrow {
    display: none !important;
  }
  .el-icon-circle-plus-outline {
    font-size: 24px;
  }
  .el-icon-remove-outline {
    font-size: 24px;
  }
}
.topSend {
  .el-form-item__label {
    width: 130px;
    line-height: 40px;
    font-size: 20px;
    font-weight: 600;
    padding-left: 20px;
  }
  .el-form-item__error {
    left: 150px;
  }
}
.el-badge{
  position: absolute;
  right: -4px;
  top: 14px;

}
.el-badge__content.is-dot {
  width: 15px;
  height: 15px;
}
</style>
