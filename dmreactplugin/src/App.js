import React, { useEffect } from 'react';
import { Route, Switch } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';

// import css styles here
import 'bootstrap/dist/css/bootstrap.min.css';
import '../src/assets/css/global.module.css';

// import chat components here
import ChatHome from './pages/newChatRoom';
import AllDms from './pages/allDms/AllDms';

// Import REDUX action
import { handleGetLoggedInUser, handleGetLoggedInUserOrganisation } from './Redux/Actions/authActions';
import { handleGetMembers } from './Redux/Actions/membersActions';

const App = () => {
  const authReducer = useSelector(({ authReducer }) => authReducer);
  const membersReducer = useSelector(({ membersReducer }) => membersReducer);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(handleGetLoggedInUser());
    dispatch(handleGetLoggedInUserOrganisation());
  }, []);

  useEffect(() => {
    if (authReducer.organisation) {
      dispatch(handleGetMembers(authReducer.organisation));
    }
  }, [authReducer.organisation]);

  return (
    <>
      {
        authReducer.user && authReducer.organisation && membersReducer.members  ? (
          <Switch>
            <Route exact path="/" component={AllDms} />
            <Route exact path="/:room_id" component={ChatHome} />
          </Switch>
        ) : (
          <div>Loading...</div>
        )
      }
    </>
  )
};

export default App;
