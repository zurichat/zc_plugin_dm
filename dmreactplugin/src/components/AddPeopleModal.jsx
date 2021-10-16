// import { useState,useEffect } from "react";
// import Parcel from "single-spa-react/parcel"
// import { AddUserModal } from "@zuri/manage-user-modal"
// import { useSelector } from "react-redux";
// import { handleAddPeopleToRoom } from '../Redux/Actions/dmActions';
// import { useDispatch } from "react-redux";
// import {GetWorkspaceUsers} from "@zuri/control";

// const AddPeopleModal = ({showModal, setShowModal, org_id, room_id}) =>{
//     const dispatch = useDispatch();
//     const [workspaceUsers, setWorkspaceUsers]=useState([]);
//     useEffect(()=>{
//         async function call(){
//             try {
//                 const users = await GetWorkspaceUsers();
//                 setWorkspaceUsers(users);
//                 console.log("trying to see something",users)
//             }catch(error)
//             {
//                 console.log("Error gettingWorkspaceUsers",error)
//             }
//         }
//         call()
//     },[]);

//     const options = workspaceUsers ? Object.keys(workspaceUsers).map((key) => {
        
//         if (+key || +key === 0) {
//                 return workspaceUsers[key]
//          }
       
//     }).filter((item) => item) : [];
//     console.log("trynna see something here",options)

//     let userList = options.map((user)=>{
//         return{
//                 value:user._id,
//                 label:user.user_name,
//             };
//         });
//     console.log("work ijn",workspaceUsers)
//     console.log("let me see the data",options)
//     let show = showModal
    // let setShow = setShowModal
//     const defaultConfig = {
//         title: "Add users",
//         type: "inputbox",
//         userList: userList,
//         addMembersEvent: users => {
//           const member_id = users
          
//           const data={
//             room_id: room_id,
//             member_id: member_id,
//          }
//             console.log(member_id)
//             console.log("Add People modal post",data)
//             dispatch(handleAddPeopleToRoom(org_id, room_id, data))
            
//         },
//         show: show,
//         handleClose: function () {
//           this.show=setShowModal(false)
//         }
//       }
//     //   data.filter(obj => obj.value === selectedValue
//     return(
//     <Parcel
//     config={AddUserModal}
//     wrapWith="div"
//     parcelConfig={defaultConfig}
//     />
//    )

   
    
// }
// export default AddPeopleModal;