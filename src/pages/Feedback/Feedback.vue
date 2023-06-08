<template>
    <div id="feedback">
      <div class="private-container">
        <div class="message-box">
          <div class="title">
            <span>就诊心得反馈</span>
          </div>
          <!-- 信息更改 -->
          <el-form  label-width="100px" class="message-form">
            <!-- 姓名 -->
            <el-form-item label="反馈内容:" >
              <el-input
                type="textarea"
                :rows="18"
                placeholder="请输入内容"
                v-model="textarea">
              </el-input>
            </el-form-item>
          </el-form>
          <div class="button">
            <el-button type="success">提交</el-button>
            <el-button type="info">清除</el-button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'app'
  }
  </script>
  
  <style>
  .private-container{
    background-color: #e4e4e4;
    height: 100%;
  }
  
  .message-box{
    width: 1500px;
    height: 700px;
    background-color: #fff;
    border-radius: 4px;
    position: absolute;
    left:50%;
    top:50%;
    transform: translate(-50%,-50%);
  }
  
  .message-form{
    position: absolute;
    left:50%;
    top:50%;
    transform: translate(-50%,-50%);
    width: 100%;
    padding: 0 400px;
    box-sizing: border-box;
  }
  
  .button{
    position: absolute;
    left:50%;
    top:85%;
    transform: translate(-50%,-50%);
  }
  
  .title{
    position: absolute;
    left:50%;
    top:10%;
    transform: translate(-50%,-50%);
    color: #02a774;
    font-size: 25px;
  }
  
  </style>
  