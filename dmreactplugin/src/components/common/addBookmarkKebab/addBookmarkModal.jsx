import React, { useState } from 'react';

const AddBookmarkModal = ({ close, children }) => {
    const [show, setShow] = useState(true);
    if (close) {
    } else {
        setShow(close);
    }
    return (
        <div
            role='presentation'
            onClick={() => {
                setShow(false);
            }}
            className={`${
                show ? 'd-flex' : 'd-none'
            } fixed-top h-100 w-100 flex-column justify-content-center align-items-center zindex-modal`}
            style={{ backgroundColor: 'rgba(0,0,0,0.4)' }}
        >
            {children}
        </div>
    );
};

export default AddBookmarkModal;
