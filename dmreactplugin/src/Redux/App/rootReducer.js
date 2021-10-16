import { combineReducers } from "redux";
import roomsReducer from "../Reducers/Room";
import membersReducer from "../Reducers/Members";
import authReducer from "../Reducers/Auth";

const rootReducer = combineReducers({
  roomsReducer,
  authReducer,
  membersReducer,
});

export default rootReducer;
