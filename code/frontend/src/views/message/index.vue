<template>
  <div class="message">
    <div class="messageBox">
      <div class="leftMessage">
        <el-form :model="form" :rules="rules" ref="form">
          <div class="topSend">
            <!-- <div>Send to:</div><el-input v-model="keyWords" ></el-input> -->
            <el-form-item label="Send to:" prop="keyWords">
              <el-input
                v-model.trim="form.keyWords"
                placeholder="Send to"
                @input="inputFrom"
              ></el-input>
            </el-form-item>
          </div>
          <div class="bottomSend">
            <el-input
              v-model="content"
              @input="inputFrom"
              type="textarea"
              :rows="24"
            ></el-input>
          </div>
          <div class="senButton">
            <el-button type="primary" @click="send">Send</el-button>
          </div>
        </el-form>
      </div>
      <!-- @scroll="rightMessageScroll()" -->
      <div class="rightMessage" ref="rightMessage">
        <div
          class="box"
          v-for="(item, index) in projectList"
          :key="index"
          @click="checkRecord(item, index)"
        >
          <div class="chattingList" @click="handleChange(index)">
            {{ item.email }}
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
              <div
                :class="item.isme == 0 ? 'leftContent' : 'rightContent'"
                v-for="(item, index) in messageList"
                :key="index"
              >
                <div class="img"><img :src="item.avatar" alt="" /></div>
                <div>
                  <span style="font-size: 12px; color: #ccc">{{
                    item.sendTime
                  }}</span>
                  <p class="dialogue">{{ item.message }}</p>
                </div>
              </div>
            </div>
          </div>
          <el-badge is-dot class="item" v-if="item.unread >= 1"></el-badge>
          <span v-if="item.unread == 0"></span>
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
  saveword,
  readingdata,
} from "@/api/message";
import { isInnerEmail } from "../../api/utils.js";
import { log } from "util";
import { setTimeout } from "timers";
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
      activeIndexs: -1,
      activeName: "",
      isme: "1",
      projectList: [],
      messageList: [],
      emails: "",
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
    readingdata({}).then(res=>{
      this.form.keyWords=res.sendTo
      this.content=res.sendMessage
      if (this.$route.query.email != null) {
        this.form.keyWords = this.$route.query.email;
      }
    })
    if (this.$route.query.email != null) {
      this.form.keyWords = this.$route.query.email;
    }
    // console.log(readingdata,"readingdatareadingdata");
  },
  methods: {
    inputFrom() {
      //  sendTo: this.form.keyWords,
      //     sendMessage: this.content,
      if (this.form.keyWords.length > 0 && this.content.length > 0) {
        setTimeout(() => {
          localStorage.setItem("keywords", this.form.keyWords);
          localStorage.setItem("content", this.content);
          saveword({
            sendTo: localStorage.getItem("keywords"),
            sendMessage: localStorage.getItem("content"),
          }).then((res) => {
            if (res.code == 1) {
              //console.log(res);
              localStorage.removeItem("keywords");
              localStorage.removeItem("content");
            }
          });
        }, 2000);
      }
    },
    handleChange(val) {
      // this.show=!this.show
      this.activeIndex = this.activeIndex == val ? -1 : val;
    },
    getList() {
      getMessageList({}).then((res) => {
        if (res.code == 1) {
          // this.$message.success(res.msg)
          this.projectList = res.projectList;
        } else {
          this.$message.error(res.msg);
        }
      });
    },
    checkRecord(val, index) {
      this.projectList.forEach((item) => {
        //console.log(item, index);
        this.projectList[index].unread = 0;
      });
      this.emails = val.email;
      const params = {
        email: val.email,
        page: 1,
        size: 20,
      };
      const { email, page, size } = params;
      getMessagerecord({ email: email, page: page, size: size }).then((res) => {
        if (res.code == 1) {
          this.messageList = res.messageList;
          this.messageList.map((item) => {
            item.avatar = require(`../../assets/avatar/${item.avatar}.png`);
          });
        } else {
          this.$message.error(res.msg);
        }
      });
    },
    send() {
      if (this.form.keyWords && this.content) {
        const params = {
          sendTo: this.form.keyWords,
          sendMessage: this.content,
        };
        const { sendTo, sendMessage } = params;
        getSendMessage({ sendTo: sendTo, sendMessage: sendMessage }).then(
          (res) => {
            if (res.code == 1) {
              this.$message.success(res.msg);
              this.content = "";
              if (this.emails != "") {
                const params = {
                  email: this.emails,
                  page: 1,
                  size: 20,
                };
                const { email, page, size } = params;
                getMessagerecord({ email: email, page: page, size: size }).then(
                  (res) => {
                    if (res.code == 1) {
                      this.messageList = res.messageList;
                      this.messageList.map((item) => {
                        item.avatar = require(`../../assets/avatar/${item.avatar}.png`);
                      });
                    } else {
                      this.$message.error(res.msg);
                    }
                  }
                );
              }
            } else {
              this.$message.error(res.msg);
            }
          }
        );
      } else if (this.form.keyWords && !this.content) {
        this.$message.error("An empty message cannot be sent");
      } else {
        this.$message.error("Please check the required message");
      }
    },
  },
};
</script>
<style lang="scss" scoped>
.message {
  .messageBox {
    width: 90%;
    height: 680px;
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
        height: 520px;
        margin-top: 20px;
      }
      .senButton {
        width: 100px;
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
        min-height: 100px;
        border: 1px solid #fcfee5;
        border-top: none;
        background: #fcfee5;
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
.el-badge {
  position: absolute;
  right: -4px;
  top: 14px;
}
.el-badge__content.is-dot {
  width: 15px;
  height: 15px;
}
</style>
