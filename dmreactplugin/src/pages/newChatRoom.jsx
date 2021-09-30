import React, { useEffect } from 'react';
import DmProfileHeader from '../components/dmProfileHeader';
import BookmarkHeader from '../components/common/addBookmarkKebab/dmBookMark';
import DmChatContainerBox from '../components/ChatContainer/dmChatContainerBox';
import InputBoxField from '../components/dmBoxInputField';
import { useDispatch } from 'react-redux';
import {
    handleGetRoomInfo,
    handleGetRoomMessages,
} from '../Redux/Actions/dmActions';
import { useSelector } from 'react-redux';

// Chat Home Page
const ChatHome = ({ org_id, loggedInUser_id, room_id }) => {
    const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);
    const membersReducer = useSelector(({ membersReducer }) => membersReducer);

    const user2_id =
        roomsReducer?.room_info?.room_user_ids !== undefined &&
        roomsReducer?.room_info?.room_user_ids[1];

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(handleGetRoomMessages(org_id, room_id));
        dispatch(handleGetRoomInfo(org_id, room_id));
    }, [dispatch, org_id, loggedInUser_id, room_id]);

    const actualUser =
        membersReducer &&
        membersReducer.find((member) => member._id === user2_id);

    return (
        <div className='dm-newchat-room position-relative w-100 d-flex flex-column'>
            <div className='dm-chatroom-header'>
                <DmProfileHeader user2_id={user2_id} actualUser={actualUser} />
                <BookmarkHeader />
            </div>
            <div className='dm-message-in-out-box w-100 position-relative row align-items-end'>
                <DmChatContainerBox
                    user2_id={user2_id}
                    actualUser={actualUser}
                />
            </div>
            <div className='dm-footer-input-field w-100 position-relative'>
                <InputBoxField />
            </div>
        </div>
    );
};
export default ChatHome;
