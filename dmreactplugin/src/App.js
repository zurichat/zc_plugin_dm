import React from "react";

import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

// Import all Global CSS components
import "bootstrap/dist/css/bootstrap.min.css";
import "../src/assets/css/global.module.css";

// Import all Router components
import ChatHome from "./pages/chathome";
import removePinnedMessage from "./components/common/removePinnedMessageModal/removePinnedMessageModal";
import PinnedMessage from "./components/dmPinnedMessages";
import HoverPinnedMessage from "./components/common/removePinnedMessageModal/hoverViewPinned";

const App = () => {
  return (
    <Router basename="/dm">
      <Switch>
        <Route exact path="/" component={ChatHome} />
        <Route exact path="/removeMessage" component={removePinnedMessage} />
        <Route exact path="/viewPinned">
          <PinnedMessage amount={3} />
        </Route>
        <Route exact path="/hoverPinnedMessage">
          <HoverPinnedMessage />
        </Route>
      </Switch>
    </Router>
  );
};

export default App;
