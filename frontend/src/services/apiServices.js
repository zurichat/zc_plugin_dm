import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'https://dm.zuri.chat/api/v1',
  withCredentials: false,
  headers:{
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  getClient(){
    return apiClient.post('/sendmessage',{
      "sender_id":"lkdl049052098509292",
      "room_id":"613b14e459842c7444fb02bc",
      "message":"testing zuri websocket"
    })
  }
}