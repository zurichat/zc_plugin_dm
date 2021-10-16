// Import all API endpoints
import APIService from '../../utils/apiServices';

// import all action types
import {
  SET_ROOM,
  GET_ROOMS,
  GET_ALL_DMS,
  CREATE_ROOM,
  GET_ROOM_INFO,
  GET_ROOM_MESSAGES,
  CREATE_ROOM_MESSAGES,
  DELETE_ROOM_MESSAGE,
  ADD_PEOPLE_TO_ROOM,
} from './actionTypes';

// Create Room
const createRoom = (room_id) => ({
  type: CREATE_ROOM,
  payload: room_id,
});

export const handleCreateDmRoom =
  ({ org_id, member_id, user_ids, room_name }) =>
    async (dispatch) => {
      try {
        const { data } = await APIService.createChatRoom(org_id, member_id, {
          org_id: org_id,
          room_member_ids: user_ids,
          room_name: room_name,
        });
        await dispatch(createRoom(data.room_id));
      } catch (error) {
        console.log(`Error from handleCreateDmRoom: ${error}`);
      }
    };

// Set Room
const setRoom = (room_id) => ({
  type: SET_ROOM,
  payload: room_id,
});

export const handleSetRoom =
  (room_id) =>
    async (dispatch) => {
      try {
        await dispatch(setRoom(room_id));
      } catch (error) {
        console.log(`Error from setRoom: ${error}`);
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

// Get all dms
const getAllDms = (dms) => ({
  type: GET_ALL_DMS,
  payload: dms,
});

export const handleAllDms = (org_id, user_id) => async (dispatch) => {
  try {
    const { data } = await APIService.getAllDms(org_id, user_id);
    await dispatch(getAllDms(data));
  } catch (error) {
    console.log(`Error from handleAllDms: ${error}`);
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

//Create room messages
const createRoomMessages = (message) => ({
  type: CREATE_ROOM_MESSAGES,
  payload: message,
});

export const handleCreateRoomMessages =
  (org_id, room_id, messageData) => async (dispatch) => {
    try {
      const { data } = await APIService.createRoomMessage(
        org_id,
        room_id,
        messageData
      );
      await dispatch(createRoomMessages(data));
    } catch (error) {
      console.log(`Error from handleCreateRoomMessages: ${error}`);
    }
  };

// Delete room message

const deleteRoomMessage = (response) => ({
  type: DELETE_ROOM_MESSAGE,
  payload: response,
});

export const handleDeleteRoomMessage =
  (org_id, room_id, message_id) => async (dispatch) => {
    try {
      const { data } = await APIService.deleteMessage(
        org_id,
        room_id,
        message_id
      );
      await dispatch(deleteRoomMessage(data));
    } catch (error) {
      console.log(`Error from handleDeleteRoomMessage: ${error}`);
    }
  };

  // Add People to Room

const addPeopleToRoom = (member_id, room_id, room_name) => ({
  type: ADD_PEOPLE_TO_ROOM,
  payload: room_id, member_id, room_name
});

export const handleAddPeopleToRoom =({org_id, room_id}) => async (dispatch) => {
    try {
      const { data } = await APIService.addPeopleToRoom(org_id, room_id, {
          member_id: member_id,
          room_id: room_id,
          room_name: room_name
        }
      );
      console.log("add people to room",data)
      await dispatch(addPeopleToRoom(data));
    } catch (error) {
      console.log(`Error from handleAddPeopleToRoom: ${error}`);
    }
  };

