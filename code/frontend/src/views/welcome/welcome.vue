<template>
<div id="background">
  <el-header>
      <div class = "product-name" style = "text-align: left;">Teamup</div>
      <el-button id="login_btn" type="success" @click="gologin" round = "true" align = "right">login</el-button>
  </el-header>

<el-divider></el-divider>

<el-row align="center">
  <el-col :span="12" align="center"><div class="grid-content bg-purple">
    <br/>
    <br/>
    <br/>
    <div class = "title">Join a group project</div>
    <div class = "title">easier with</div>
    <div class = "product-name">Teamup !!</div>
    </div></el-col>
  <el-col :span="12"><div class="grid-content bg-purple-light">
    <div class="block">
      <el-image :src="require('../../assets/Teamwork.png')" :fit="fill"></el-image>
    </div>
    </div></el-col>
</el-row>

    <br/>
    <br/>

<div class = "blue_background">
<el-main>
  <div class = "subtitle">Easy-to-use interface</div>
  <div class = "under_subtitle">One-Click Grouping, Create project, Browser projects</div>
    <div>
  <el-carousel indicator-position="outside">
    <el-carousel-item v-for="item in 4" :key="item">
      <h3>{{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
    </div>

</el-main>
</div>

<el-divider></el-divider>

<div class = "subtitle">Models for different people</div>
<div class = "under_subtitle">Whether you are an instructor or a student, you can use Teamup! </div>


<div class = "index">

    <el-tabs value="For student with idea" type="border-card">
      <el-tab-pane name="For student with idea">
        <span slot="label" class="fontClass">For student with idea</span>
        <el-steps  :active="3" finish-status="process" align-center>
          <el-step title="Publish your project"></el-step>
          <el-step title="Looking for teammates"></el-step>
          <el-step title="Begin to work!"></el-step>
        </el-steps>

      </el-tab-pane>
      <el-tab-pane name="For student without idea">
        <span slot="label" class="fontClass">For student without idea</span>
        <el-steps  :active="3" finish-status="process" align-center>
          <el-step title="Looking for project"></el-step>
          <el-step title="Apply to join"></el-step>
          <el-step title="Begin to work!"></el-step>
        </el-steps>

      </el-tab-pane>
      <el-tab-pane name="For instructor">
        <span slot="label" class="fontClass">For instructor</span>
        <el-steps  :active="3" finish-status="process" align-center>
          <el-step title="Select criterion"></el-step>
          <el-step title="One-click automatic team formation"></el-step>
          <el-step title="Visual view of each groups"></el-step>
        </el-steps>
      </el-tab-pane>
    </el-tabs>


</div>

<br/>
<br/>
<br/>
<br/>

<div class = "darkblue_background">
  <el-footer>Designed by project-team-05-four-z-one-x</el-footer>
</div>

</div>
</template>



<script>
  export default {
    data() {
      return {

      }
    },
    methods: {
    gologin() {
      this.$router.push('/login')
    }
  }
  }


</script>


<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  #login_btn{
    margin: auto 0;
    position: absolute;
    right: 10px;
    top: 20px;
  }

  #background {
  /* background-image:url('../../assets/background.png'); */
  background-repeat: no-repeat;
  background-size: 100% 100%;
  position: fixed;
  width: 100%;
  height: 100%;
  overflow: auto;
  }

  .el-header, .el-footer {
    color: #333;
    text-align: center;
    line-height: 80px;
  }

  .el-main {
    color: #333;
    text-align: center;
    line-height: 50px;
  }
  .el-steps{
     margin: 30px;
  }
  .fontClass{
  font-size:20px;
  font-family: Arial, Helvetica, sans-serif;
  }
  .index{
    margin: 30px;
  }
  .title{
  font-size:50px;
  color: rgb(10, 11, 32);
  font-family: Arial, Helvetica, sans-serif;
  }
  .product-name{
  font-size:50px;
  color: rgb(58, 69, 167);
  font-family: Arial, Helvetica, sans-serif;
  }
  .blue_background{
    background-color: rgb(218, 221, 236);
  }
  .darkblue_background{
    background-color: rgb(102, 140, 245);
  }
  .subtitle{
    text-align:center;
    font-size:30px;
    margin: 20px;
  }
  .under_subtitle{
    text-align:center;
    font-size:18px;
    color: rgb(104, 104, 104);
    margin: 20px;
  }
</style>
