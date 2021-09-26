import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

// Import all Global CSS components
import "bootstrap/dist/css/bootstrap.min.css";
import "../src/assets/css/global.module.css";

// Import all Router components
import ChatHome from "./pages/chathome";
import RemovePinnedMessage from "./components/common/pinnedMessage/removePinnedMessageModal";
import PinnedMessage from "./components/dmPinnedMessages";
import HoverPinnedMessage from "./components/common/pinnedMessage/hoverViewPinned";
import AddBookmark from "./components/common/addBookmarkKebab/addBookmark";
import AddBookmarkLink from "./components/common/addBookmarkKebab/addBookmarkLink";
import BoxInput from "./components/dmBoxInput";


const App = () => {
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
      <Switch>
        <Route exact path="/BoxInput">
          <BoxInput />
        </Route>
      </Switch>
    </Router>
  );
};

export default App;
