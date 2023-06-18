<template>
    <div id="register">
      <!-- <img src="./assets/logo.png">
      <div>
        <el-button @click="startHacking">Start</el-button>
      </div> -->
      <!-- <el-row>
        <el-button type="primary" plain>预约挂号</el-button>
        <el-button type="primary" plain>当天挂号</el-button>
      </el-row>
      <el-row>
        <el-col :span="24"><div class="grid-content bg-purple-light"></div></el-col>
      </el-row> -->
      <el-menu default-active="menu1" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="menu1">
        预约挂号
      </el-menu-item>
      <el-menu-item index="menu2">当天挂号</el-menu-item>
      <!-- <el-submenu index="3">
        <template slot="title">我的工作台</template>
        <el-menu-item index="3-1">选项1</el-menu-item>
        <el-menu-item index="3-2">选项2</el-menu-item>
        <el-menu-item index="3-3">选项3</el-menu-item>
        <el-submenu index="3-4">
          <template slot="title">选项4</template>
          <el-menu-item index="3-4-1">选项1</el-menu-item>
          <el-menu-item index="3-4-2">选项2</el-menu-item>
          <el-menu-item index="3-4-3">选项3</el-menu-item>
        </el-submenu>
      </el-submenu> -->
      <!-- <el-menu-item index="3" disabled>消息中心</el-menu-item> -->
      <!-- <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item> -->
    </el-menu>
    <div v-if="currentMenu === 'menu1'">
      <el-row>
        <el-col :span="24"><div class="grid-content bg-purple-light"></div></el-col>
      </el-row> 
      <div class="block">
        <span class="demonstration">请选择挂号科室</span>
        <el-cascader
          v-model="value"
          :options="options"
          @change="handleChange"></el-cascader>
      </div>
  
    </div>
    <div v-if="currentMenu === 'menu2'">
      <el-row>
        <el-col :span="24"><div class="grid-content bg-purple-light"></div></el-col>
      </el-row> 
      <div class="block">
        <span class="demonstration">请选择挂号科室</span>
        <el-cascader
          v-model="value"
          :options="options"
          @change="handleChange"></el-cascader>
      </div>
    </div>
    <div class="line"></div>
    
  </div>
  
  </template>
  
  <script>
    export default {
      data() {
        return {
          value: [],
          options: [{
            value: 'duoxueke',
            label: '多学科联合诊治',
            children: [{
              value: 'duoxuekejiefanglu',
              label: '多学科联合诊治-解放路',
            }]
          }, {
            value: 'quanke',
            label: '全科医学科',
            children: [{
              value: 'quankejiefanglu',
              label: '全科医学科门诊-解放路',
            }]
          },
          {
            value: 'neike',
            label: '内科',
            children: [{
              value: 'neifenmi',
              label: '内分泌科',
            }, {
              value: 'xinxueguan',
              label: '心血管科',
              
            }, {
              value: 'shenjing',
              label: '神经内科',
            }, {
              value: 'xueye',
              label: '血液内科',
              
            }, {
              value: 'huxi',
              label: '呼吸内科',
              
            }, {
              value: 'xiaohua',
              label: '消化内科',
            }, {
              value: 'yichuan',
              label: '医学遗传科',
            }, {
              value: 'fengshi',
              label: '风湿免疫科',
            }, {
              value: 'guomin',
              label: '过敏科（变态反应科）',
            }, {
              value: 'shenzang',
              label: '肾脏内科',
            }, {
              value: 'jingshen',
              label: '精神科',
            }, {
              value: 'ganran',
              label: '感染性疾病科',
            }]
          }, {
            value: 'waike',
            label: '外科',
            children: [{
              value: 'ruxian',
              label: '乳腺外科'
            }, {
              value: 'zhengxing',
              label: '整形科'
            }, {
              value: 'gandanyi',
              label: '肝胆胰外科'
            }, {
              value: 'xueguan',
              label: '血管外科'
            }, {
              value: 'dachang',
              label: '大肠外科'
            }, {
              value: 'puwai',
              label: '普外科'
            }, {
              value: 'jiazhuangxian',
              label: '甲状腺外科'
            }, {
              value: 'weichang',
              label: '胃肠外科'
            }, {
              value: 'gu',
              label: '骨科'
            }, {
              value: 'miniao',
              label: '泌尿外科'
            }, {
              value: 'shenjingwai',
              label: '神经外科'
            }, {
              value: 'xiongwai',
              label: '胸外科'
            }]
          }, {
            value: 'fuchanke',
            label: '妇产科'
          }, {
            value: 'erke',
            label: '儿科'
          }],
          currentMenu: 'menu1'
        };
      },
      methods: {
        handleSelect(key) {
          this.currentMenu = key;
        },
        handleChange(value) {
          console.log(value);
        }
      }
    }
  </script>
  
  <style>
  #register {
    font-family: Helvetica, sans-serif;
    text-align: center;
  }
  .el-row {
      margin-bottom: 20px;
      &:last-child {
        margin-bottom: 0;
      }
    }
    .el-col {
      border-radius: 4px;
    }
    .bg-purple-dark {
      background: #99a9bf;
    }
    .bg-purple {
      background: #d3dce6;
    }
    .bg-purple-light {
      background: #e5e9f2;
    }
    .grid-content {
      border-radius: 4px;
      min-height: 36px;
    }
    .row-bg {
      padding: 10px 0;
      background-color: #f9fafc;
    }
  </style>
  