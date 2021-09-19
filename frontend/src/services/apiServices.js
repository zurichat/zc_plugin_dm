import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'https://dm.zuri.chat/api/v1/rooms/',
  withCredentials: false,
  headers:{
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  getClient(room_id,sender_id,message){
    return apiClient.post(`${room_id}/message`,{
      "sender_id":`${sender_id}`,
      "message":`${message}`
    })
  }
}