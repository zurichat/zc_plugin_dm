import { combineReducers } from "redux";
import roomsReducer from "../Reducers/Room";
import membersReducer from "../Reducers/Members";
import allDmsReducer from "../Reducers/Dms";

const rootReducer = combineReducers({
  roomsReducer,
  membersReducer,
  allDmsReducer,
});

export default rootReducer;
