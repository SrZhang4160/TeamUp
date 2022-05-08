<template>
  <!-- :style="backgourndStyle" -->
  <div class="login-container" :style="backgourndStyle">
    <el-form
      ref="loginForm"
      :model="loginForm"
      :rules="loginRules"
      class="login-form"
      auto-complete="on"
      label-position="left"
    >
      <div class="title-container">
        <h1 class="title">TeamUp!!!</h1>
      </div>

      <div class="title-input">
        <h3 class="title">Email:</h3>
      </div>
      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="email" />
        </span>
        <el-input
          ref="username"
          v-model="loginForm.username"
          placeholder="Please enter email address"
          name="username"
          type="text"
          tabindex="1"
          auto-complete="on"
        />
      </el-form-item>
      <div class="title-input">
        <h3 class="title">Password:</h3>
      </div>
      <el-form-item prop="password">
        <span class="svg-container">
          <svg-icon icon-class="password" />
        </span>
        <el-input
          :key="passwordType"
          ref="password"
          v-model="loginForm.password"
          :type="passwordType"
          placeholder="Please enter password"
          name="password"
          tabindex="2"
          auto-complete="on"
          @keyup.enter.native="handleLogin"
        />
        <span class="show-pwd" @click="showPwd">
          <svg-icon
            :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'"
          />
        </span>
      </el-form-item>

      <el-button
        :loading="loading"
        type="primary"
        style="width: 100%; margin-bottom: 30px"
        @click.native.prevent="handleLogin"
      >
        LOGIN
      </el-button>

      <div class="tips" style="margin-left: 30px">
        <span style="margin-right: 20px">Don't have an accont ?</span>
        <a class="asp" @click="goadduser">Create a TeamUp account!!!</a>
      </div>
      <!-- <div class="tips" style="margin-left: 30px">
        <span style="margin-right: 20px">Forgot your password?</span>
        <a class="asp" @click="goreset">Reset it!</a>
      </div> -->
    </el-form>
  </div>
</template>

<script>
import { validUsername } from "@/utils/validate";
import { log } from "util";

export default {
  name: "Login",
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error("Please enter the correct user name"));
      } else {
        callback();
      }
    };
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error("The password can not be less than 6 digits"));
      } else {
        callback();
      }
    };
    return {
      loginForm: {
        username: "",
        password: "",
      },
      indexI: localStorage.getItem("index") || 0,
      loginRules: {
        username: [
          { required: true, trigger: "blur", validator: validateUsername },
        ],
        password: [
          { required: true, trigger: "blur", validator: validatePassword },
        ],
      },
      loading: false,
      passwordType: "password",
      redirect: undefined,
      backgourndStyle:
        "background-image: url('http://bookstore.zealon.cn/00-4.jpg'); background-repeat: round; height: 100vh;",
    };
  },
  mounted() {
    let cHeight =
      window.outerHeight - (window.outerHeight - window.innerHeight);
    // 存放要换的图片
    let imgs = [
      require("@/assets/loginbg/1.webp"),
      require("@/assets/loginbg/2.webp"),
      require("@/assets/loginbg/3.webp"),
      require("@/assets/loginbg/4.webp"),
      require("@/assets/loginbg/5.webp"),
    ];
    console.log(this.indexI,"111this.indexI")

    let imgName = imgs[this.indexI]; //进行计算随机
    this.backgourndStyle =
      "background-image:url('" +
      imgName +
      "'); background-repeat: round; height:" +
      cHeight +
      "px;";
    if (this.indexI < 4) {
      this.indexI++;

    } else {
      this.indexI = 0;
    }
       localStorage.setItem("index", this.indexI);
   
    console.log(this.indexI, "打印下表");
    // console.log(this.backgourndStyle())
  },
  computed: {
    // backgourndStyle:function(){
    //     // 计算body可用高度
    //     return style
    // }
  },
  watch: {
    $route: {
      handler: function (route) {
        this.redirect = route.query && route.query.redirect;
      },
      immediate: true,
    },
  },
  methods: {
    showPwd() {
      if (this.passwordType === "password") {
        this.passwordType = "";
      } else {
        this.passwordType = "password";
      }
      this.$nextTick(() => {
        this.$refs.password.focus();
      });
    },
    goadduser() {
      this.$router.push("/adduser");
    },
    goreset() {
      this.$message({
        message: "Coming soon!",
        type: "info",
      });
    },
    handleLogin() {
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          this.loading = true;
          this.$store
            .dispatch("user/loginMod", this.loginForm)
            .then(() => {
              this.$router.push("/dashboard"); // 登录成功之后重定向到首页
              this.loading = false;
            })
            .catch(() => {
              this.loading = false;
            });
        } else {
          console.log("error submit!!");
          return false; // 登录失败提示错误
        }
      });
    },
  },
};
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg: #e5e5e5b7;
$light_gray: black;
$cursor: black;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
$bg: #2d3a4b;
$dark_gray: #889aa4;
$light_gray: #eee;
a:hover {
  color: #409eff;
}

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    height: 550px;
    max-width: 100%;
    padding: 50px 35px 0;
    margin: 100px auto 0;
    overflow: hidden;
    background: #fff;
    // border:1px solid red;
  }

  .tips {
    font-size: 14px;
    color: black;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
    asp {
      margin-right: 5px;
      cursor: pointer;
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 48px;
      color: black;
      margin: 0px auto 30px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .title-input {
    position: relative;

    .title {
      font-size: 26px;
      color: black;
      margin: 20px auto 10px auto;
      text-align: left;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }
}
</style>
