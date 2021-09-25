import Centrifuge from 'centrifuge';

const centrClient = new Centrifuge('wss://centrifuge.io/connection/websocket');

centrClient.subscribe(`${room_id}`, function (message) {
    console.log(message);
});

centrClient.connect();
