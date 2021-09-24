import { CREATE_ROOM, GET_ROOMS, GET_ROOM_MESSAGES } from "../Actions/Room";

const initialState = {
  room_id: [],
  rooms: [],
  messages: {},
};

export default (state = initialState, action) => {
  switch (action.type) {
    case CREATE_ROOM:
      return { ...state, room_id: [...state.room_id, action.payload] };

    case GET_ROOMS:
      return { ...state, rooms: [...state.rooms, action.payload] };

    case GET_ROOM_MESSAGES:
      return { ...state, messages: { ...state.messages, ...action.payload } };

    default:
      return state;
  }
};
