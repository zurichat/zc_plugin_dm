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

centrifuge.subscribe('6146d126845b436ea04d102e', function(ctx) {
    console.log(ctx);
});

// centrifuge.connect();
export default centrifuge.connect();
