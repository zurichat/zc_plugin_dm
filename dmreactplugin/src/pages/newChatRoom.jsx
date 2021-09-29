import React, { useEffect } from "react";
import DmProfileHeader from "../components/dmProfileHeader";
import BookmarkHeader from "../components/common/addBookmarkKebab/dmBookMark";
import DmChatContainerBox from "../components/ChatContainer/dmChatContainerBox";
import InputBoxField from "../components/dmBoxInputField";
import PinnedMessage from "../components/common/pinnedMessage/dmPinnedMessages";
import { useDispatch } from "react-redux";
import {
    handleGetRoomInfo,
    handleGetRoomMessages,
} from "../Redux/Actions/dmActions";
import { useSelector } from "react-redux";

// Chat Home Page
const ChatHome = ({ org_id, loggedInUser_id, room_id }) => {
    const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);

    const user2_id =
        roomsReducer?.room_info?.room_user_ids !== undefined &&
        roomsReducer?.room_info?.room_user_ids[1];

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(handleGetRoomMessages(org_id, room_id));
        dispatch(handleGetRoomInfo(org_id, room_id));
    }, [dispatch, org_id, loggedInUser_id, room_id]);

    return (
        <div className="dm-newchat-room position-relative w-100 d-flex flex-column">
            <div className="dm-chatroom-header">
                <DmProfileHeader user2_id={user2_id} />
                <div className=" dm-bookmark-head">
                    <div className="add-bookmark gap-2 d-flex flex-direction-column flex-flow align-items-center px-3 py-1">
                        <PinnedMessage amount={3} />
                        <BookmarkHeader />
                    </div>
                </div>
            </div>
            <div className="dm-message-in-out-box w-100 position-relative row align-items-end">
                <DmChatContainerBox user2_id={user2_id} />
            </div>
            <div className="dm-footer-input-field w-100 position-relative">
                <InputBoxField />
            </div>
        </div>
    );
};
export default ChatHome;
