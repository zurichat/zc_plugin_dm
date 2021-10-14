import { useState } from "react";
import Parcel from "single-spa-react/parcel"
import { AddUserModal } from "@zuri/manage-user-modal"
import { useSelector } from "react-redux";
import { handleAddPeopleToRoom } from '../Redux/Actions/dmActions';
import { useDispatch } from "react-redux";

const AddPeopleModal = ({showModal, org_id, room_id}) =>{
    // const [showModal,setShowModal] = useState(false)
    // setShow=setShowModal;
    const dispatch = useDispatch()
    // const addPeople = () => {
    //   const data={
    //     room_id: room_id,
    //     member_id: member_id,
    // }
    //     // ApiServices.postMessageThread(org_id, room_id, "61584d6e87675da1c20179fa", data).then(response=>{
    //     //   console.log(response);
    //     console.log("Add People modal post",data)
    //     // dispatch(handleAddPeopleToRoom(org_id, room_id, data))
    
        
    // }
    const membersReducer = useSelector(({ membersReducer }) => membersReducer);
    console.log("This is a test", membersReducer)
    const [show,setShow]=useState(showModal);
        // setShow(showModal)
    // const parcelConfig = {
    // title: "Add People",
    // type: "addmodal",
    // showModal: `${show}`,
    // userList: [
    //     { value: "chocolate", label: "New Member" },
    // ],
    // addMembersEvent: (users)=>{
    //     // console.log("This is a test",users)
    //     users = member_id
    //     addPeople()
    // },
    // }
    const defaultConfig = {
        title: "Add users",
        type: "addmodal",
        userList: [
          { value: "Workspace User 1", label: "Workspace User 1" },
          
        ],
        addMembersEvent: users => {
          // console.warn(users)
          const member_id = users
          const data={
            room_id: room_id,
            member_id: member_id,
         }
            console.log(member_id)
            console.log("Add People modal post",data)
            // dispatch(handleAddPeopleToRoom(org_id, room_id, data))
            // addPeople()
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
export default AddPeopleModal;