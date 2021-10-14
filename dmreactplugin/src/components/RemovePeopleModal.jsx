import React, {useState} from "react"
import Parcel from "single-spa-react/parcel"
import { AddUserModal } from "@zuri/manage-user-modal"


const AddPeopleModal = ({ShowModal}) =>{

  const defaultConfig = {
    title: "Add users",
    type: "removemodal",
    userList: [
      { value: "chocolate", label: "Chocolate" },
      
    ],
    addMembersEvent: users => {

    },
    show: true,
    handleClose: function () {
      this.show = false
    }
  }
    return(
    <Parcel
    config={AddUserModal}
    wrapWith="div"
    parcelConfig={defaultConfig}
    />
   )
}