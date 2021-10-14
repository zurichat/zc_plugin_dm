import Parcel from "single-spa-react/parcel"
import { AddUserModal } from "@zuri/manage-user-modal"
// import { useSelector } from "react-redux";


const InputBox = () =>{

    const parcelConfig = {
    title: "Add People",
    type: "inputbox",
    showModal: true,
    userList: [
        { value: "chocolate", label: "Chocolate" },
        { value: "strawberry", label: "Strawberry" },
        { value: "vanilla", label: "Vanilla" }
    ],
    addMembersEvent: (users)=>{
        console.log("This is a test",users)
    },
    }
    return(
    <Parcel
    config={AddUserModal}
    wrapWith="div"
    parcelConfig={parcelConfig}
    />
   )
}
export default InputBox;