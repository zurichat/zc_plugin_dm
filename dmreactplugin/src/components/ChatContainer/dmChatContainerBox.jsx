import React, { useState } from 'react';
import MessageWrapper from '../common/dmHoverState/dmHoverstate';
import DmInitMessageBox from '../dmInitMessagebox';
import DmSingleMessageContainer from '../dmSingleMessageContainer';
import DmReplyInThread from '../ReplyInThread/replyInThread';

import './chatContainerBox.css';

const DmChatContainerBox = () => {
    const [openThread, setOpenThread] = useState(false);

    const handleOpenThread = () => {
        setOpenThread(true);
    };

    const handleCloseThread = () => {
        setOpenThread(false);
    };

    return (
        <>
            <div className='dm-chatContainerBox w-100 d-flex align-items-end'>
                <main>
                    <DmInitMessageBox />
                    {}
                    <MessageWrapper handleOpenThread={handleOpenThread}>
                        <DmSingleMessageContainer />
                    </MessageWrapper>
                    <MessageWrapper handleOpenThread={handleOpenThread}>
                        <DmSingleMessageContainer />
                    </MessageWrapper>
                </main>
                <aside className={`asideContent ${openThread ? 'active' : ''}`}>
                    <DmReplyInThread handleCloseThread={handleCloseThread} />
                </aside>
            </div>
        </>
    );
};

export default DmChatContainerBox;
