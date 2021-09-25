import React from 'react';

import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// Import all Global CSS components
import 'bootstrap/dist/css/bootstrap.min.css';
import '../src/assets/css/global.module.css';

// Import all Router components
import ChatHome from './pages/chathome';
import dmPopupProfile from './components/dmPopupProfile';

const App = () => {
    return (
        <Router basename='/dm'>
            <Switch>
                <Route exact path='/' component={ChatHome} />
                <Route exact path='/popup' component={dmPopupProfile} />
               
            </Switch>
        </Router>
    );
};

export default App;
