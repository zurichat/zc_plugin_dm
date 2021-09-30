import React from 'react';
import { useSelector } from 'react-redux';
import '../assets/css/dmInitMessagebox.css';
import { BsChatDots } from 'react-icons/bs';
import ReactTooltip from 'react-tooltip';

const DmInitMessageBox = ({ secondUser }) => {
  const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);
  const { description } = roomsReducer?.room_info;
  return (
    <>
      <div className='d-flex align-item-center flex-row py-4 px-3'>
        <div className='link-btn '>
          <button className='btn-outline-disabled btn-dm-chat'>
            <BsChatDots />
          </button>
        </div>
        <div className='px-3 chat-description'>
          <h6 className='m-0 dmInitmessageHeadText'>
            This conversation is just between the two of you
          </h6>
          <p className='m-0 dmInitmessageSubText'>
            Here you can send messages and share files with{' '}
            <span
              style={{ color: '#1264A3' }}
              className='dmSecondUsersName'
              data-tip
              data-for='userInfoPopUp'
            >
              @{secondUser?.user_name}
            </span>
            <ReactTooltip id='userInfoPopUp' effect='solid'>
              <div className='dm-message-data-tip-pop-up'>
                <img
                  src={secondUser?.image_url}
                  alt=''
                  className='dm-message-data-tip-pop-up-image'
                  width='20'
                  height='20'
                />
                {secondUser?.first_name && secondUser?.last_name && (
                  <span className='dm-message-data-tip-pop-up-fullname'>
                    {`${secondUser?.first_name} ${secondUser?.last_name}`}
                  </span>
                )}

                <span className='dm-message-data-tip-pop-up-active-status'></span>
                {secondUser?.user_name && (
                  <span className='dm-message-data-tip-pop-up-username'>
                    {secondUser?.user_name}
                  </span>
                )}
                {secondUser?.status && (
                  <span className='dm-message-data-tip-pop-up-status'>
                    {secondUser?.status}
                  </span>
                )}
              </div>
            </ReactTooltip>
          </p>
        </div>
      </div>
    </>
  );
};
export default DmInitMessageBox;
