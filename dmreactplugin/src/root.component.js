import { BrowserRouter } from "react-router-dom";
import { Provider } from "react-redux";
import store from "./Redux/App/store";
import App from "./App";

export default function Root(props) {
  return (
    <BrowserRouter basename="/dm">
      <Provider store={store}>
        <App />
      </Provider>
    </BrowserRouter>
  );
}
