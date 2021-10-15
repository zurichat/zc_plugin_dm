import React from "react";
import './AllDms.css'

const DmCard = ({time,room_name,message,created_at,sender_id,image_url}) =>{
    return(
        <div className="DM-Card-Container">
            <h4 className="DM-AllDMs-MessageDate">{time}</h4>
            <div className="DM-AllDMs-Message"> 
            <div className="DM-AllDMs-MessageDetail-Left"> 
                <img src={image_url} alt="logo" />
                <div className="DM-AllDMs-MessageContent">
                <h4 className="DM-AllDMs-MessageSender"> {room_name}</h4>
                <p className="DM-AllDMs-MessageText"> {sender_id}: {message} </p>
                </div>
            </div>
            <div className="DM-AllDMs-MessageDetail-Right"> 
                <p className="DM-AllDMs-MessageTime"> {created_at} </p>
            </div>
            </div>
        </div>
    )
}
export default DmCard;