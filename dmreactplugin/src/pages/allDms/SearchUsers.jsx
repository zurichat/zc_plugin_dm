import React, {useState, useEffect} from 'react';
import SelectedUsersTag from './SelectedUsersTag';
import SearchedUsersModal from './SearchedUsersModal';


const SearchUsers = ({ orgUsers })=>{
    const newOrgUsers = orgUsers && orgUsers
    const [filteredUsers, setFilteredUsers] = useState(newOrgUsers);
    const [selectedUsers, setSelectedUsers] = useState([]);
    const [searchModalOpen, setSearchModalOpen] = useState(false);
    const [searchInputValue, setSearchInputValue] = useState('')

    const searchUser = (e)=>{
        const searchInput = e.target.value
        setSearchInputValue(searchInput)
        if(searchInput){
            setSearchModalOpen(true)
        }else{
            setSearchModalOpen(false)
        }

        console.log(filteredUsers)

        const newFilteredUsers = filteredUsers.filter((user)=>(
            user.user_name.toLowerCase().includes(searchInput.toLowerCase()) ||
            user.first_name.toLowerCase()
            .concat(` ${user.last_name.toLowerCase()}`)
            .includes(searchInput.toLowerCase())
        ))

        setFilteredUsers(newFilteredUsers)
        console.log(newFilteredUsers)
    }

    const selectUser = (user)=>{
        const exists = selectedUsers.find((selectedUser=>(
            selectedUser._id  === user._id
        )))

        if(!exists){
            setSelectedUsers(selectedUsers.concat(user))
        }

        setSearchInputValue('')
    }

    const deselectUser = (user)=>{
        const newSelectedUsers = selectedUsers.filter((selectedUser)=>(
            selectedUser._id !== user._id
        ))

        setSelectedUsers(newSelectedUsers)
    }

    useEffect(()=>{
        setFilteredUsers(orgUsers)
        console.log(orgUsers)
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
                <input
                    type='text'
                    placeholder={!selectedUsers.length? '@somebody or somebody@example.com': ''}
                    onChange = {searchUser}
                    value={searchInputValue}
                />
                <div className='alldms-searchedusersmodal-wrapper'>
                {
                    searchModalOpen &&
                    <SearchedUsersModal searchedUsers = {filteredUsers} onSelectUser = {selectUser}/>
                }
                </div>
                <div className='alldms-searchusers-warning'>
                    <p>Only 8 people can be in a direct message</p>
                </div>
            </div>
        </div>
    )
}

export default SearchUsers;