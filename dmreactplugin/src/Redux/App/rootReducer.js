import { combineReducers } from "redux";
import authedUserReducer from "../Reducers/AuthedUser";
import membersReducer from "../Reducers/Members";
// import other reducers

const rootReducer = combineReducers({
  //   Reducers go here
  authedUser: authedUserReducer,
  members: membersReducer,
});
export default rootReducer;
