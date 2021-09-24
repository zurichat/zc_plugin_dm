export const AUTHED_USER = "AUTHED_USER";
export const REMOVE_USER = "REMOVE_USER";

// for logging in users
export const authedUser = (authedUser) => ({
  type: AUTHED_USER,
  payload: authedUser,
});

// for logging out users
export const removeUser = () => ({
  type: REMOVE_USER,
});
