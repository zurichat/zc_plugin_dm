import {
  SET_ROOM,
  GET_ROOMS,
  CREATE_ROOM,
  GET_ALL_DMS,
  GET_ROOM_INFO,
  GET_ROOM_MESSAGES,
  CREATE_ROOM_MESSAGES,
  ADD_PEOPLE_TO_ROOM
} from "../Actions/actionTypes";

const initialState = {
  room_id: null,
  rooms: null,
  room_info: {},
  room_messages: null,
  room_message: '',
  all_dms: null,
  addMember:null,
};

const roomsReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_ROOM:
      return { ...state, room_id: action.payload };
    
    case CREATE_ROOM:
      return { ...state, room_id: action.payload };

    case GET_ROOMS:
      return { ...state, rooms: action.payload };

    case GET_ALL_DMS:
      return { ...state, all_dms: action.payload };

    case GET_ROOM_INFO:
      return { ...state, room_info: { ...action.payload } };

    case GET_ROOM_MESSAGES:
      return {
        ...state,
        room_messages: { ...action.payload },
      };
    case CREATE_ROOM_MESSAGES:
      return {
        ...state,
        room_message: action.payload
      }
    case ADD_PEOPLE_TO_ROOM:
      return{
        ...state,
        addMember:action.payload
      }
    
    default:
      return state;
  }
};
export default roomsReducer;
