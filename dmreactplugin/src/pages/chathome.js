import React from 'react';

import DmInputTextField from '../../old/components/common/dmInputTextField/dmInputTextField';
import DmFullProfile from '../../old/components/DmFullProfile/DmFullProfile';
import ThreeDotKebab from '../../old/components/common/threeDotKebabMenu/threeDotKebab';

const ChatHome = () => {
    return (
        <div className='chat-home'>
            <DmFullProfile />
            <DmInputTextField />
            {/* This is the Popup menu for the threeDotKebab from the hover state */}
            <ThreeDotKebab />
        </div>
    );
};

export default ChatHome;
