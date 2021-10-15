import React, { useEffect, useState, useRef, useMemo } from 'react';
import DmProfileHeader from '../components/dmProfileHeader';
import BookmarkHeader from '../components/common/addBookmarkKebab/dmBookMark';
import DmChatContainerBox from '../components/ChatContainer/dmChatContainerBox';
import InputBoxField from '../components/dmBoxInputField';
import PinnedMessage from '../components/common/pinnedMessage/dmPinnedMessages';
import { useDispatch } from 'react-redux';
// import { SubscribeToChannel } from '@zuri/utilities';
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
  console.log('rm', room_messages);
  const chatSidebarConfig = useMemo(() => ({
    sendChatMessageHandler: (msg) => {
      dispatch(
        handleCreateRoomMessages(org_id, room_id, {
          sender_id: loggedInUser_id,
          room_id,
          message: msg.message,
        })
      );
    },
    // messages: [
    //   { message: 'Cheeee', formatOptions: ['bold'] },
    //   { message: 'first message', formatOptions: ['bold', 'italic'] },
    //   {
    //     message: 'lossdnnkebgekeng bk gf gkf  hfk gk fw',
    //     formatOptions: ['italic'],
    //   },
    //   { message: 'hello world chat', formatOptions: [] },
    //   { message: 'second message', formatOptions: ['bold', 'italic'] },
    // ],
    // messages: room_messages?.results?.reverse().map((msg) => {
    //   console.log('lo', { ...msg, ormatOptions: ['bold', 'italic'] });
    //   return { ...msg, formatOptions: ['bold', 'italic'] };
    // }),
    currentUserData: {
      username: 'Aleey',
      imageUrl: '',
    },
    messages: [
      {
        username: 'Pidoxy',
        id: 7,
        time: '7:05PM',
        imageUrl: '',
        emojis: [
          { name: 'smiling', count: 4, emoji: '😋' },
          { name: 'grining', count: 1, emoji: '😊' },
        ],
        richUiData: {
          blocks: [
            {
              data: {},
              depth: 0,
              entityRanges: [],
              inlineStyleRanges: [],
              key: '543og',
              text: 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;. Nulla porttitor accumstincidunt.',
              type: 'unstyled',
            },
          ],
          entityMap: {},
        },
      },
      {
        username: 'Fortune',
        id: 7,
        time: '9:35PM',
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
              text: 'Qwertitgv asfjf jheiuhie vehhoe trices posdf sjde dewl;. Nulla porttitor accumstincidunt.',
              type: 'unstyled',
            },
          ],
          entityMap: {},
        },
      },
      {
        username: 'Detoun',
        id: 7,
        time: '12:15PM',
        imageUrl: '',
        emojis: [
          { name: 'cool', count: 9, emoji: '🥳' },
          { name: 'celebrate', count: 11, emoji: '🥂' },
        ],
        richUiData: {
          blocks: [
            {
              data: {},
              depth: 0,
              entityRanges: [],
              inlineStyleRanges: [],
              key: '543og',
              text: 'Portiioe asfjf jgjgioef vehhoe rtuwodd posdf sjde dewl;. Nulla porttitor accumstincidunt.',
              type: 'unstyled',
            },
          ],
          entityMap: {},
        },
      },
    ],
    showChatSideBar: true,
    chatHeader: 'Chats',
  }));
  const user2_id =
    roomsReducer?.room_info?.room_user_ids !== undefined &&
    roomsReducer?.room_info?.room_user_ids[1];
  const messages = room_messages?.results;

  const dispatch = useDispatch();
  // useEffect(() => {
  //   SubscribeToChannel(room_id, function (ctx) {
  //     console.log('room_id', ctx);
  //   });
  // }, []);
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
            room_id = {room_id}
            org_id = {org_id}
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
          {room_messages && <MessageBoard chatsConfig={chatSidebarConfig} />}
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
