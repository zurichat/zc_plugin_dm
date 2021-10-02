import React, {useState, useEffect} from 'react';
import SelectedUsersTag from './SelectedUsersTag';
import SearchedUsersModal from './SearchedUsersModal';


const SearchUsers = ({ orgUsers })=>{
    const [filteredUsers, setFilteredUsers] = useState([]);
    const [selectedUsers, setSelectedUsers] = useState([]);
    const [searchModalOpen, setSearchModalOpen] = useState(false);
    const [searchInputValue, setSearchInputValue] = useState('');
    const [fetchLoading, setFetchLoading] = useState(true)

    const filterUser = (searchInput, allUsers)=>{
        const newFilteredUsers = allUsers.filter((user)=>(
            user.user_name.toLowerCase().includes(searchInput.toLowerCase()) ||
            user.first_name.toLowerCase()
            .concat(` ${user.last_name.toLowerCase()}`)
            .includes(searchInput.toLowerCase()) ||
            user.email.toLowerCase().includes(searchInput.toLowerCase())
        ))

        setFilteredUsers(newFilteredUsers)
    }

    const searchUser = (e)=>{
        const searchInput = e.target.value
        setSearchInputValue(searchInput)
        if(searchInput){
            setSearchModalOpen(true)
        }else{
            setSearchModalOpen(false)
        }

        filterUser(searchInput, orgUsers || [])
    }

    const selectUser = (user)=>{
        const exists = selectedUsers.find((selectedUser=>(
            selectedUser._id  === user._id
        )))

        if(!exists && selectedUsers.length < 8){
            setSelectedUsers(selectedUsers.concat(user))
        }

        setSearchInputValue('')
        setSearchModalOpen(false)
    }

    const deselectUser = (user)=>{
        const newSelectedUsers = selectedUsers.filter((selectedUser)=>(
            selectedUser._id !== user._id
        ))

        setSelectedUsers(newSelectedUsers)
    }

    const clearTag = (e)=>{
        if(e.keyCode === 8 && !searchInputValue){
            const newSelectedUsers = selectedUsers.filter((selectedUser, i)=>(
                selectedUsers.length - 1 !== i
            ))
    
            setSelectedUsers(newSelectedUsers)
        }
    }

    useEffect(()=>{ 
        filterUser(searchInputValue, orgUsers || [])
        if( orgUsers && orgUsers.length){
            setFetchLoading(false)
        }

    }, [orgUsers])

    return(
        <div className="alldms-searchusers">
            <p>To:</p>
            <div className="alldms-searchusers-content">
                {
                    // selectedUsers.map((selectedUser)=>(
                    //     <SelectedUsersTag selectedUser={selectedUser}/>
                    // ))
                }
                {
                    selectedUsers[0] &&
                    <SelectedUsersTag selectedUser = {selectedUsers[0]} onClose = {deselectUser}/>
                }
                {
                    selectedUsers[1] &&
                    <SelectedUsersTag selectedUser = {selectedUsers[1]} onClose = {deselectUser}/>
                }
                {
                    selectedUsers[2] &&
                    <SelectedUsersTag selectedUser = {selectedUsers[2]} onClose = {deselectUser}/>
                }
                {
                    selectedUsers[3] &&
                    <SelectedUsersTag selectedUser = {selectedUsers[3]} onClose = {deselectUser}/>
                }
                <input
                    type='text'
                    placeholder={!selectedUsers.length? '@somebody or somebody@example.com': ''}
                    onChange = {searchUser}
                    onKeyDown = {clearTag}
                    value={searchInputValue}
                />
                <div className='alldms-searchedusersmodal-wrapper'>
                {
                    searchModalOpen &&
                    <SearchedUsersModal searchedUsers = {filteredUsers} onSelectUser = {selectUser} loading = {fetchLoading}/>
                }
                </div>
                {
                    selectedUsers.length === 8 &&
                    <div className='alldms-searchusers-warning'>
                            <p>Only 8 people can be in a direct message</p>
                    </div>
                }
            </div>
        </div>
    )
}

export default SearchUsers;