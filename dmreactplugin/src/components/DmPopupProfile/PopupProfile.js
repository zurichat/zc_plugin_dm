import React from 'react';
import '../../assets/css/profilePopupDm.css';

const PopupProfile = ({ handleViewProfile, user }) => {
  return (
    <div className='dmUserContainer'>
      <div className='dmPopupImg'>
        <img src={user?.image_url} alt='userimg' />
      </div>

      <div className='px-3'>
        <div className='dmPopupName'>
          <h1>
            {user?.first_name || 'John'} {user?.last_name || 'DOE'}
          </h1>
        </div>
        <div className='dmPopupStack'>
          <p>{user?.role}</p>
        </div>
        <div className='dmPopupPronouns'>
          <p>{user?.pronouns || 'He/She'}</p>
        </div>

        <div className='dmViewProfile mt-2'>
          <p onClick={handleViewProfile}>View Full Profile</p>
        </div>
        <div className='dmPopupStatus text-muted'>
          <p className='text-muted'>Status</p>

          <p>{user?.status || 'No Status'}</p>
        </div>

        <div className='dmPopupTime text-muted'>
          <p>Local Time</p>
          <p>{new Date().toLocaleTimeString()}</p>
        </div>
        <div className=' dmPopupFooter popup_footer'>
          <button className='dm_button'>Message</button>
          <button className='dm_button'>Mute</button>
        </div>
      </div>
    </div>
  );
};

export default PopupProfile;
