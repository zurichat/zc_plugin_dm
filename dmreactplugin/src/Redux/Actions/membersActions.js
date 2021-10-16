import { GET_MEMBERS, GET_MEMBER_PROFILE } from './actionTypes';
import APIService from '../../utils/apiServices';
import axios from 'axios';

const BASEURL = 'https://api.zuri.chat/organizations';

// Get MEmbers
const getMembers = (members) => ({
    type: GET_MEMBERS,
    payload: members,
});

export const handleGetMembers = (org_id) => async (dispatch) => {
       try {
        const response = await axios.get(`${BASEURL}/${org_id}/members`);
        dispatch(getMembers(response.data.data));
    } catch (error) {
        console.log(error);
    }
};

// GET_MEMBER_PROFILE
const getMemberProfile = (profile) => ({
    type: GET_MEMBER_PROFILE,
    payload: profile,
});

export const handleGetMEmberProfile =
    (org_id, member_id) => async (dispatch) => {
        try {
            const { data } = APIService.getMemberProfile(org_id, member_id, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization:
                        'Bearer f6822af94e29ba112be310d3af45d5c7=MTYzMjg1OTkxMHxHd3dBR0RZeE5UTTNOekEyTmpJM1pEY3lPV1ZtWldNME5tSXhNZz09fKZuk9o04bteGm-SNEDGjWecvvS6qY6QtoGd8P-wNjm7',
                },
            });
            dispatch(getMemberProfile(data));
        } catch (error) {
            console.log(`Error from handleGetMEmberProfile ${error}`);
        }
    };
