import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login', // 登录
    component: () => import('@/views/login/index'),
    hidden: true
  },
  {
    path: '/adduser', // 注册
    component: () => import('@/views/login/adduser.vue'),
    hidden: true
  },
  {
    path: '/welcome', // 欢迎页
    component: () => import('@/views/welcome/welcome.vue'),
    hidden: true
  },
  {
    path: '/404', // 404
    component: () => import('@/views/404'),
    hidden: true
  },
  {
    path: '/', // 主页
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: {
        title: 'Main Lobby',
        icon: 'dashboard'
      }
    }]
  },
  {
    path: '/viewxx', // personal info
    component: Layout,
    children: [{
      path: 'index',
      name: 'Personal info',
      component: () => import('@/views/stinfo/viewxx.vue'),
      meta: {
        title: 'Personal info',
        icon: 'form'
      }
    }]
  },

  {
    path: '/txxx/index', // getstudent info
    component: () => import('@/views/stinfo/txxx.vue'),
    hidden: false
  },

  // {
  //   path: '/txxx', // get student info
  //   component: Layout,
  //   hidden: true,
  //   children: [{
  //     path: 'index',
  //     name: 'txxx',
  //     component: () => import('@/views/stinfo/txxx.vue'),
  //     meta: {
  //       title: 'add detailed information',
  //       icon: 'form'
  //     }
  //   }]
  // },

  // {
  //   path: '/viewxx', // 查看学生详情
  //   component: Layout,
  //   hidden: true,
  //   children: [{
  //     path: 'index',
  //     name: 'viewxx',
  //     component: () => import('@/views/stinfo/viewxx.vue'),
  //     meta: {
  //       title: 'view detailed information',
  //       icon: 'form'
  //     }
  //   }]
  // },

  // {
  //  path: '/project',
  //  component: () => import('@/views/project/project.vue'),
  //  hidden: true
  // },
  {
    path: '/project', // 主页 项目列表
    component: Layout,
    hidden: true,
    children: [{
      path: 'index',
      name: 'project',
      component: () => import('@/views/dashboard/index'),
      meta: {
        title: 'project LIST',
        icon: 'form'
      }
    }]
  },
  {
    path: '/projectdetail', // 项目详情
    component: Layout,
    hidden: true,
    children: [{
      path: 'index',
      name: 'projectdetail',
      component: () => import('@/views/project/projectDetail.vue'),
      meta: {
        title: 'project detail',
        icon: 'form'
      }
    }]
  },
  {
    path: '/find', // 查询用户列表
    component: Layout,
    children: [{
      path: 'index',
      name: 'Find Teammates',
      component: () => import('@/views/findTeammates/index'),
      meta: {
        title: 'Find Teammates',
        icon: 'form'
      }
    }]
  },
  {
    path: '/mygroup', // 我的项目
    component: Layout,
    children: [{
      path: 'index',
      name: 'My group',
      component: () => import('@/views/project/projectDetail.vue'),
      meta: {
        title: 'My group',
        icon: 'form'
      }
    }]
  },


  {
    path: '/projectEdit', // 修改项目
    component: Layout,
    hidden: true,
    children: [{
      path: 'index',
      name: 'projectEdit',
      component: () => import('@/views/project/projectEdit.vue'),
      meta: {
        title: 'project Edit',
        icon: 'form'
      }
    }]
  },
  {
    path: '/addproject', // 新增项目
    component: Layout,
    hidden: true,
    children: [{
      path: 'index',
      name: 'addproject',
      component: () => import('@/views/project/addproject.vue'),
      meta: {
        title: 'project add',
        icon: 'form'
      }
    }]
  },
  {
    path: '/opupxx', // 修改学生详情
    component: Layout,
    hidden: true,
    children: [{
      path: 'index',
      name: 'viewxx',
      component: () => import('@/views/stinfo/opupxx.vue'),
      meta: {
        title: 'update detailed information',
        icon: 'form'
      }
    }]
  },
  {
    path: '/example', // 系统自带用不上
    component: Layout,
    redirect: '/example/table',
    name: 'Example',
    hidden: true,
    meta: {
      title: 'Example',
      icon: 'el-icon-s-help'
    },
    children: [{
      path: 'table',
      name: 'Table',
      component: () => import('@/views/table/index'),
      meta: {
        title: 'Table',
        icon: 'table'
      }
    },
    {
      path: 'tree',
      name: 'Tree',
      component: () => import('@/views/tree/index'),
      meta: {
        title: 'Tree',
        icon: 'tree'
      }
    }]
  },

  {
    path: '/message', // 消息列表
    component: Layout,
    children: [{
      path: 'index',
      name: 'Message',
      component: () => import('@/views/message/index'),
      meta: {
        title: 'Message',
        icon: 'form'
      }
    }]
  },
  {
    path: '/teammatesDetail', // 学生详情
    component: Layout,
    hidden: true,
    children: [{
      path: 'index',
      name: 'teammatesDetail',
      component: () => import('@/views/findTeammates/teammatesDetail.vue'),
      meta: {
        title: 'teammates detail',
        icon: 'form'
      }
    }]
  },
  {
    path: '/contact', // Contact
    component: Layout,
    children: [{
      path: 'index',
      name: 'Contact',
      component: () => import('@/views/contact/index.vue'),
      meta: {
        title: 'Contact',
        icon: 'form'
      }
    }]
  },
  // 系统自带 用不上
  {
    path: '/form', // 系统自带 用不上
    component: Layout,
    hidden: true,
    children: [{
      path: 'index',
      name: 'Form',
      component: () => import('@/views/form/index'),
      meta: {
        title: 'Form',
        icon: 'form'
      }
    }]
  },

  {
    path: '/nested', // 系统自带 用不上
    component: Layout,
    redirect: '/nested/menu1',
    name: 'Nested',
    hidden: true,
    meta: {
      title: 'Nested',
      icon: 'nested'
    },
    children: [{
      path: 'menu1',
      component: () => import('@/views/nested/menu1/index'), // Parent router-view
      name: 'Menu1',
      meta: {
        title: 'Menu1'
      },
      children: [{
        path: 'menu1-1',
        component: () => import('@/views/nested/menu1/menu1-1'),
        name: 'Menu1-1',
        meta: {
          title: 'Menu1-1'
        }
      }, {
        path: 'menu1-2',
        component: () => import('@/views/nested/menu1/menu1-2'),
        name: 'Menu1-2',
        meta: {
          title: 'Menu1-2'
        },
        children: [{
          path: 'menu1-2-1',
          component: () => import('@/views/nested/menu1/menu1-2/menu1-2-1'),
          name: 'Menu1-2-1',
          meta: {
            title: 'Menu1-2-1'
          }
        },
        {
          path: 'menu1-2-2',
          component: () => import('@/views/nested/menu1/menu1-2/menu1-2-2'),
          name: 'Menu1-2-2',
          meta: {
            title: 'Menu1-2-2'
          }
        }]
      }, {
        path: 'menu1-3',
        component: () => import('@/views/nested/menu1/menu1-3'),
        name: 'Menu1-3',
        meta: {
          title: 'Menu1-3'
        }
      }]
    },
    {
      path: 'menu2',
      component: () => import('@/views/nested/menu2/index'),
      name: 'Menu2',
      meta: {
        title: 'menu2'
      }
    }
    ]
  },

  {
    path: 'external-link', // 系统自带 用不上
    hidden: true,
    component: Layout,
    children: [{
      path: 'https://panjiachen.github.io/vue-element-admin-site/#/',
      meta: {
        title: 'External Link',
        icon: 'link'
      }
    }]
  },

  // 404 page must be placed at the end !!!
  {
    path: '*',
    redirect: '/404',
    hidden: true
  }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({
    y: 0
  }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
