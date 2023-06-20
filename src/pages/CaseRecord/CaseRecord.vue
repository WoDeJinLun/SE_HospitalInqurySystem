<template>
  <div class="medical-record">
    <h2>病历录入</h2>
    <form>
      <div class="form-group">
        <label for="name">患者姓名</label>
        <input id="name" type="text" v-model="patientName">
      </div>
      <div class="form-group">
        <label for="gender">性别</label>
        <select id="gender" v-model="gender">
          <option value="男">男</option>
          <option value="女">女</option>
        </select>
      </div>
      <div class="form-group">
        <label for="age">年龄</label>
        <input id="age" type="number" v-model="age">
      </div>
      <div class="form-group">
        <label for="diagnosis">诊断结果</label>
        <textarea id="diagnosis" v-model="diagnosis"></textarea>
      </div>
      <div class="form-group">
        <label for="treatment">治疗方案</label>
        <textarea id="treatment" v-model="treatment"></textarea>
      </div>
    </form>
    <button class="send-btn" @click="sendRecord">保存病历</button>
    <button class="send-btn" @click="goBack">返回</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      patientName: "",
      gender: "男",
      age: "",
      diagnosis: "",
      treatment: "",
    };
  },
  methods: {
    sendRecord() {
      this.$message.success("保存成功");
      // TODO: 发送病历信息
      console.log({
        patientName: this.patientName,
        gender: this.gender,
        age: this.age,
        diagnosis: this.diagnosis,
        treatment: this.treatment,
      });
    },
    goBack() {
      this.$router.push("/chat");
    },
  },
};
</script>

<style>
.medical-record {
  display: flex;
  flex-direction: column;
  background-color: #d0f0c0;
  padding: 16px;
  border-radius: 5px;
  max-width: 500px;
  margin: 0 auto;
}

h2 {
  font-size: 24px;
  margin-bottom: 20px;
  margin-top: 20px;
  text-align: center;
  color: #448f1d;
}

.form-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 20px;
}

.form-group label {
  flex: 0 0 120px;
  font-size: 16px;
  color: #448f1d;
}

.form-group input,
.form-group select,
.form-group textarea {
  flex: 1;
  height: 30px;
  border-radius: 3px;
  border: 1px solid #448f1d;
  padding: 5px;
  font-size: 16px;
  margin-left: 30px;
}

.form-group textarea {
  height: 100px;
  resize: none;
}

.send-btn {
  width: 200px;
  height: 40px;
  background-color: #448f1d;
  color: #fff;
  border-radius: 3px;
  margin-top: 20px;
  border: none;
  font-size: 18px;
  cursor: pointer;
}

.send-btn:hover {
  background-color: #32741c;
}
</style>
