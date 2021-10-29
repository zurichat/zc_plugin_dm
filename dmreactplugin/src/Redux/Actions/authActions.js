// Import all API endpoints
import APIService from '../../utils/apiServices';

// import all action types
import {
    GET_LOGGED_IN_USER,
    GET_LOGGED_IN_USER_ORGANISATION,
    SET_IS_AUTHENTICATED,
} from './actionTypes';

// Get Logged in user
const getLoggedInUser = (user) => ({
    type: GET_LOGGED_IN_USER,
    payload: user,
});

const setIsAuthenticated = (isAuthenticated) => ({
    type: SET_IS_AUTHENTICATED,
    payload: isAuthenticated,
});

export const handleGetLoggedInUser = () => async (dispatch) => {
    try {
        const userInfo = await APIService.getLoggedInUser();
        if (userInfo[0]._id !== '') {
            await dispatch(getLoggedInUser(userInfo[0]));
        } else {
            await dispatch(getLoggedInUser(null));
        }
    } catch (error) {
        console.log(`Error from handleGetLoggedInUser: ${error}`);
    }
};

// Get Logged in user organisation
const getLoggedInUserOrganisation = (organisation) => ({
    type: GET_LOGGED_IN_USER_ORGANISATION,
    payload: organisation,
});

export const handleGetLoggedInUserOrganisation = () => async (dispatch) => {
    try {
        const { currentWorkspace } = await APIService.getLoggedInUserOrganisation();
        await dispatch(getLoggedInUserOrganisation(currentWorkspace));
    } catch (error) {
        console.log(`Error from handleGetLoggedInUserOrganisation: ${error}`);
    }
};
