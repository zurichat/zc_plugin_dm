import { combineReducers } from "redux";
import authedUserReducer from "../Reducers/AuthedUser";
import roomsReducer from "../Reducers/Room";

const rootReducer = combineReducers({
  //   Reducers go here
  authedUserReducer,
  roomsReducer,
});

export default rootReducer;
