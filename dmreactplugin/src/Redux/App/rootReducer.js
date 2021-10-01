import { combineReducers } from "redux";
import roomsReducer from "../Reducers/Room";
import membersReducer from "../Reducers/Members";

const rootReducer = combineReducers({
  roomsReducer,
  membersReducer,
});

export default rootReducer;
