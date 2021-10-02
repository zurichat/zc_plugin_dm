import axios from 'axios';

const baseURL = 'https://dm.zuri.chat/api/v1';

const apiConfig = {
    baseURL,
    timeout: 30000,
    headers: {
        'Content-Type': 'application/json',
    },
};

const $http = axios.create({ ...apiConfig });

class APIServices {
    async getOrgUsers(org_id, data) {
        return await $http.get(`/org/${org_id}/members`, data, {
            withCredentials: true,
        });
    }

    async createChatRoom(org_id, member_id, data) {
        console.log('here')
        console.log(data)
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
        return await $http.post(
            `/${org_id}/rooms/${room_id}/messagemedia`,
            data
        );
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

    async deleteMessage(org_id, room_id, message_id) {
        return await $http.delete(
            `/${org_id}/rooms/${room_id}/messages/${message_id}/message`,
        );
    }
}

const instance = new APIServices();

export default instance;
