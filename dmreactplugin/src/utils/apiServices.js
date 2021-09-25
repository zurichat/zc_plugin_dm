import axios from "axios";
import { GET_ROOM_MESSAGES } from "../Redux/Actions/actionTypes";

const baseURL = "https://dm.zuri.chat/api/v1";

const apiConfig = {
  baseURL,
  timeout: 30000,
  headers: {
    "Content-Type": "application/json",
  },
};

const $http = axios.create({ ...apiConfig });

class APIServices {
  async getOrgUsers(org_id, data) {
    return await $http.get(`/organization/${org_id}/members`, data);
  }

  async createChatRoom(org_id, data) {
    return await $http.post(`/${org_id}/createroom`, data);
  }

  async updateMembers(org_id, member_id, data) {
    return await $http.put(`/${org_id}/members/${member_id}`, data);
  }

  async getMembersOrg(org_id, member_id, data) {
    return await $http.get(`/${org_id}/members/${member_id}`, data);
  }

  async postMembersOrg(org_id, member_id, data) {
    return await $http.post(`/${org_id}/members/${member_id}`, data);
  }

  async pinMessage(org_id, message_id, data) {
    return await $http.put(`/${org_id}/messages/${message_id}/pin`, data);
  }

  async unPinMessage(org_id, message_id, data) {
    return await $http.delete(`/${org_id}/messages/${message_id}/unpin`);
  }

  async getRoomInfo(org_id, data) {
    return await $http.get(`/${org_id}/room-info`, data);
  }

  async postRoomMessage(org_id, room_id, data) {
    return await $http.post(`/${org_id}/rooms/${room_id}/message`, data);
  }

  async postRoomMedia(org_id, room_id, data) {
    return await $http.post(`/${org_id}/rooms/${room_id}/messagemedia`, data);
  }

  async postMessageReactions(org_id, room_id, message_id, data) {
    return await $http.post(
      `/${org_id}/rooms/${room_id}/messages/${message_id}/reactions`,
      data
    );
  }

  async getMessageReactions(org_id, room_id, message_id, data) {
    return await $http.get(
      `/${org_id}/rooms/${room_id}/messages/${message_id}/reactions`,
      data
    );
  }

  async postMessageThread(org_id, room_id, message_id, data) {
    return await $http.post(
      `/${org_id}/rooms/${room_id}/messages/${message_id}/thread`,
      data
    );
  }

  async getRoomUserId(org_id, user_id, data) {
    return await $http.get(`/${org_id}/rooms/${user_id}`, data);
  }

  async updateMessage(org_id, id, data) {
    return await $http.get(`/${org_id}/updatemessage/${id}`, data);
  }

  async postUpdateMesage(org_id, id, data) {
    return await $http.post(`/${org_id}/updatemessage/${id}`, data);
  }

  async getRoomMessages(org_id, room_id, data) {
    return await $http.get(`/${org_id}/${room_id}/messages`, data);
  }


  async getSingleMessage(room_id, message_id){
    ​return await $http.get(`/${room_id}​/${message_id}`,data)
  }

  async getPinnedMessages(org_id,room_id, data){
    return await $http.get(`/${org_id}/${message_id}/pinnedmessage/`, data)
    
  }

  async getAllBookmarks(org_id,room_id, data){
    return await $http.get(`/${org_id}/${message_id}/bookmark/all`,data)

  }

async addToBookmark(org_id,room_id, data){
    return await $http.post(`/${org_id}/${message_id}/bookmark/new`,data)
}

}

const instance = new APIServices();

export default instance;
