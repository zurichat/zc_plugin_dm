import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// Import all Global CSS components
import 'bootstrap/dist/css/bootstrap.min.css';
import '../src/assets/css/global.module.css';

// Import all Router components
import ChatHome from './pages/newChatRoom';
import Pop from './components/dmPopupProfile';

const App = () => {
    return (
        <Router basename='/dm'>
            <Switch>
                <Route path='/' component={ChatHome} />
                <Route path='/test' component={Pop} />
            </Switch>
        </Router>
    );
};

export default App;
