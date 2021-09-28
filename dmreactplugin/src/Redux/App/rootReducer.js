import { combineReducers } from "redux";
import roomsReducer from "../Reducers/Room";

const rootReducer = combineReducers({
  roomsReducer,
});

export default rootReducer;
