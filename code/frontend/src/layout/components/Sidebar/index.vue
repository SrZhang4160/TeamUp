<template>
  <div :class="{ 'has-logo': showLogo }">
    <logo v-if="showLogo" :collapse="isCollapse" />
    <el-scrollbar wrap-class="scrollbar-wrapper">
      <el-menu
        :default-active="activeMenu"
        :collapse="isCollapse"
        :background-color="variables.menuBg"
        :text-color="variables.menuText"
        :unique-opened="false"
        :active-text-color="variables.menuActiveText"
        :collapse-transition="false"
        mode="vertical"
      >
        <sidebar-item
          v-for="route in routes"
          :key="route.path"
          :item="route"
          :isShow="isShow"
          :unread="unread"
          :base-path="route.path"
        />
      </el-menu>
    </el-scrollbar>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Logo from './Logo'
import SidebarItem from './SidebarItem'
import variables from '@/styles/variables.scss'
import { getInfo } from "@/api/userapi";
export default {
  data(){
    return{
      isShow: true,
      unread:null,
    }
  },
  created(){


      let token=JSON.parse(localStorage.getItem('token'))
      getInfo(token).then((res) => {
        // console.log('isUnread:'+res.isUnread)
        if(res.isUnread!=0 || null){
          // console.log('isUnread:hongDian')
          this.isShow = true
          this.unread=res.isUnread
        }else{
          // console.log('isUnread:noHong')
          this.isShow = false
        }
      });
    
  },
  components: { SidebarItem, Logo },
  computed: {
    ...mapGetters([
      'sidebar'
    ]),
    routes() {
      return this.$router.options.routes
    },
    activeMenu() {
      const route = this.$route
      const { meta, path } = route
      // if set path, the sidebar will highlight the path you set
      if (meta.activeMenu) {
        return meta.activeMenu
      }
      return path
    },
    showLogo() {
      return this.$store.state.settings.sidebarLogo
    },
    variables() {
      return variables
    },
    isCollapse() {
      return !this.sidebar.opened
    }
  }
}
</script>
<style>
.el-submenu__title {
  display: flex;
  align-items: center;
}
.el-submenu__title span{
  white-space: normal;
  word-break: break-all;
  line-height: 20px;
  flex: 1;
  padding-right: 20px;
}
 
.el-menu-item {
  display: flex;
  align-items: center;
  padding-right: 20px!important;
}
.el-menu-item span {
  white-space: normal;
  word-break: break-all;
  line-height: 20px;
  flex: 1;
}
</style>
