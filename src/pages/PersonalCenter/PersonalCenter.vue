<template>
    <div id="PersonalCenter">
      <el-container class="home-container">
        <el-header>
          <div>
            <span>个人中心</span>
          </div>
          <el-button type="info" @click="logout">
              退出
          </el-button></el-header>
        <el-container>
          <el-aside width="200px">
            <el-menu
              background-color="#e4f5ef"
              text-color="#000000"
              active-text-color="#02a774"
              unique-opened
              >
              <!-- 一级菜单 -->
            <el-submenu index="1">
              <!-- 一级菜单模板 -->
              <template slot="title">
                <i class="el-icon-user"></i>
                <span>个人信息</span>
              </template>
                <el-menu-item index="1-1">个人信息管理</el-menu-item>
            </el-submenu>
  
            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-chat-dot-square"></i>
                <span>诊断心得</span>
              </template>
                <el-menu-item index="2-1">就诊反馈</el-menu-item>
            </el-submenu>
  
            <el-submenu index="3">
              <!-- 一级菜单模板 -->
              <template slot="title">
                <i class="el-icon-warning-outline"></i>
                <span>关于我们</span>
              </template>
                <el-menu-item index="3-1">版本信息</el-menu-item>
            </el-submenu>
  
            </el-menu>
          </el-aside>
          <el-main></el-main>
        </el-container>
      </el-container>
    </div>
  </template>
  
  
  <script>
  export default {
    name: "app"
  }
  </script>
  
  
  <style>
  .home-container{
    height:100vh;
  }
  .el-header{
    background-color: #02a774;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #fff;
    font-size: 20px;
    
  }
  .el-aside{
    background-color: #e4f5ef;
  }
  .el-main{
    background-color: #e4e4e4;
  }
  </style>