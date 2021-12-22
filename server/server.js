const screenshot = require('screenshot-desktop');
const express = require('express');
const app = express();
const socket = require('socket.io');

let interval;

app.use(express.static('public'))

let server = app.listen(3000, console.log('listening on 3000...'));
let io = socket(server);

io.sockets.on('connection', (socket) => {
    console.log(socket.id);

    interval = setInterval(() => {
        screenshot().then((img) => {
            let imgStr = new Buffer.from(img).toString('base64');
            let obj = {};
            obj.image = imgStr;
    
            socket.emit('screen-data', JSON.stringify(obj));
        });
    }, 300);
});