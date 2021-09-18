import Centrifuge from 'centrifuge';

const centrifuge = new Centrifuge(
    'wss://realtime.zuri.chat/connection/websocket'
);

centrifuge.on('connect', function(ctx) {
    console.log('connected', ctx);
});

centrifuge.on('disconnect', function(ctx) {
    console.log('disconnected', ctx);
});

centrifuge.subscribe('61423bbc9fd1f4f655d445e7', function(ctx) {
    console.log(ctx);
});

// centrifuge.connect();
export default centrifuge.connect();
