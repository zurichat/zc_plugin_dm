import React from 'react';
import loading_gif from './loading.gif';

const SearchedUsersModal = ({
    searchedUsers,
    onSelectUser,
    loading,
    roomLoading,
}) => {
    return (
        <div className='alldms-searchedusersmodal'>
            {roomLoading && (
                <p className='loading-text'>
                    <img className='loading-gif' src={loading_gif} alt='' />
                    Please wait, loading room...
                </p>
            )}
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
                searchedUsers.map((user)=>(
                    <div className="user" onClick = {()=>{onSelectUser(user)}}>
                        <div
                            className="user-picture"
                            style={{
                            backgroundImage:
                                `url(${user.image_url})`,
                            }}
                        ></div>
                        <p><span>{user.user_name} O </span>{user.first_name} {user.last_name}</p>
                    </div>
                ))
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
                        onSelectUser(searchedUsers[5]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[5].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[5].user_name} O </span>
                        {searchedUsers[5].first_name}{' '}
                        {searchedUsers[5].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[6] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[6]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[6].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[6].user_name} O </span>
                        {searchedUsers[6].first_name}{' '}
                        {searchedUsers[6].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[7] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[7]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[7].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[7].user_name} O </span>
                        {searchedUsers[7].first_name}{' '}
                        {searchedUsers[7].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[8] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[8]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[8].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[8].user_name} O </span>
                        {searchedUsers[8].first_name}{' '}
                        {searchedUsers[8].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[9] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[9]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[9].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[9].user_name} O </span>
                        {searchedUsers[9].first_name}{' '}
                        {searchedUsers[9].last_name}
                    </p>
                </div>
            )}
            {searchedUsers[10] && (
                <div
                    className='user'
                    onClick={() => {
                        onSelectUser(searchedUsers[10]);
                    }}
                >
                    <div
                        className='user-picture'
                        style={{
                            backgroundImage: `url(${searchedUsers[10].image_url})`,
                        }}
                    ></div>
                    <p>
                        <span>{searchedUsers[10].user_name} O </span>
                        {searchedUsers[10].first_name}{' '}
                        {searchedUsers[10].last_name}
                    </p>
                </div>
            )}
        </div>
    );
};

export default SearchedUsersModal;
