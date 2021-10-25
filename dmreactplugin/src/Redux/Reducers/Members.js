import { GET_MEMBERS, GET_MEMBER_PROFILE } from '../Actions/actionTypes';

const initialState = {
    members: null,
    member: null
};

const membersReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_MEMBERS:
            return { ...state, members: action.payload }
        case GET_MEMBER_PROFILE:
            return { ...state, member: action.payload }
        default:
            return state;
    }
};

export default membersReducer;
