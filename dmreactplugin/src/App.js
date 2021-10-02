import React, { useEffect } from 'react';
import {
    BrowserRouter as Router,
    Route,
    Switch,
    useLocation,
} from 'react-router-dom';

// import css styles here
import 'bootstrap/dist/css/bootstrap.min.css';
import '../src/assets/css/global.module.css';

// import chat components here
import ChatHome from './pages/newChatRoom';
import AllDms from './pages/allDms/AllDms';

// Import REDUX action
import { useDispatch } from 'react-redux';
import { handleGetRooms } from './Redux/Actions/dmActions';
import { handleGetMembers } from './Redux/Actions/Members';

const App = () => {
    const dispatch = useDispatch();

    let location = useLocation();

    let [org_id, room_id, loggedInUser_id] = location.pathname
        .split('/')
        .filter((string) => string.length > 11);

    useEffect(() => {
       org_id && loggedInUser_id && dispatch(handleGetRooms(org_id, loggedInUser_id));
       org_id && dispatch(handleGetMembers(org_id));
    }, [location, org_id, loggedInUser_id]);

    return (
        <Router basename='/dm'>
            <Switch>
                <Route
                    exact
                    path={`/${org_id}/${room_id}/${loggedInUser_id}`}
                    render={() => (
                        <ChatHome
                            org_id={org_id}
                            loggedInUser_id={loggedInUser_id}
                            room_id={room_id}
                        />
                    )}
                />
                <Route
                    exact
                    path={`/${org_id}/all-dms`}
                    render={() => (
                        <AllDms
                            org_id={org_id}
                        />
                    )}
                />
            </Switch>
        </Router>
    );
};

export default App;
