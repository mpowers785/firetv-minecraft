let socket = io();
let body = document.body;

socket.on('connect', () => {
    console.log('connected');
});

socket.on('screen-data', data => {
    data = JSON.parse(data);
    let imgStr = data.image;
    // console.log(imgStr);

    $('img').attr('src', 'data:image/png;base64,' + imgStr);
    console.log('ye');
});