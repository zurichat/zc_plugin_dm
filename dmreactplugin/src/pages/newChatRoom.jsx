import React, { useEffect, useState, useRef, useMemo } from 'react';
import DmProfileHeader from '../components/dmProfileHeader';
import BookmarkHeader from '../components/common/addBookmarkKebab/dmBookMark';
import DmChatContainerBox from '../components/ChatContainer/dmChatContainerBox';
import InputBoxField from '../components/dmBoxInputField';
import PinnedMessage from '../components/common/pinnedMessage/dmPinnedMessages';
import { useDispatch } from 'react-redux';
import { SubscribeToChannel } from '@zuri/utilities';
import {
  CommentBox,
  MessageInputBox,
  ChatSection,
  MessageBoard,
} from '@zuri/zuri-ui';

// console.log('cb', CommentBox);
import {
  handleCreateRoomMessages,
  handleGetRoomInfo,
  handleGetRoomMessages,
} from '../Redux/Actions/dmActions';
import { useSelector } from 'react-redux';
import './newChatRoom.css';
import ProfileSidebar from '../components/profileSidebar/profileSidebar';

// Chat Home Page
const ChatHome = ({ org_id, loggedInUser_id, room_id }) => {
  const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);
  const membersReducer = useSelector(({ membersReducer }) => membersReducer);
  const { room_messages } = useSelector(({ roomsReducer }) => roomsReducer);
  const chatSidebarConfig = useMemo(() => {
    const currentUser = membersReducer?.find(
      (member) => member._id === loggedInUser_id
    );
    return {
      sendChatMessageHandler: (msg) => {
        dispatch(
          handleCreateRoomMessages(org_id, room_id, {
            sender_id: loggedInUser_id,
            room_id,
            message: msg.richUiData.blocks[0].text,
          })
        );
      },
      currentUserData: {
        username: currentUser?.user_name || 'John Doe',
        imageUrl: '',
      },
      messages: room_messages?.results
        ?.map((message) => {
          const currentDate = new Date(message.created_at);
          return {
            username: currentUser?.user_name || 'John Doe',
            id: message.id,
            time: `${
              currentDate.getHours() < 12
                ? currentDate.getHours()
                : currentDate.getHours() - 12
            }:${currentDate.getMinutes()}${
              currentDate.getHours() < 12 ? 'AM' : 'PM'
            }`,
            imageUrl: '',
            emojis: [
              { name: 'cool', count: 4, emoji: '😎' },
              { name: 'celebrate', count: 1, emoji: '🎉' },
            ],
            richUiData: {
              blocks: [
                {
                  data: {},
                  depth: 0,
                  entityRanges: [],
                  inlineStyleRanges: [],
                  key: '543og',
                  text: message.message,
                  type: 'unstyled',
                },
              ],
              entityMap: {},
            },
          };
        })
        .reverse(),
      showChatSideBar: true,
      chatHeader: 'Chats',
    };
  }, [room_messages, membersReducer]);
  const user2_id =
    roomsReducer?.room_info?.room_user_ids !== undefined &&
    roomsReducer?.room_info?.room_user_ids[1];
  const messages = room_messages?.results;

  const dispatch = useDispatch();
  useEffect(() => {
    SubscribeToChannel(room_id, function (ctx) {
      console.log('room_id', ctx);
    });
  }, []);
  useEffect(() => {
    dispatch(handleGetRoomMessages(org_id, room_id));
    dispatch(handleGetRoomInfo(org_id, room_id));
  }, [dispatch, org_id, loggedInUser_id, room_id]);

  const actualUser = membersReducer?.find((member) => member._id === user2_id);

  const [grid, setGrid] = useState('');
  const [none, setNone] = useState('none');

  return (
    <div className="dm-plugin-full-page" style={{ display: grid }}>
      <div className="dm-newchat-room">
        <div className="dm-chatroom-header">
          <DmProfileHeader
            user2_id={user2_id}
            actualUser={actualUser}
            none={none}
            setNone={setNone}
            grid={grid}
            setGrid={setGrid}
          />
          <div className="dm-bookmark-head">
            <div className="add-bookmark gap-2 d-flex flex-direction-column flex-flow align-items-center px-3 py-1">
              <PinnedMessage room_id={room_id} actualUser={actualUser} />
              <BookmarkHeader />
            </div>
          </div>
        </div>
        <div className="dm-message-in-out-box w-100 h-100 position-relative row align-items-end">
          {/* <DmChatContainerBox
            user2_id={user2_id}
            room_id={room_id}
            actualUser={actualUser}
          /> */}
          {room_messages && membersReducer && (
            <MessageBoard chatsConfig={chatSidebarConfig} />
          )}
        </div>
        <div className="dm-footer-input-field w-100 position-relative">
          {/* <InputBoxField
            org_id={org_id}
            room_id={room_id}
            loggedInUser_id={loggedInUser_id}
          /> */}
        </div>
        {/* <MessageInputBox sendMessageHandler={console.log} /> */}
        {/* <CommentBox sendMessageHandler={console.log} /> */}
      </div>
      <div className="dm-plugin-right-sidebar" style={{ display: none }}>
        <ProfileSidebar
          none={none}
          setNone={setNone}
          grid={grid}
          setGrid={setGrid}
          actualUser={actualUser}
        />
      </div>
    </div>
  );
};
export default ChatHome;
