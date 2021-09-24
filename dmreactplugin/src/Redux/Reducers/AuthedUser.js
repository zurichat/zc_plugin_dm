import { AUTHED_USER, REMOVE_USER } from "../Actions/AuthedUser";

const authedUserReducer = (state = null, action) => {
  switch (action.type) {
    case AUTHED_USER:
      return action.payload;

    case REMOVE_USER:
      return null;

    default:
      return state;
  }
};

export default authedUserReducer;
