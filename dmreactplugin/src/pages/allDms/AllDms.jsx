import React from 'react';
import SearchUsers from './SearchUsers';
import { useSelector } from 'react-redux';
import './AllDms.css'

const AllDms = ()=>{
    const membersReducer = useSelector(({ membersReducer }) => membersReducer);

    const orgUsers = membersReducer;

    return(
        <div className='alldms'>
            <header className='alldms-header d-flex align-items-center'>
                <div className='alldms-header-text d-flex align-items-center'>
                    <p>#</p>
                    <p>All direct messages</p>
                </div>
            </header>
            <SearchUsers orgUsers = {orgUsers}/>
        </div>
    )
};

export default AllDms;