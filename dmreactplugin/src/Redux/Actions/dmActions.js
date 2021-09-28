// Import all API endpoints
import APIService from "../../utils/apiServices";

// import all action types
import {
  CREATE_ROOM,
  GET_ROOMS,
  GET_ROOM_INFO,
  GET_ROOM_MESSAGES,
} from "./actionTypes";

// Create Room

const createRoom = (room_id) => ({
  type: CREATE_ROOM,
  payload: room_id,
});

export const handleCreateDmRoom =
  (org_id, user1_id, user2_id) => async (dispatch) => {
    try {
      const { data } = await APIService.createChatRoom(org_id, {
        data: {
          org_id: org_id,
          room_user_ids: [user1_id, user2_id],
          bookmark: [],
          pinned: [],
        },
      });
      await dispatch(createRoom(data));
    } catch (error) {
      console.log(`Error from handleCreateDmRoom: ${error}`);
    }
  };

// Get rooms
const getRooms = (rooms) => ({
  type: GET_ROOMS,
  payload: rooms,
});

export const handleGetRooms = (org_id, user_id) => async (dispatch) => {
  try {
    const { data } = await APIService.getRoomUserId(org_id, user_id);
    await dispatch(getRooms(data));
  } catch (error) {
    console.log(`Error from handleGetRooms: ${error}`);
  }
};

// Get room Info
const getRoomInfo = (info) => ({
  type: GET_ROOM_INFO,
  payload: info,
});

export const handleGetRoomInfo = (org_id, room_id) => async (dispatch) => {
  try {
    const { data } = await APIService.getRoomInfo(org_id, room_id);
    await dispatch(getRoomInfo(data));
  } catch (error) {
    console.log(`Error from handleGetRoomInfo: ${error}`);
  }
};

// Get room messages
const getRoomMessages = (message) => ({
  type: GET_ROOM_MESSAGES,
  payload: message,
});

export const handleGetRoomMessages = (org_id, room_id) => async (dispatch) => {
  try {
    const { data } = await APIService.getRoomMessages(org_id, room_id);
    await dispatch(getRoomMessages(data));
  } catch (error) {
    console.log(`Error from handleGetRoomMEssages: ${error}`);
  }
};
