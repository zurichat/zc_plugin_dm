import axios from "axios";
export const Base_Url = "http://dm.zuri.chat/api/v1";
// Getting members in the organization
export const GET_MEMBERS = "GET_MEMBERS";
export const CREATE_MEMBERS = "CREATE_MEMBERS";

export const getMembers = (members) => ({
  type: GET_MEMBERS,
  payload: members,
});

export const handleGetMembers = (org_id) => async (dispatch) => {
  try {
    const members = await axios.get(
      `${Base_Url}/organization/${org_id}/members`
    );
    await dispatch(getMembers(members));
  } catch (error) {
    console.log(`Error from handleGetMembers ${error}`);
  }
};

// Creating new member
export const createMembers = (member) => ({
  type: CREATE_MEMBERS,
  payload: member,
});

export const handleCreateMember = (org_id, cookie) => async (dispatch) => {
  try {
    const member = axios.post(`${Base_Url}/organization/${org_id}/members`, {
      data: {
        cookie,
      },
    });
    await dispatch(createMembers(member));
  } catch (error) {
    console.log(`Error from create members: ${error}`);
  }
};
