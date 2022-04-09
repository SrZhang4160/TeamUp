<template>
  <div class="navbar">
    <hamburger :is-active="sidebar.opened" class="hamburger-container" @toggleClick="toggleSideBar" />

    <breadcrumb class="breadcrumb-container" />

    <div class="right-menu">
      <el-dropdown class="avatar-container" trigger="click">
        <div class="avatar-wrapper">
          <img v-if="avatar === 'chicken'" src="@/assets/avatar/chicken.png" class="user-avatar">
          <img v-if="avatar === 'cow'" src="@/assets/avatar/cow.png" class="user-avatar">
          <img v-if="avatar === 'dog'" src="@/assets/avatar/dog.png" class="user-avatar">
          <img v-if="avatar === 'dragon'" src="@/assets/avatar/dragon.png" class="user-avatar">
          <img v-if="avatar === 'horse'" src="@/assets/avatar/horse.png" class="user-avatar">
          <img v-if="avatar === 'mice'" src="@/assets/avatar/mice.png" class="user-avatar">
          <img v-if="avatar === 'monkey'" src="@/assets/avatar/monkey.png" class="user-avatar">
          <img v-if="avatar === 'pig'" src="@/assets/avatar/pig.png" class="user-avatar">
          <img v-if="avatar === 'rabbit'" src="@/assets/avatar/rabbit.png" class="user-avatar">
          <img v-if="avatar === 'sheep'" src="@/assets/avatar/sheep.png" class="user-avatar">
          <img v-if="avatar === 'snake'" src="@/assets/avatar/snake.png" class="user-avatar">
          <img v-if="avatar === 'tiger'" src="@/assets/avatar/tiger.png" class="user-avatar">
          <img v-if="avatar === 'undefined'" src="@/assets/avatar/undefined.png" class="user-avatar">
          <img v-if="avatar === 'xrr'" src="@/assets/avatar/xrr.png" class="user-avatar">

          <i class="el-icon-caret-bottom" />
        </div>
        <el-dropdown-menu slot="dropdown" class="user-dropdown">
          <router-link to="/">
            <el-dropdown-item>
              Home
            </el-dropdown-item>
          </router-link>
          <a target="_blank" href="https://github.com/PanJiaChen/vue-admin-template/">
            <el-dropdown-item>Github</el-dropdown-item>
          </a>
          <a target="_blank" href="https://panjiachen.github.io/vue-element-admin-site/#/">
            <el-dropdown-item>Docs</el-dropdown-item>
          </a>
          <el-dropdown-item divided @click.native="logout">
            <span style="display:block;">Log Out</span>
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Breadcrumb from '@/components/Breadcrumb'
import Hamburger from '@/components/Hamburger'

export default {
  components: {
    Breadcrumb,
    Hamburger
  },
  computed: {
    ...mapGetters([
      'sidebar',
      'avatar'
    ])
  },
  methods: {
    toggleSideBar() {
      this.$store.dispatch('app/toggleSideBar')
    },
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    }
  }
}
</script>

<style lang="scss" scoped>
.navbar {
  height: 50px;
  overflow: hidden;
  position: relative;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0,21,41,.08);

  .hamburger-container {
    line-height: 46px;
    height: 100%;
    float: left;
    cursor: pointer;
    transition: background .3s;
    -webkit-tap-highlight-color:transparent;

    &:hover {
      background: rgba(0, 0, 0, .025)
    }
  }

  .breadcrumb-container {
    float: left;
  }

  .right-menu {
    float: right;
    height: 100%;
    line-height: 50px;

    &:focus {
      outline: none;
    }

    .right-menu-item {
      display: inline-block;
      padding: 0 8px;
      height: 100%;
      font-size: 18px;
      color: #5a5e66;
      vertical-align: text-bottom;

      &.hover-effect {
        cursor: pointer;
        transition: background .3s;

        &:hover {
          background: rgba(0, 0, 0, .025)
        }
      }
    }

    .avatar-container {
      margin-right: 30px;

      .avatar-wrapper {
        margin-top: 5px;
        position: relative;

        .user-avatar {
          cursor: pointer;
          width: 40px;
          height: 40px;
          border-radius: 10px;
        }

        .el-icon-caret-bottom {
          cursor: pointer;
          position: absolute;
          right: -20px;
          top: 25px;
          font-size: 12px;
        }
      }
    }
  }
}
</style>
