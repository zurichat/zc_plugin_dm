import axios from 'axios';
import { GetUserInfo } from "@zuri/utilities";

const baseURL = 'https://dm.zuri.chat/api/v1';

const apiConfig = {
  baseURL,
  timeout: 30000000,
  headers: {
    'Content-Type': 'application/json',
  },
  validateStatus: function (status) {
    return status < 500; // Resolve only if the status code is less than 500
  },
};

const $http = axios.create({ ...apiConfig });

class APIServices {

  async getLoggedInUser() {
    return await GetUserInfo();
  }

  async getLoggedInUserOrganisation() {
    return await GetUserInfo();
  }

  async getAllDms(org_id, member_id) {
    return await $http.get(`/org/${org_id}/members/${member_id}/all_dms`);
  }

  async getOrgUsers(org_id, data) {
    return await $http.get(`/org/${org_id}/members`, data, {
      withCredentials: true,
    });
  }

  async createChatRoom(org_id, member_id, data) {
    return await $http.post(`/org/${org_id}/users/${member_id}/room`, data);
  }

  async updateMembers(org_id, member_id, data) {
    return await $http.put(`/${org_id}/members/${member_id}`, data);
  }

  async getMemberProfile(org_id, member_id, data) {
    return await $http.get(
      `/org/${org_id}/members/${member_id}/profile`,
      data,
      {
        withCredentials: true,
      }
    );
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

  async getRoomInfo(org_id, room_id) {
    return await $http.get(`/org/${org_id}/rooms/${room_id}/info`);
  }

  async getRoomMessages(org_id, room_id) {
    return await $http.get(`/org/${org_id}/rooms/${room_id}/messages`);
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
    return await $http.get(`/org/${org_id}/users/${user_id}/rooms`);
  }

  async updateMessage(org_id, id, data) {
    return await $http.get(`/${org_id}/updatemessage/${id}`, data);
  }

  async postUpdateMesage(org_id, id, data) {
    return await $http.post(`/${org_id}/updatemessage/${id}`, data);
  }

  async createRoomMessage(org_id, room_id, data) {
    return await $http.post(`/org/${org_id}/rooms/${room_id}/messages`, data);
  }

  async deleteMessage(org_id, room_id, message_id, data) {
    return await $http.delete(
      `/${org_id}/rooms/${room_id}/messages/${message_id}/message`,
      data
    );
  }
  async starPerson(org_id, room_id, message_id) {
    return await $http.put(
      `/org/${org_id}/rooms/${room_id}/members/${message_id}/star`
    );
  }

  async getStarPersonInfo(org_id, room_id, message_id) {
    return await $http.get(
      `/org/${org_id}/rooms/${room_id}/members/${message_id}/star`
    );
  }

  async addPeopleToRoom(org_id, room_id, data) {
    return await $http.post(
        `/org/${org_id}/rooms/${room_id}/member`,
        data
    );
  }
}

const instance = new APIServices();

export default instance;
