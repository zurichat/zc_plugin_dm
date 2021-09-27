import axios from "axios";

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

  async getRoomUserId(org_id, user_id) {
    return await $http.get(`/sidebar?org=${org_id}&user=${user_id}`);
  }

  async updateMessage(org_id, id, data) {
    return await $http.get(`/${org_id}/updatemessage/${id}`, data);
  }

  async postUpdateMesage(org_id, id, data) {
    return await $http.post(`/${org_id}/updatemessage/${id}`, data);
  }
}

const instance = new APIServices();

export default instance;
