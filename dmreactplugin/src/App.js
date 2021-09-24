import React from 'react';

import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// Import all Global CSS components
import 'bootstrap/dist/css/bootstrap.min.css';
import '../src/assets/css/global.module.css';

// Import all Router components
import ChatHome from './pages/chathome';
import RemindMe from './components/common/remindMe/remindMe';

const App = () => {
    return (
        <Router basename='/dm'>
            <Switch>
                <Route exact path='/' component={ChatHome} />
                <Route path="/remind" component={RemindMe} />
            </Switch>
        </Router>
    );
};

export default App;
