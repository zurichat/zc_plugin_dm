import { GET_LOGGED_IN_USER, GET_LOGGED_IN_USER_ORGANISATION, SET_IS_AUTHENTICATED } from '../Actions/actionTypes';

const initialState = {
    isAuthenticated: false,
    user: null,
    organisation: null
};

const authReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_IS_AUTHENTICATED:
            return { ...state, isAuthenticated: action.payload };

        case GET_LOGGED_IN_USER:
            return { ...state, user: action.payload };

        case GET_LOGGED_IN_USER_ORGANISATION:
            return { ...state, organisation: action.payload };

        default:
            return state;
    }
};

export default authReducer;
