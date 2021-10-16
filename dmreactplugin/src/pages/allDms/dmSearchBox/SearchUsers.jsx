import { useHistory } from 'react-router';
import { useDispatch, useSelector } from 'react-redux';
import React, { useState, useEffect, useRef } from 'react';

import SelectedUsersTag from './SelectedUsersTag';
import SearchedUsersModal from './SearchedUsersModal';
import { handleCreateDmRoom, handleSetRoom } from '../../../Redux/Actions/dmActions.js';

const SearchUsers = ({ orgUsers }) => {
    const [filteredUsers, setFilteredUsers] = useState([]);
    const [selectedUsers, setSelectedUsers] = useState([]);
    const [searchModalOpen, setSearchModalOpen] = useState(false);
    const [searchInputValue, setSearchInputValue] = useState('');
    const [fetchLoading, setFetchLoading] = useState(true);
    const [roomLoading, setRoomLoading] = useState(false);

    const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);
    const authReducer = useSelector(({ authReducer }) => authReducer);

    const history = useHistory();

    const searchInputRef = useRef(null);

    const dispatch = useDispatch();

    const filterUser = (searchInput, allUsers) => {
        const newFilteredUsers = allUsers.filter(
            (user) =>
                user.user_name
                    .toLowerCase()
                    .includes(searchInput.toLowerCase()) ||
                user.first_name
                    .toLowerCase()
                    .concat(` ${user.last_name.toLowerCase()}`)
                    .includes(searchInput.toLowerCase()) ||
                user.email.toLowerCase().includes(searchInput.toLowerCase())
        );

        setFilteredUsers(newFilteredUsers);
    };

    const searchUser = (e) => {
        const searchInput = e.target.value;
        setSearchInputValue(searchInput);
        if (searchInput) {
            setSearchModalOpen(true);
        } else {
            setSearchModalOpen(false);
        }

        filterUser(searchInput, orgUsers || []);
    };

    const selectUser = (user) => {
        const exists = selectedUsers.find(
            (selectedUser) => selectedUser._id === user._id
        );

        if (!exists && selectedUsers.length < 8) {
            setSelectedUsers(selectedUsers.concat(user));
        }

        setSearchInputValue('');
        setSearchModalOpen(false);
        searchInputRef.current.focus();
    };

    const deselectUser = (user) => {
        const newSelectedUsers = selectedUsers.filter(
            (selectedUser) => selectedUser._id !== user._id
        );

        setSelectedUsers(newSelectedUsers);
        searchInputRef.current.focus();
    };

    const onCreateRoom = () => {
        setRoomLoading(true);
        const room_name_list = selectedUsers.map((user) => user.user_name);

        const room_name = room_name_list.join(', ');

        const selectedUsersIds = selectedUsers.map((user) => user._id);

        if (selectedUsers.length) {
            dispatch(
                handleCreateDmRoom({
                    org_id: authReducer.organisation,
                    member_id: authReducer.user._id,
                    user_ids: selectedUsersIds,
                    room_name,
                })
            );
        }
    };

    const onKeyEvent = (e) => {
        if (e.keyCode === 8 && !searchInputValue) {
            deselectUser(selectedUsers[selectedUsers.length - 1]);
        }

        if (e.keyCode === 13) {
            onCreateRoom();
            setSearchModalOpen(true);
        }
    };

    useEffect(() => {
        if (roomsReducer.room_id) {
            setRoomLoading(false);
            const redirectTo = `/${roomsReducer.room_id}`;
            history.push(redirectTo);
            dispatch(handleSetRoom(null));
        }
    }, [roomsReducer]);

    useEffect(() => {
        filterUser(searchInputValue, orgUsers || []);
        if (orgUsers && orgUsers.length) {
            setFetchLoading(false);
        }
    }, [orgUsers]);

    return (
        <div className='alldms-searchusers'>
            <p>To:</p>
            <div className='alldms-searchusers-content'>
                {
                    // selectedUsers.map((selectedUser)=>(
                    //     <SelectedUsersTag selectedUser={selectedUser}/>
                    // ))
                }
                {selectedUsers[0] && (
                    <SelectedUsersTag
                        selectedUser={selectedUsers[0]}
                        onClose={deselectUser}
                    />
                )}
                {selectedUsers[1] && (
                    <SelectedUsersTag
                        selectedUser={selectedUsers[1]}
                        onClose={deselectUser}
                    />
                )}
                {selectedUsers[2] && (
                    <SelectedUsersTag
                        selectedUser={selectedUsers[2]}
                        onClose={deselectUser}
                    />
                )}
                {selectedUsers[3] && (
                    <SelectedUsersTag
                        selectedUser={selectedUsers[3]}
                        onClose={deselectUser}
                    />
                )}
                {selectedUsers[4] && (
                    <SelectedUsersTag
                        selectedUser={selectedUsers[4]}
                        onClose={deselectUser}
                    />
                )}
                {selectedUsers[5] && (
                    <SelectedUsersTag
                        selectedUser={selectedUsers[5]}
                        onClose={deselectUser}
                    />
                )}
                {selectedUsers[6] && (
                    <SelectedUsersTag
                        selectedUser={selectedUsers[6]}
                        onClose={deselectUser}
                    />
                )}
                {selectedUsers[7] && (
                    <SelectedUsersTag
                        selectedUser={selectedUsers[7]}
                        onClose={deselectUser}
                    />
                )}
                {selectedUsers[8] && (
                    <SelectedUsersTag
                        selectedUser={selectedUsers[8]}
                        onClose={deselectUser}
                    />
                )}

                <input
                    type='text'
                    placeholder={
                        !selectedUsers.length
                            ? '@somebody or somebody@example.com'
                            : ''
                    }
                    onChange={searchUser}
                    onKeyDown={onKeyEvent}
                    ref={searchInputRef}
                    value={searchInputValue}
                />
                <div className='alldms-searchedusersmodal-wrapper'>
                    {searchModalOpen && (
                        <SearchedUsersModal
                            searchedUsers={filteredUsers}
                            onSelectUser={selectUser}
                            loading={fetchLoading}
                            roomLoading={roomLoading}
                        />
                    )}
                </div>
                {selectedUsers.length === 8 && (
                    <div className='alldms-searchusers-warning'>
                        <p>Only 8 people can be in a direct message</p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default SearchUsers;
