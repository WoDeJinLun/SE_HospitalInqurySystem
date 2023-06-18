<template>
    <div class="chat-container">
      <div class="chat-header">
        Chat with ChatGPT
      </div>
      <div class="chat-messages">
        <div v-for="message in messages" :key="message.id" class="message" :class="{ 'user-message': message.isUserMessage }">
          {{ message.content }}
        </div>
      </div>
      <div class="chat-input">
        <input v-model="userInput" @keyup.enter="sendMessage" type="text" placeholder="Type your message..." />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Chat',
    data() {
      return {
        messages: [],
        userInput: '',
      };
    },
    methods: {
      sendMessage() {
        const userMessage = {
          id: Date.now(),
          content: this.userInput,
          isUserMessage: true,
        };
        this.messages.push(userMessage);
        this.userInput = '';
  
        // Simulate response from ChatGPT
        setTimeout(() => {
          const response = {
            id: Date.now(),
            content: 'This is a response from ChatGPT.',
            isUserMessage: false,
          };
          this.messages.push(response);
        }, 500);
      },
    },
  };
  
  import { createApp } from 'vue';
  
  const app = createApp(Chat);
  app.mount('#app');
  