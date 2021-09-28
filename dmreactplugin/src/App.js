<<<<<<< HEAD

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";


=======
import React, { useEffect, useState } from 'react';
import {
    BrowserRouter as Router,
    Route,
    Switch,
    useLocation,
} from 'react-router-dom';
export const AppContext = React.createContext();
>>>>>>> 9a48c65447a65a76450fc54ca2d52be9b216c99e
// Import all Global CSS components
import 'bootstrap/dist/css/bootstrap.min.css';
import '../src/assets/css/global.module.css';

// Import all Router components
import ChatHome from './pages/newChatRoom';
import { useDispatch, useSelector } from 'react-redux';
import { handleGetRooms } from './Redux/Actions/dmActions';

import dmSingleMessageContainer from './components/dmSingleMessageContainer';
const App = () => {
<<<<<<< HEAD

    return (
        <Router basename='/dm'>
            <Switch>
                <Route exact path='/' component={ChatHome} />

                <Route exact path='/message' component={dmSingleMessageContainer} />
            </Switch>
        </Router>
    );

  return (
    <Router basename="/dm">
      <Switch>
        <Route exact path="/" component={ChatHome} />
      </Switch>
      <Switch>
        <Route exact path="/removeMessage">
          <RemovePinnedMessage />
        </Route>
      </Switch>
      <Switch>
        <Route exact path="/viewPinned">
          <PinnedMessage amount={3} />
        </Route>
      </Switch>
      <Switch>
        <Route exact path="/hoverPinnedMessage">
          <HoverPinnedMessage />
        </Route>
      </Switch>
      <Switch>
        <Route exact path="/addBookmark">
          <AddBookmark />
        </Route>
      </Switch>
      <Switch>
        <Route exact path="/textField">
          <AddBookmarkLink />
        </Route>
      </Switch>
    </Router>
  );
=======
    const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);
    const dispatch = useDispatch();
    const [actualRoom, setActualRoom] = useState([]);
    let location = useLocation();
    let room_id =
        location.pathname.split('/')[location.pathname.split('/').length - 1];
    // const org_id = '614679ee1a5607b13c00bcb7'
    let org_id =
        location.pathname.split('/')[location.pathname.split('/').length - 2];

    console.log(org_id, room_id);
    // org_id, user_id
    // useEffect(() => {
    //   dispatch(
    //     // pass in the org_id and the user_id from the url
    //     handleGetRooms('614679ee1a5607b13c00bcb7', '6145f987285e4a18402074eb')
    //   )
    // }, [dispatch])

    // console.log(roomsReducer)
    const getActualRoom = async () => {
        const res = await fetch(
            'https://dm.zuri.chat/api/v1/sidebar?org=614679ee1a5607b13c00bcb7&user=614679ee1a5607b13c00bcb8'
        );
        const data = await res.json();
        const joinedRooms = data.joined_rooms;
        const actualRoom = joinedRooms.filter(
            (room) => room.room_url === `/dm/${org_id}/${room_id}`
        );
        setActualRoom(actualRoom);
    };

    useEffect(() => {
        getActualRoom();
    }, [location]);

    if (actualRoom.length === 0) {
        return <div>loading...</div>;
    }
    return (
        <AppContext.Provider value={{ actualRoom }}>
            <Router basename='/dm'>
                {/* {console.log(actualRoom)} */}
                <Switch>
                    <Route exact path={`/${org_id}/${room_id}`}>
                        <ChatHome />
                    </Route>
                </Switch>
            </Router>
        </AppContext.Provider>
    );
>>>>>>> 9a48c65447a65a76450fc54ca2d52be9b216c99e
};

export default App;
