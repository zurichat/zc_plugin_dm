import { GET_ALL_USER_DMS } from '../Actions/actionTypes';

const initialState = {
    allDms: {},
};

const allDmsReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ALL_USER_DMS:
        return{
            ...state,
            allDms:action.payload
        } 

        default:
        return state;
    }
};

export default allDmsReducer;
