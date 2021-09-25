import { combineReducers } from "redux";
import authedUserReducer from "../Reducers/AuthedUser";
import membersReducer from "../Reducers/Members";
import roomsReducer from "../Reducers/Room";
// import other reducers

const rootReducer = combineReducers({
  //   Reducers go here
  authedUser: authedUserReducer,
  members: membersReducer,
  rooms: roomsReducer,
});
export default rootReducer;
