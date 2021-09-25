// Import all API endpoints
import APIService from '../../utils/apiServices';

// import all action types
import {
    GET_MEMBERS,
    CREATE_ROOM,
    GET_ROOMS,
    GET_SOCKETS,
    GET_MESSAGES,
    SEND_MESSAGE,
    GET_PINNED_MESSAGE,
    MESSAGE_REACTION,
} from './actionTypes';

// Get Organization Members
const handleGetMembers = (org_id) => async (dispatch) => {
    try {
        const res = await APIService.getOrgUsers(org_id);

        dispatch({ type: GET_MEMBERS, payload: res.data.data });
    } catch (error) {
        console.log(error);
    }
};

const createDmRoom = (org_id, user1_id, user2_id) => async (dispatch) => {
    try {
        const res = await APIService.createChatRoom(org_id, {
            data: {
                org_id: org_id,
                room_user_ids: [user1_id, user2_id],
                bookmark: ['string'],
                pinned: ['string'],
            },
        });

        dispatch({ type: CREATE_ROOM, payload: res.data.data });
    } catch (error) {
        console.log(error);
    }
};

const appActions = {
    handleGetMembers,
    createDmRoom,
};

export default appActions;
