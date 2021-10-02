import React from 'react';
import loading_gif from './loading.gif';

const SearchedUsersModal = ({ searchedUsers, onSelectUser, loading }) => {
    return (
        <div className='alldms-searchedusersmodal'>
            {loading && (
                <p className='loading-text'>
                    <img className='loading-gif' src={loading_gif} alt='' />
                    Loading results...
                </p>
            )}
            {!searchedUsers.length && !loading && (
                <p className='notFound-text'>No matches Found</p>
            )}
            {
                // searchedUsers.map((user)=>(
                //     <div className="user" onClick = {()=>{onSelectUser(user)}}>
                //         <div
                //             className="user-picture"
                //             style={{
                //             backgroundImage:
                //                 `url(${user.image_url})`,
                //             }}
                //         ></div>
                //         <p><span>{user.user_name} O </span>{user.first_name} {user.last_name}</p>
                //     </div>
                // ))
            }
            {searchedUsers[0] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[0]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[0].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[0].user_name} O </span>
                        {searchedUsers[0].first_name}{' '}
                        {searchedUsers[0].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[1] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[1]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[1].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[1].user_name} O </span>
                        {searchedUsers[1].first_name}{' '}
                        {searchedUsers[1].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[2] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[2]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[2].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[2].user_name} O </span>
                        {searchedUsers[2].first_name}{' '}
                        {searchedUsers[2].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[3] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[3]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[3].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[3].user_name} O </span>
                        {searchedUsers[3].first_name}{' '}
                        {searchedUsers[3].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[4] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[4]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[4].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[4].user_name} O </span>
                        {searchedUsers[4].first_name}{' '}
                        {searchedUsers[4].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[5] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[4]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[4].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[4].user_name} O </span>
                        {searchedUsers[4].first_name}{' '}
                        {searchedUsers[4].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[6] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[4]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[4].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[4].user_name} O </span>
                        {searchedUsers[4].first_name}{' '}
                        {searchedUsers[4].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[7] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[4]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[4].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[4].user_name} O </span>
                        {searchedUsers[4].first_name}{' '}
                        {searchedUsers[4].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[8] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[4]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[4].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[4].user_name} O </span>
                        {searchedUsers[4].first_name}{' '}
                        {searchedUsers[4].last_name}
                    </p>
                </div>
            )}
        </div>
    );
};

export default SearchedUsersModal;
