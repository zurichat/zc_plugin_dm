import { GET_MEMBERS, GET_MEMBER_PROFILE } from "../Actions/actionTypes";

const initialState = {
  members: null,
};

const membersReducer = (state = null, action) => {
  switch (action.type) {
    case GET_MEMBERS:
      return action.payload;
    default:
      return state;
  }
};

export default membersReducer;
