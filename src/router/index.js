/*
*路由器对象模块
**/

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../pages/Home/Home'
import Grades from '../pages/Grades/Grades'
import Profile from '../pages/Profile/Profile'
import Login from '../pages/Login/Login'
import Register from '../pages/Register/Register'
import Feedback from '../pages/Feedback/Feedback'
import PersonalCenter from '../pages/PersonalCenter/PersonalCenter'
import AnotherProfile from '../pages/AnotherProfile/AnotherProfile'
import Chat from '../pages/Chat/Chat.vue'
import CaseRecord from '../pages/CaseRecord/CaseRecord.vue'
import Bill from '../pages/Bill/Bill.vue'
import SelectChat from "../pages/SelectChat/SelectChat.vue"
import docterchat from "../pages/doctorchat/doctorchat.vue"
// 声明使用插件
Vue.use(VueRouter)

export default new VueRouter({
  // 所以路由
  routes: [
    {
      path: '/home',
      component: Home,
      meta: {
        showFooter: true
      }
    },
    {
      path: '/grades',
      component: Grades,
      meta: {
        showFooter: true
      }
    },
    {
      path: '/aprofile',
      component: Profile,
      meta: {
        showFooter: true
      }
    },
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/login',
      component: Login
    },
    {
      path:'/register',
      component: Register
    },
  
    {
      path:'/leftuptest',
      component:Feedback
      
    },
    {
      path:'/PersonalCenter',
      component:PersonalCenter
    },

    {
      path:'/profile',
      component: PersonalCenter
    },
    {
      path: '/chat',
      name: 'chat',
      component: Chat
    },
    {
      path: '/chatdoctor',
      component: Chat
    },
    {
      path: '/CaseRecord',
      name: 'CaseRecord',
      component: CaseRecord
    },
    {
      path: '/Bill',
      name: 'Bill',
      component: Bill
    },
    {
      path: '/SelectChat',
      name: 'SelectChat',
      component: SelectChat
    },
    {
      path: '/doctorchat',
      name:'doctorchat',
      component: docterchat
    }
  ]
})
