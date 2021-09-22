import Axios from 'axios';

const apiClient = Axios.create({
    baseURL: 'https://dm.zuri.chat/api/v1/rooms/',
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
    },
});


export default {
    getClient(room_id, sender_id, message) {
        return apiClient.post(`${room_id}/message`, {
            sender_id: `${sender_id}`,
            message: `${message}`,
        });
    },
    postEmoji(room_id, message_id, emoji){
        return apiClient.post(`${room_id}/messages/${message_id}/reactions`, emoji);
    },
    getEmojis(room_id, message_id){
        return apiClient.get(`${room_id}/messages/${message_id}/reactions`)
    },
    recieveClient(room_id) {
        return Axios.get(`https://dm.zuri.chat/api/v1/messages/${room_id}`);
    },
};
