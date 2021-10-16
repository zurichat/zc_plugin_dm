import React, {useEffect} from 'react';
import SearchUsers from './SearchUsers';
import { useSelector } from 'react-redux';
import './AllDms.css'


const DefaultNoDms=()=>{
  return(
    <div>
      <p>Keep Track of your conversations with teammates</p>
      <p>You'll see a list of all your direct messages here-with all the latest messages at the top</p>
      <p>so you can tell what's new at a glance</p>
    </div>
  )
}

const AllDms = ({org_id, loggedInUser_id})=>{
    const membersReducer = useSelector(({ membersReducer }) => membersReducer);
    const orgUsers = membersReducer;

    return(
      
        <div className='alldms'>
            <header className='alldms-header d-flex align-items-center'>
                <div className='alldms-header-text d-flex align-items-center'>
                    <p>#</p>
                    <p>All direct messages</p>
                </div>
            </header>
            <SearchUsers orgUsers = {orgUsers} org_id={org_id} loggedInUser_id={loggedInUser_id}/>

        <div className="DM-AllDMs">
          <div className="DM-AllDMs-MessageWrapper"> 
            <h4 className="DM-AllDMs-MessageDate"> Today </h4>
            <div className="DMcard__body__card1">
              
            <div  className="DM-AllDMs-Message"> 
              <div className="DM-AllDMs-MessageDetail-Left"> 
                <img src="https://bit.ly/sage-adebayo" alt="logo" />
                  <div className="DM-AllDMs-MessageContent">
                    <h4 className="DM-AllDMs-MessageSender"> StartUPJahswill </h4>
                    <p className="DM-AllDMs-MessageText"> SeunPaul: Good Morning </p>
                  </div>
              </div>
              <div className="DM-AllDMs-MessageDetail-Right"> 
                <p className="DM-AllDMs-MessageTime"> 09:00am </p>
              </div>
            </div>
          
            <div className="DM-AllDMs-Message"> 
            <div className="DM-AllDMs-MessageDetail-Left"> 
              <img src="https://bit.ly/sage-adebayo" alt="logo" />
              <div className="DM-AllDMs-MessageContent">
                <h4 className="DM-AllDMs-MessageSender"> Duvie </h4>
                <p className="DM-AllDMs-MessageText"> You: What's up with the endpoint? </p>
              </div>
            </div>
            <div className="DM-AllDMs-MessageDetail-Right"> 
              <p className="DM-AllDMs-MessageTime"> 11:05am </p>
            </div>
          </div>
          </div>
          </div>
         
          <div className="DM-AllDMs-MessageWrapper"> 
          <h4 className="DM-AllDMs-MessageDate"> Yesterday </h4>  
          <div className="DMcard__body__card1">
          <div className="DM-AllDMs-Message"> 
            <div className="DM-AllDMs-MessageDetail-Left"> 
              <img src="https://bit.ly/sage-adebayo" alt="logo" />
              <div className="DM-AllDMs-MessageContent">
                <h4 className="DM-AllDMs-MessageSender"> Naza </h4>
                <p className="DM-AllDMs-MessageText"> Aniebiet: Hello mentor, I think my friend... </p>
              </div>
            </div>
            <div className="DM-AllDMs-MessageDetail-Right"> 
              <p className="DM-AllDMs-MessageTime"> 10:00am </p>
            </div>
          </div>
          <div className="DM-AllDMs-Message"> 
            <div className="DM-AllDMs-MessageDetail-Left"> 
              <img src="https://bit.ly/sage-adebayo" alt="logo" />
              <div className="DM-AllDMs-MessageContent">
                <h4 className="DM-AllDMs-MessageSender"> Ufon </h4>
                <p className="DM-AllDMs-MessageText"> Ufon: @Channel </p>
              </div>
            </div>
            <div className="DM-AllDMs-MessageDetail-Right"> 
              <p className="DM-AllDMs-MessageTime"> 13:00pm </p>
            </div>
          </div>
         </div>
         </div>
         
         
          <div className="DM-AllDMs-MessageWrapper"> 
          <h4 className="DM-AllDMs-MessageDate"> Friday, October 4th  </h4>
          <div className="DMcard__body__card1">
          <div className="DM-AllDMs-Message"> 
            <div className="DM-AllDMs-MessageDetail-Left"> 
              <img src="https://bit.ly/sage-adebayo" alt="logo" />
              <div className="DM-AllDMs-MessageContent">
                <h4 className="DM-AllDMs-MessageSender"> Richard </h4>
                <p className="DM-AllDMs-MessageText"> Victor: Hey man </p>
              </div>
            </div>
            <div className="DM-AllDMs-MessageDetail-Right"> 
              <p className="DM-AllDMs-MessageTime"> 05:45am </p>
            </div>
          </div>
          <div className="DM-AllDMs-Message"> 
            <div className="DM-AllDMs-MessageDetail-Left"> 
              <img src="https://bit.ly/sage-adebayo" alt="logo" />
              <div className="DM-AllDMs-MessageContent">
                <h4 className="DM-AllDMs-MessageSender"> Haven </h4>
                <p className="DM-AllDMs-MessageText"> Kemzi: How far your task? </p>
              </div>
            </div>
            <div className="DM-AllDMs-MessageDetail-Right"> 
              <p className="DM-AllDMs-MessageTime"> 09:00am </p>
            </div>
          </div>
          <div className="DM-AllDMs-Message"> 
            <div className="DM-AllDMs-MessageDetail-Left"> 
              <img src="https://bit.ly/sage-adebayo" alt="logo" />
              <div className="DM-AllDMs-MessageContent">
                <h4 className="DM-AllDMs-MessageSender"> Nathan </h4>
                <p className="DM-AllDMs-MessageText"> Mark: Na cruising since morning oh </p>
              </div>
            </div>
            <div className="DM-AllDMs-MessageDetail-Right"> 
              <p className="DM-AllDMs-MessageTime"> 12:10pm </p>
            </div>
          </div>
          <div className="DM-AllDMs-Message"> 
            <div className="DM-AllDMs-MessageDetail-Left"> 
              <img src="https://bit.ly/sage-adebayo" alt="logo" />
              <div className="DM-AllDMs-MessageContent">
                <h4 className="DM-AllDMs-MessageSender"> Xylux </h4>
                <p className="DM-AllDMs-MessageText"> You: Good evening </p>
              </div>
            </div>
            <div className="DM-AllDMs-MessageDetail-Right"> 
              <p className="DM-AllDMs-MessageTime"> 17:00pm </p>
            </div>
          </div>
          </div>
         </div>
        </div></div>
         )

          


      // const orgUsers = [
    //     {
    //         _id: "6145f987285e4a18402074eb",
    //         user_name: "seunpaul",
    //         first_name: "Seun",
    //         last_name: "Oluwafemi",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a44202074eb",
    //         user_name: "casper",
    //         first_name: "Tobi",
    //         last_name: "Amasa",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18472074eb",
    //         user_name: "andy",
    //         first_name: "Anu",
    //         last_name: "Adewale",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18402174ec",
    //         user_name: "fado",
    //         first_name: "Fuad",
    //         last_name: "Agboola",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18402084ed",
    //         user_name: "richycool",
    //         first_name: "Richard",
    //         last_name: "Olufarati",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285b4a18402074eb",
    //         user_name: "damiDev",
    //         first_name: "Dami",
    //         last_name: "Smith",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18404474eb",
    //         user_name: "Haywhy._Online",
    //         first_name: "Ayo",
    //         last_name: "Amoo",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f457285e4a18402074eb",
    //         user_name: "wallyStrinGs",
    //         first_name: "Wale",
    //         last_name: "Ademilola",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18542074eb",
    //         user_name: "LaCasera",
    //         first_name: "David",
    //         last_name: "Adeoye",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987272e4a18402074eb",
    //         user_name: "INEC",
    //         first_name: "Damilare",
    //         last_name: "Atanda",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     }
    // ] */}
    // )
};



export default AllDms;