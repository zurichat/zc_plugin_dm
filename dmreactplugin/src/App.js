import React, { useEffect, useState } from "react";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  useLocation,
} from "react-router-dom";

// Import all Global CSS components
import "bootstrap/dist/css/bootstrap.min.css";
import "../src/assets/css/global.module.css";

// Import all Router components
import ChatHome from "./pages/newChatRoom";
import { useDispatch, useSelector } from "react-redux";
import {
  handleCreateDmRoom,
  handleGetRoomInfo,
  handleGetRooms,
} from "./Redux/Actions/dmActions";

const App = () => {
  const loggedInUser_id = "6145f987285e4a18402074eb";
  const dispatch = useDispatch();

  let location = useLocation();
  let room_id =
    location.pathname.split("/")[location.pathname.split("/").length - 1];
  let org_id =
    location.pathname.split("/")[location.pathname.split("/").length - 2];

  //   const room_id=roomsReducer.rooms?.find((room) => (
  //   room._id===roomsReducer.rooms_id
  // ))

  useEffect(() => {
    dispatch(handleGetRooms(org_id, loggedInUser_id));

    // dispatch(handleGetRoomInfo(org_id, room_id));
    // handleCreateDmRoom(org_id, roomsReducer?.room_info?.room_room_ids)

    // const actualRoom =
    //   joinedRooms &&
    //   joinedRooms.find((room) => room?.room_url === `/dm/${org_id}/${room_id}`);
    // console.log(actualRoom);
  }, [location]);

  return (
    <Router basename="/dm">
      <Switch>
        <Route
          exact
          path={`/${org_id}/${room_id}`}
          render={() => (
            <ChatHome
              org_id={org_id}
              loggedInUser_id={loggedInUser_id}
              room_id={room_id}
            />
          )}
        />
      </Switch>
    </Router>
  );
};

export default App;
