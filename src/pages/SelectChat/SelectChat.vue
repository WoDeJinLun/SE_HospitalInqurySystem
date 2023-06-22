<template>
    <div>
      <h1>请选择问诊方式</h1>
      <button @click="redirectToAI">AI问诊</button>
      <button @click="redirectToHuman">人工问诊</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      redirectToAI() {
        // 在这里编写跳转到AI问诊页面的逻辑
        console.log('跳转到AI问诊页面');
        this.$router.push('/chat')
      },
      redirectToHuman() {
        // 在这里编写跳转到人工问诊页面的逻辑
        console.log('跳转到人工问诊页面');
        this.$router.push('/doctorchat')
      },

    }
  };
  </script>
  
  <style scoped>
  h1 {
    text-align: center;
  }
  button {
    margin: 10px;
    padding: 5px 10px;
  }
  </style>
  