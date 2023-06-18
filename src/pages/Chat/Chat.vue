<template>
    <div class="chat-window">
      <div class="chat-header">
        <div class="chat-title">{{ title }}</div>
        <div class="chat-controls">
          <el-tooltip content="写病历" placement="top">
            <el-button icon="el-icon-notebook-1" circle @click="gotoRecord"></el-button>
          </el-tooltip>
          <el-tooltip content="开票据" placement="top">
            <el-button icon="el-icon-document" circle @click="gotoBill"></el-button>
          </el-tooltip>
          <el-tooltip content="关闭" placement="top">
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
      goTo (path) {
        this.$router.replace(path)
      },
      sendMessage() {
        if (this.newMessage.content) {
          this.messages.push({...this.newMessage })
          this.clearInput()
          this.scrollChatToBottom()
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
        this.goTo('/CaseRecord')
      },
      gotoBill() {
        // 跳转到开票据页面
        console.log('跳转到开票据页面')
        this.goTo('/Bill')
      },
      closeChat() {
        this.$emit('close-chat')
        this.goTo('/home')
      }
    }
  }
  </script>
  
  <style scoped>
  .chat-window {
    position: fixed;
    width: 100%;
    height: 100%;
    background-color: #f1f1f1;
    border-radius: 6px;
    font-size: 14px;
    color: #333;
    z-index: 999;
}

.chat-header {
display: flex;
justify-content: space-between;
align-items: center;
height: 46px;
padding: 0 10px;
background-color: #fff;
color: #333;
border-top-left-radius: 6px;
border-top-right-radius: 6px;
box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
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
height: 250px;
padding: 10px;
overflow-y: auto;
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
border-color: #f1f1f1 transparent transparent transparent;
top: 0;
left: 50%;
margin-left: -10px;
}

.message-bubble.user {
background-color: #007aff;
}

.message-bubble.agent {
background-color: #5cb85c;
}

.chat-footer {
display: flex;
align-items: center;
padding: 10px;
border-top: 1px solid #e6e6e6;
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
</style>