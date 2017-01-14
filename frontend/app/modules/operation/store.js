import thunk from "redux-thunk";
import {applyMiddleware, compose, createStore} from "redux";
import baseReducer from "./reducers";
import createLogger from "redux-logger";

const logger = createLogger();
const middlewaresList = [thunk, logger];
const store = compose(applyMiddleware(...middlewaresList))(createStore)(baseReducer);
export default store;