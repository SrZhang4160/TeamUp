<template>
  <div class="addstinfo-container">
    1填写学生信息
    <el-form ref="addstinfo" :model="addstinfo" label-width="120px">
      <el-form-item label="real name" prop="rename">
        <el-input
          ref="rename"
          v-model="addstinfo.rename"
          placeholder="Rename"
          name="rename"
          type="text"
          tabindex="1"
          auto-complete="on"
        />
      </el-form-item>
      <el-form-item label="sex">
        <el-select v-model="addstinfo.sex" placeholder="please select your sex">
          <el-option label="man" value="0" />
          <el-option label="wuman" value="1" />
          <el-option label="other" value="2" />
        </el-select>
      </el-form-item>
      <el-form-item label="birthday">
        <el-col :span="11">
          <el-date-picker v-model="addstinfo.birthday" type="date" placeholder="Birthday" style="width: 100%;" />
        </el-col>
      </el-form-item>

      <el-form-item label="hobby">
        <el-checkbox-group v-model="addstinfo.hobby">
          <el-checkbox label="XXX" name="type" />
          <el-checkbox label="YYY" name="type" />
          <el-checkbox label="ZZZ" name="type" />
          <el-checkbox label="OOO" name="type" />
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="grade">
        <el-radio-group v-model="addstinfo.grade">
          <el-radio label="a" />
          <el-radio label="b" />
          <el-radio label="c" />
          <el-radio label="d" />
        </el-radio-group>
      </el-form-item>
      <el-form-item label="remark">
        <el-input v-model="addstinfo.remark" type="textarea" />
      </el-form-item>
      <el-form-item label="agree">
        <el-switch v-model="addstinfo.agree" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click.native.prevent="onSubmitTxxx">submit</el-button>
        <el-button v-if="2 < 1 " @click="onCancel">Cancel</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'Addstinfo',
  data() {
    return {
      addstinfo: {
        rename: '',
        sex: '',
        birthday: '',
        agree: false,
        hobby: [],
        grade: '',
        remark: ''
      },
      loading: false,
      redirect: undefined
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {
    onSubmitTxxx() {
      this.loading = true
      // this.addstinfo
      this.$store.dispatch('user/addstinfo', this.addstinfo).then(() => {
        this.$router.push({ path: this.redirect || '/viewxx/index' }) // 跳转到查看页
        this.loading = false
      }).catch(() => {
        this.loading = false
      })
    },
    onCancel() {
      this.$message({
        message: 'cancel!',
        type: 'warning'
      })
    }
  }
}
</script>

<style scoped>
.line{
  text-align: center;
}
</style>
