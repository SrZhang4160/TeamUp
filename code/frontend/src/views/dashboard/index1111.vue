<template>
  <div class="dashboard-container">
    Hello World !
    <div class="dashboard-text">name: {{ name }}</div>
    <div class="dashboard-text">eml: {{ eml }}</div>
    <div class="dashboard-text">avatar: {{ avatar }}</div>
    <div class="dashboard-text" style="margin-top: 20px;">type: {{ type }}</div>
    User Information Type: 0. Common user whose information is to be filled in  1. Administrator  2. Common user whose information is to be filled in in details
    <el-form style="margin-top: 10px;">
      <el-form-item v-if="type === 0 " label="填写信息" prop="addinfo">
        <el-button @click="txxx">填写个人信息</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name', 'eml', 'sex', 'type', 'avatar'
    ])
  },
  mounted: function() {
    this.testType()
  },
  methods: {
    txxx() {
      this.$router.push('/txxx/index')
    },
    testType() {
      if (this.type === 0) {
        this.$router.push('/txxx/index')
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
