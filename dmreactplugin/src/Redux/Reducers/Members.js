import { CREATE_MEMBERS, GET_MEMBERS } from "../Actions/Members";

const initialState = {
  members: {},
};

const membersReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_MEMBERS:
      return { ...state, members: action.payload };

    case CREATE_MEMBERS:
      return { ...state, members: { ...state.members, ...action.payload } };
    default:
      return state;
  }
};
export default membersReducer;
