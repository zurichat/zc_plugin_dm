import { combineReducers } from "redux";
import authedUserReducer from "../Reducers/AuthedUser";
// import other reducers

const rootReducer = combineReducers({
//   Reducers go here
    authedUser:authedUserReducer,
});
export default rootReducer;
