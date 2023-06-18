<!-- 搜索页面 -->
<template>
  <div>
    <div class="goback">
      <el-button type="danger" @click="goback">返回</el-button>
    </div>

    <div>
      <el-input v-model="search" placeholder="请输入内容"></el-input>
      <el-button type="primary" @click="Search">搜索</el-button>
    </div>
    <!-- 搜索后的 -->
    <div v-if="searchData.length>0">
      <ul v-for="(item, index) in searchData" :key="index">
        <li>
          <span>{{item.contact_name}}</span>
          <span>{{item.address}}</span>
          <span>{{item.phone}}</span>
        </li>
      </ul>
    </div>
    <!-- 搜索前的 -->
    <div v-else>
      <ul v-for="(item, index) in list" :key="index">
        <li>
          <span>{{item.contact_name}}</span>
          <span>{{item.address}}</span>
          <span>{{item.phone}}</span>
        </li>
      </ul>
    </div>
  </div>
</template>