import React from 'react';
import DmInitMessageBox from './dmInitMessagebox';
import DmSingleMessageContainer from './dmSingleMessageContainer';

const DmChatContainerBox = () => {
    return (
        <>
            <div className='dm-chatcontainer-box'>
                <DmInitMessageBox />
                <DmSingleMessageContainer />
            </div>
        </>
    );
};

export default DmChatContainerBox;
