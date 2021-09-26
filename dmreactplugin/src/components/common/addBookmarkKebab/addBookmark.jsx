import React, { useState } from 'react';

import Add from '../../../assets/img/svg/add.svg';

const AddBookmark = () => {
    const [open, setOpen] = useState(false);

    return (
        <div
            className='d-inline-flex align-items-center gap-1 px-3 py-1 rounded-3 position-relative'
            style={{ height: '30px', backgroundColor: '#BCF9E6' }}
            onClick={() => {
                setOpen(!open);
            }}
            role='presentation'
        >
            <img src={Add} alt='pin' className='h-50' />
            <div>Add a bookmark</div>
        </div>
    );
};

export default AddBookmark;
