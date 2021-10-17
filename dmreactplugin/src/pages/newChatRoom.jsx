import moment from 'moment';
import React, { useEffect, useState, useMemo } from 'react';
import { useParams } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { MessageBoard } from '@zuri/zuri-ui';
import { SubscribeToChannel } from '@zuri/utilities';

import './newChatRoom.css';
import DmProfileHeader from '../components/dmProfileHeader';
import BookmarkHeader from '../components/common/addBookmarkKebab/dmBookMark';
import PinnedMessage from '../components/common/pinnedMessage/dmPinnedMessages';
import ProfileSidebar from '../components/profileSidebar/profileSidebar';
import {
  handleGetRoomInfo,
  handleGetRoomMessages,
  handleCreateRoomMessages,
} from '../Redux/Actions/dmActions';

// Chat Home Page
const ChatHome = () => {
  const { room_id } = useParams({});
  const dispatch = useDispatch();

  const authReducer = useSelector(({ authReducer }) => authReducer);
  const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);
  const membersReducer = useSelector(({ membersReducer }) => membersReducer);

  useEffect(() => {
    dispatch(handleGetRoomMessages(authReducer.organisation, room_id));
    dispatch(handleGetRoomMessages(authReducer.organisation, room_id));
    dispatch(handleGetRoomInfo(authReducer.organisation, room_id));
    SubscribeToChannel(room_id, (ctx) => {
      switch (ctx.data.event) {
        case 'message_create':
          dispatch(handleGetRoomMessages(authReducer.organisation, room_id));
          break;

        default:
          console.log(ctx);
          break;
      }
    });
  }, []);

  const currentUser = membersReducer.members?.find(
    (member) => member._id === authReducer.user._id
  );
  useEffect(() => {}), [];

  const chatSidebarConfig = {
    chatHeader: 'Chats',
    showChatSideBar: true,
    sendChatMessageHandler: (msg) => {
      dispatch(
        handleCreateRoomMessages(authReducer.organisation, room_id, {
          sender_id: authReducer.user._id,
          room_id,
          message: msg.richUiData.blocks[0].text,
        })
      );
    },
    currentUserData: {
      username: currentUser?.user_name || 'John Doe',
      imageUrl: '',
    },
    messages: roomsReducer.room_messages?.results
      .map((message) => {
        return {
          username: currentUser?.user_name || 'John Doe',
          id: message.id,
          time: moment(message.created_at).format('hh:mm A'),
          imageUrl: '',
          emojis: [],
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
  };

  const user2_id =
    roomsReducer.room_info?.room_user_ids !== undefined &&
    roomsReducer.room_info?.room_user_ids[1];

  const actualUser = membersReducer.members?.find(
    (member) => member._id === user2_id
  );

  const [grid, setGrid] = useState('');
  const [none, setNone] = useState('none');

  return (
    <div className="dm-plugin-full-page" style={{ display: grid }}>
      <div className="dm-newchat-room">
        <div className="dm-chatroom-header">
          {/* <DmProfileHeader
						user2_id={user2_id}
						actualUser={actualUser}
						none={none}
						setNone={setNone}
						grid={grid}
						setGrid={setGrid}
					/> */}
          <div className="dm-bookmark-head">
            <div className="add-bookmark gap-2 d-flex flex-direction-column flex-flow align-items-center px-3 py-1">
              <PinnedMessage room_id={room_id} actualUser={actualUser} />
              <BookmarkHeader />
            </div>
          </div>
        </div>
        <div className="dm-message-in-out-box w-100 h-100 position-relative row align-items-end">
          {roomsReducer.room_messages && membersReducer.members && (
            <MessageBoard chatsConfig={chatSidebarConfig} />
          )}
        </div>
        <div className="dm-footer-input-field w-100 position-relative"></div>
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
