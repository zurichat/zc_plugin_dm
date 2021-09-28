import { GET_MEMBERS, GET_MEMBER_PROFILE } from "./actionTypes";
import APIService from "../../utils/apiServices";

// Get MEmbers
const getMembers = (members) => ({
  type: GET_MEMBERS,
  payload: members,
});

export const handleGetMembers = (org_id) => async (dispatch) => {
  try {
    const { data } = await APIService.getOrgUsers(org_id);
    dispatch(getMembers(data));
  } catch (error) {
    console.log(`Error from handleGetMEmbers ${error}`);
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
      const { data } = APIService.getMemberProfile(org_id, member_id);
      dispatch(getMemberProfile(data));
    } catch (error) {
      console.log(`Error from handleGEtMemberPRofile ${error}`);
    }
  };
