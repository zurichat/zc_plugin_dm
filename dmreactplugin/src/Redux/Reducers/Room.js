import {
  CREATE_ROOM,
  GET_ROOMS,
  GET_ROOM_MESSAGES,
  GET_ROOM_INFO,
} from "../Actions/actionTypes";

const initialState = {
  room_ids: null,
  rooms: null,
  room_info: {},
  room_messages: null,
};

const roomsReducer = (state = initialState, action) => {
  switch (action.type) {
    case CREATE_ROOM:
      return { ...state, room_ids: action.payload };

    case GET_ROOMS:
      return { ...state, rooms: action.payload };

    case GET_ROOM_INFO:
      return { ...state, room_info: { ...action.payload } };

    case GET_ROOM_MESSAGES:
      return {
        ...state,
        room_messages: { ...action.payload },
      };

    default:
      return state;
  }
};
export default roomsReducer;
