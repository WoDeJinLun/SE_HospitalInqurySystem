<template>


  <div class="container">
     
    <div class="medical-record" v-show="showLog">
      <h1>病历录入</h1>
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
        <button class="send-btn" @click="sendRecord">保存病历</button>
      </form>
    </div>

    <div class="bill-page" v-show="showBill">
      <!-- Add your bill component here -->
      <div class="invoice">
        <h1>药品票据</h1>
        <form>
          <div>
            <label for="name">患者姓名</label>
            <input type="text" id="name" v-model="patientName">
          </div>
          <div>
            <label for="drug">药品名称</label>
            <input type="text" id="drug" v-model="drugName">
          </div>
          <div>
            <label for="price">药品单价</label>
            <input type="number" id="price" v-model="drugPrice">
          </div>
          <div>
            <label for="quantity">药品数量</label>
            <input type="number" id="quantity" v-model="drugQuantity">
          </div>
          <div>
            <label for="total">总价格</label>
            <input type="number" id="total" v-model="totalPrice" disabled>
          </div>
        </form>
        <div class="invoice-preview">
          <h3>医院收据</h3>
          <div class="invoice-details">
            <p>患者姓名：{{ patientName }}</p>
            <p>药品名称：{{ drugName }}</p>
            <p>药品单价：{{ drugPrice }} 元/个</p>
            <p>药品数量：{{ drugQuantity }}</p>
            <p>总价格：{{ totalPrice }} 元人民币</p>
          </div>
        </div>
        <button class="save-btn" @click="saveInvoice">保存票据</button>
      </div>
    </div>
    <div class="chat-window">
      <div class="chat-header">
        <div class="chat-title">{{ title }}</div>
        <div class="chat-controls">
          <el-tooltip content="log" placement="top">
            <el-button icon="el-icon-notebook-1" circle @click="gotoRecord"></el-button>
          </el-tooltip>
          <el-tooltip content="bill" placement="top">
            <el-button icon="el-icon-document" circle @click="gotoBill"></el-button>
          </el-tooltip>
          <el-tooltip content="close" placement="top">
            <el-button icon="el-icon-close" circle @click="closeChat"></el-button>
          </el-tooltip>
        </div>
      </div>
      <div class="chat-body" ref="chatBody">
        <ul>
          <li v-for="(message, index) in messages" :key="index" :class="message.sender">
            <div class="message-bubble">
              <div class="message-content">{{ message.content }}</div>
            </div>
          </li>
        </ul>
      </div>
      <div class="chat-footer">
        <div class="message-input">
          <div class="input-wrapper">
            <el-input
              placeholder="请输入消息内容"
              clearable
              class="message-text"
              v-model="newMessage.content"
              @keyup.enter="sendMessage"
            ></el-input>
          </div>
          <el-button type="primary" circle class="send-btn" @click="sendMessage">
            <span>发送</span>
          </el-button>
        </div>
      </div>
      <div class="quick-messages">
        <el-button type="text" width=12 @click="sendQuickMessage('医生您好！')">医生您好！</el-button>
        <el-button type="text" @click="sendQuickMessage('这个检查该如何做？')">这个检查该如何做？</el-button>
      </div>
      <div class="quick-messages">
        <el-button type="text" @click="sendQuickMessage('我讲一下自己的病情')">我讲一下自己的病情</el-button>
        <el-button type="text" @click="sendQuickMessage('好的，谢谢医生')">好的，谢谢医生</el-button>

        <!-- Add more quick message buttons as needed -->
      </div>
 
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatWindow',
  props: {
    title: {
      type: String,
      default: '问诊'
    }
  },
  data() {
    return {
      gender: "男",
      age: "",
      diagnosis: "",
      treatment: "",
      showBill:false,
      showLog:false,
      patientName: "",
      drugName: "",
      drugPrice: "",
      drugQuantity: "",
      totalPrice: "",
      messages: [
        { sender: 'agent', content: '您好' }
      ],
      newMessage: {
        sender: 'user',
        content: ''
      }
    }
  },
  methods: {
    
    calculateTotalPrice() {
      if (this.drugPrice && this.drugQuantity) {
        this.totalPrice = (this.drugPrice * this.drugQuantity).toFixed(2);
      }
    },
    // 保存票据
    saveInvoice() {
      this.$message.success("保存成功");
      // TODO: 保存到数据库或本地存储等
      console.log({
        patientName: this.patientName,
        drugName: this.drugName,
        drugPrice: this.drugPrice,
        drugQuantity: this.drugQuantity,
        totalPrice: this.totalPrice,
      });
    },
    goTo(path) {
      this.$router.replace(path)
    },
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
    sendMessage() {
      if (this.newMessage.content) {
        this.messages.push({ ...this.newMessage })
        this.clearInput()
        this.scrollChatToBottom()
      }
    },
    sendQuickMessage(msg) 
    {
      if (msg) {
        this.messages.push({ sender: 'user', content: msg });
        this.scrollChatToBottom();
      }
    },

    clearInput() {
      this.newMessage.content = ''
    },
    scrollChatToBottom() {
      this.$nextTick(() => {
        if (this.$refs.chatBody) {
          this.$refs.chatBody.scrollTop = this.$refs.chatBody.scrollHeight
        }
      })
    },
    gotoRecord() {
      // 跳转到写病历页面
      console.log('跳转到写病历页面')
      this.showBill = false; 
      this.showLog = !this.showLog;
    },
    gotoBill() {
      // 跳转到开票据页面
      console.log('跳转到开票据页面')
      this.showBill = !this.showBill;
      this.showLog = false;

    },
    closeChat() {
      this.$emit('close-chat')
      this.goTo('/home')
    }
  },
  
  computed: {
    invoiceTitle() {
      return `${this.patientName} 的药品票据`;
    },
  },
  watch: {
    // 监听药品单价和数量的变化
    drugPrice: "calculateTotalPrice",
    drugQuantity: "calculateTotalPrice",
  },
}

