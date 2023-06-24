const express = require('express');
const cors = require('cors');
const app = express();
const server = require('http').createServer(app);
const http = require('http').createServer(app);
const io = require('socket.io')(http, {
    cors: {
     
      methods: ['GET', 'POST']
    }
  });
app.use(cors({
  //origin: ['http://localhost:8080','http://localhost:8081','http://192.168.43.97:9528', 'http://192.168.43.109:8080', 'http://192.168.43.62:8080'], // 允许的源地址
  methods: ['GET', 'POST'], // 允许的请求方法
}));

// 存储连接的用户信息
const connectedUsers = {};

// 监听连接事件
io.on('connection', socket => {
  // 监听前端发送的消息事件
  socket.on('sendMessage', ({ sender, content }) => {
    // 将消息发送给其他用户
    console.log('s');
    socket.broadcast.emit('receiveMessage', { sender, content });
  });
  socket.on('receiveMessage', ({ sender, content }) => {
    // 处理接收到的消息
    console.log('Received content:', sender, content);
    // 这里可以编写进一步处理接收消息的逻辑
  });
 // socket.on('')
});

app.use(express.json()); // 添加 JSON 解析中间件

app.post('/msg', (req, res) => {
  const { sender, content } = req.body;
  // 群发消息给其他连接的用户
  io.emit('receiveMessage', { sender, content });
  console.log(sender);
  console.log(content);
  res.sendStatus(200); // 返回成功状态码
});

app.post('/bill', (req, res) => {
  //const { sender, content } = req.body;
  // 群发消息给其他连接的用户
  console.log(req.body);
  console.log(req.body.drugPrice);
  io.emit('receiveBill', req.body);
  res.sendStatus(200); // 返回成功状态码
});

app.post('/log', (req, res) => {
  //const { sender, content } = req.body;
  // 群发消息给其他连接的用户
  console.log(req.body);
  io.emit('receiveLog', req.body);
  res.sendStatus(200); // 返回成功状态码
});

app.get('/', (req, res) => {
  res.send('Server is running');
});

http.listen(3000, () => {
  console.log('Server is running on port 3000');
});
