import {
  CREATE_ROOM,
  GET_ROOMS,
  GET_ROOM_MESSAGES,
  GET_ROOM_INFO,
  CREATE_ROOM_MESSAGES,
} from "../Actions/actionTypes";

const initialState = {
  room_id: null,
  rooms: null,
  room_info: {},
  room_messages: null,
  room_message :''
};

const roomsReducer = (state = initialState, action) => {
  switch (action.type) {
    case CREATE_ROOM:
      return { ...state, room_id: action.payload };

    case GET_ROOMS:
      return { ...state, rooms: action.payload };

    case GET_ROOM_INFO:
      return { ...state, room_info: { ...action.payload } };

    case GET_ROOM_MESSAGES:
      return {
        ...state,
        room_messages: { ...action.payload },
      };
    case CREATE_ROOM_MESSAGES:
      return{
        ...state,
        room_message:action.payload
      }

    default:
      return state;
  }
};
export default roomsReducer;
