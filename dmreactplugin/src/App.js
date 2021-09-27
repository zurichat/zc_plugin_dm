import React, { useEffect } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

// Import all Global CSS components
import "bootstrap/dist/css/bootstrap.min.css";
import "../src/assets/css/global.module.css";

// Import all Router components
import ChatHome from "./pages/newChatRoom";
import { useDispatch, useSelector } from "react-redux";
import { handleGetRooms } from "./Redux/Actions/dmActions";

const App = () => {
  const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);
  const dispatch = useDispatch();

  // org_id, user_id
  useEffect(() => {
    dispatch(
      // pass in the org_id and the user_id from the url
      handleGetRooms("614679ee1a5607b13c00bcb7", "6145f987285e4a18402074eb")
    );
  }, [dispatch]);

  console.log(roomsReducer);

  return (
    <Router basename="/dm">
      <Switch>
        <Route exact path="/" component={ChatHome} />
      </Switch>
    </Router>
  );
};

export default App;