</script>

<style scoped>

.invoice {
  display: flex;
  flex-direction: column;
  background-color: #d0f0c0;
  padding: 16px;
  border-radius: 5px;
  max-width: 500px;
  margin: 0;
  margin-left: 0;
}

h1 {
  font-size: 32px;
  margin-bottom: 20px;
  margin-top: 20px;
  text-align: center;
  color: #448f1d;
}

h3 {
  font-size: 24px;
}

form div {
  display: flex;
  margin-bottom: 16px;
}

form label {
  flex: 0 0 120px;
  font-size: 16px;
  font-weight: bold;
  margin-top: 8px;
  margin-bottom: 5px;
  margin-left: 10px;
  color: #448f1d;
}

form input[type="text"],
form input[type="number"] {
  padding: 8px;
  border-radius: 3px;
  border: 1px solid #448f1d;
  font-size: 16px;
  flex: 1;
  margin-right: 20px;
}

form input[type="number"]:disabled {
  background-color: #f0f0f0;
}

.invoice-preview {
  margin-top: 24px;
  padding: 16px;
  border: 1px solid #448f1d;
  border-radius: 5px;
  background-color: #eaf7e0;
}

.invoice-preview h3 {
  margin-bottom: 8px;
  text-align: center;
  color: #448f1d;
}

.invoice-preview p {
  margin-bottom: 4px;
  color: #448f1d;
}


h2 {
  font-size: 24px;
  margin-bottom: 20px;
  margin-top: 20px;
  text-align: center;
  color: #448f1d;
}
.save-btn {
  width: 150px;
  height: 40px;
  background-color: #448f1d;
  color: #fff;
  border-radius: 3px;
  margin-top: auto;
  margin-bottom: 16px;
  border: none;
  font-size: 18px;
  cursor: pointer;
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
.save-btn:hover {
  background-color: #32741c;
}
.container {
  display: flex;
  height: 100vh;
}

.bill-page {
  flex: 1;
  padding: 16px;
  order: 1;
  z-index:1;
}

.chat-window {
  position: fixed;
  width: 100%;
  height: 100%;
  max-width: 400px;
  max-height: 600px;
  bottom: 0;
  right: 0;
  background-color: #fff;
  border-radius: 6px;
  font-size: 14px;
  color: #333;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  order: 2; /* Add this line */
  z-index:2;
}

/* Responsive styles */
@media screen and (min-width: 480px) {
  .chat-window {
    max-width: 600px; /* Adjust the maximum width for larger screens */
    max-height: 800px; /* Adjust the maximum height for larger screens */
  }
}

@media screen and (min-width: 768px) {
  .chat-window {
    max-width: 800px; /* Adjust the maximum width for even larger screens */
    max-height: 1000px; /* Adjust the maximum height for even larger screens */
  }
}

.quick-messages {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}

.quick-messages:first-child {
  justify-content: center;
}




.quick-messages el-button {
  margin: 5px 5px 5px 5px;
}
.quick-messages:nth-child(2) .el-button:first-child {
  margin-right: 100px;
}
.chat-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 46px;
  padding: 0 10px;
  background-color: #f3f3f3;
  color: #333;
  border-top-left-radius: 6px;
  border-top-right-radius: 6px;
}

.chat-title {
  flex-grow: 1;
  font-size: 16px;
  font-weight: bold;
}

.chat-controls {
  display: flex;
  align-items: center;
}

.chat-controls el-button {
  margin-left: 10px;
}

.chat-body {
  height: 280px;
  padding: 10px;
  overflow-y: auto;
  background-color: #f9f9f9;
}

.chat-body ul {
  padding: 0;
  margin: 0;
}

.chat-body li {
  list-style: none;
  margin-bottom: 10px;
}

.chat-body li.user .message-bubble {
  display: flex;
  flex-direction: row-reverse;
}

.message-bubble {
  padding: 10px;
  border-radius: 20px;
  display: inline-block;
  max-width: 95%;
  word-break: break-word;
  color: #333;
}

.message-bubble:after {
  content: "";
  position: absolute;
  border-style: solid;
  border-width: 15px 10px 0 10px;
  border-color: #f9f9f9 transparent transparent transparent;
  top: 0;
  left: 50%;
  margin-left: -10px;
}

.message-bubble.user {
  background-color: #007aff;
  color: #fff;
}

.message-bubble.agent {
  background-color: #5cb85c;
  color: #fff;
}

.chat-footer {
  display: flex;
  align-items: center;
  padding: 10px;
  border-top: 1px solid #e6e6e6;
  background-color: #f3f3f3;
}

.message-input {
  display: flex;
  align-items: center;
  width: 100%;
}

.input-wrapper {
  flex-grow: 1;
  margin-right: 10px;
}

.message-text {
  border-radius: 4px;
  border: 1px solid #e6e6e6;
}

.send-btn {
  margin-left: 10px;
  font-size: 16px;
  text-align: center;
  line-height: normal;
}

.medical-record {
  display: flex;
  flex-direction: column;
  background-color: #d0f0c0;
  padding: 16px;
  border-radius: 5px;
  width:500px;
  margin: 0;
  margin-left: 20px;
  margin-bottom: 100px;
  margin-top: 20px;
}

.medical-record .textbox {
    margin-bottom: 20px;
  }

  /* Adjust the width */
  .medical-record .textbox input[type="text"] {
    width: 1000px;
    box-sizing: border-box;
  }
  .medical-record .container {
    width: 200%;
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
  height: 90px;
  width: 50%;
  resize: auto;
}

</style>
