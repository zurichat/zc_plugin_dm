import React, { useEffect } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

// Import all Global CSS components
import "bootstrap/dist/css/bootstrap.min.css";
import "../src/assets/css/global.module.css";

// Import all Router components
import ChatHome from "./pages/newChatRoom";
import { useDispatch, useSelector } from "react-redux";
import { handleCreateDmRoom, handleGetRooms } from "./Redux/Actions/dmActions";

const App = () => {
  const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);
  const dispatch = useDispatch();

  // org_id, user_id
  useEffect(() => {
    dispatch(
      handleCreateDmRoom(
        "614679ee1a5607b13c00bcb7",
        "6145f987285e4a18402074eb",
        "61467e651a5607b13c00bcc8"
      )
    );
    dispatch(
      handleGetRooms("614679ee1a5607b13c00bcb7", "6145f987285e4a18402074eb")
    );
  }, [dispatch]);

  return (
    <Router basename="/dm">
      <Switch>
        <Route
          exact
          path="/:org_Id/:user_id"
          render={(props) => <ChatHome roomsReducer={roomsReducer} />}
        />
      </Switch>
    </Router>
  );
};

export default App;
