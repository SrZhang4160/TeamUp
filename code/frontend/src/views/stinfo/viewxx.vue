<template>
  <div class="stinfo-container">
      <h2 align="center">
    Personal info
  </h2>
  <el-form label-position="top" ref="stinforef" label-width="160px" class="stinfoForm">
    <el-form-item label="name:" prop="name">
      <template slot="label">
        <i class="el-icon-user"></i>
        Name
      </template>
      {{ stinfo.name }}
    </el-form-item>
    <el-divider></el-divider>

    <el-form-item label="email:" prop="email">
      <template slot="label">
        <i class="el-icon-user"></i>
        E-mail
      </template>
      {{ stinfo.email }}
    </el-form-item>
    <el-divider></el-divider>

    <el-form-item label="Major:" prop="major">
      <template slot="label">
        <i class="el-icon-suitcase"></i>
        Major
      </template>
      {{ stinfo.major }}
    </el-form-item>
    <el-divider></el-divider>

    <el-form-item label="Grade:" prop="grade">
      <template slot="label">
        <i class="el-icon-school"></i>
        Grade
      </template>
      {{ stinfo.grade }}
    </el-form-item>
    <el-divider></el-divider>

    <el-form-item label="Leadership Interest:" prop="leadInt">
      <template slot="label">
        <i class="el-icon-magic-stick"></i>
        Leadership Interest
      </template>
      {{ stinfo.leadInt }}
    </el-form-item>
    <el-divider></el-divider>

    <el-form-item label="Type of End Product:" prop="prod">
      <template slot="label">
        <i class="el-icon-bangzhu"></i>
        Type of End Product
      </template>
      {{ stinfo.prod }}
    </el-form-item>
    <el-divider></el-divider>

    <el-form-item label="Related Experience:" prop="exep">
      <template slot="label">
        <i class="el-icon-discover"></i>
        Related Experience
      </template>
      {{ stinfo.exep }}
    </el-form-item>
<el-divider></el-divider>

    <el-form-item label="Field of Interest:" prop="fieldInt">
      <template slot="label">
        <i class="el-icon-suitcase"></i>
        Field of Interest
      </template>

        <el-form-item
          v-for="(interest,index) in stinfo.fieldInt"
          :key="index"
        >
          {{interest}}

        </el-form-item>

    </el-form-item>
<el-divider></el-divider>



    <el-form-item label="skillLevel:" prop="skillLevel">
      <template slot="label">
        <i class="el-icon-suitcase"></i>
        skillLevel
      </template>

        <el-form-item
          v-for="(skill_level) in stinfo.skillLevel"
          :key="skill_level.key"
        >
          {{skill_level.skillName}} : {{skill_level.level}}

        </el-form-item>

    </el-form-item>
<el-divider></el-divider>

    <el-form-item label="Prefer to work with:" prop="prefer">
      <template slot="label">
        <i class="el-icon-suitcase"></i>
        Prefer to work with
      </template>
      {{ stinfo.prefer }}
    </el-form-item>
<el-divider></el-divider>

    <el-form-item label="Prefer NOT to work with:" prop="preferNot">
      <template slot="label">
        <i class="el-icon-suitcase"></i>
        Prefer NOT to work with
      </template>
      {{ stinfo.preferNot }}
    </el-form-item>
<el-divider></el-divider>

    <el-form-item label="mbti personality:" prop="mbti">
      <template slot="label">
        <i class="el-icon-suitcase"></i>
        mbti personality
      </template>
      {{ stinfo.mbti }}
    </el-form-item>
    <el-divider></el-divider>

    <el-form-item label="Project:" prop="mbti">
      <template slot="label">
        <i class="el-icon-suitcase"></i>
        Project:
      </template>
      <div v-if="userProject.projectId==undefined">
        <div>You have not joined any project! Brower the main lobby for project info!</div>
      </div>
      <div v-else>

        <div>Project name : {{ userProject.projectName }}</div>
      </div>

    </el-form-item>

    <el-form-item  style="text-align: center;">
        <el-button type="primary" class="submit-btn" @click="changeInfo()">Update</el-button>
    </el-form-item>

    </el-form>

<!--

    <el-form ref="stinforef" label-width="120px">
      <el-form-item label="real name:" prop="eml">
        {{ stinfo.eml }}
      </el-form-item>
      <el-form-item label="sex:">
        {{ stinfo.sex }}
      </el-form-item>
      <el-form-item label="birthday:">
        {{ dateFormat(stinfo.birthday) }}
      </el-form-item>

      <el-form-item label="hobby:">
        {{ stinfo.hobby }}
      </el-form-item>
      <el-form-item label="grade:">
        {{ stinfo.grade }}
      </el-form-item>
      <el-form-item label="remark:">
        {{ stinfo.remark }}
      </el-form-item>
      <el-form-item label="agree:">
        {{ stinfo.agree }}
      </el-form-item>
    </el-form> -->

  </div>
</template>




<script>
import { getstinfo_api,query_profile_api } from '@/api/stinfoapi'

export default {
  data() {
    return {
      stinfo: {},
      userProject: {}
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      query_profile_api().then(response => {
        this.stinfo = response.userDetails;
        this.userProject = response.userProject;
        console.log("test!!!!!!!!!!!!!!!!!!!!!!!");
        console.log(this.userProject);

      })
    },

  changeInfo(){
    this.$router.push('/opupxx/index')
  },

    dateFormat: function(time) {
      var date = new Date(time)
      var year = date.getFullYear()
      // eslint-disable-next-line
      var month= date.getMonth()+1<10 ? "0" +(date.getMonth()+1) : date.getMonth()+1;
      // eslint-disable-next-line
      var day=date.getDate()<10 ? "0"+date.getDate() : date.getDate();
      return year + '-' + month + '-' + day
    }
  }
}
</script>

<style scoped>
.stinfoForm {
  width: 100%;
  margin-top: 20px;
  padding: 20px 20px 1px 20px;
  /* border-radius: 5px;
  box-shadow: 0px 5px 10px #cccc; */
}

.stinfo-container{
  width: 80%;
  margin:0 auto;
  margin-top: 40px;
  margin-bottom: 40px;
  padding: 20px 20px 2px 20px;
  border-radius: 5px;
  box-shadow: 0px 5px 10px #cccc;
    /* text-align: center; */
}
.el-form-item{

}
</style>
