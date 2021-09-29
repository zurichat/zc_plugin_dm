import React, {useState} from "react"
import "./threeDotKebab.css"
import { FaUniregistry } from "react-icons/fa"
import { IoIosArrowForward } from "react-icons/io"
import { RiParkingLine } from "react-icons/ri"
import { BiEditAlt } from "react-icons/bi"
import { HiOutlineExternalLink } from "react-icons/hi"
import { MdPoll } from "react-icons/md"
// import { IoLogoMedium } from "react-icons/io"
function ThreeDotKebab() {
  
  const [secondPopupOpen,setSecondPopupOpen]=useState(false)
  return ( <>
     <div className="Dm-ThreeDotKebab-Menu-FirstPopup">
      <div className="DmMenuListBorder">Turn off notififcations for replies

      </div>
      <div > 
          Mark Unread
        <FaUniregistry /></div>
      <div onClick={()=>setSecondPopupOpen(!secondPopupOpen)}>Remind me about this <IoIosArrowForward /></div>
      <div>Copy Link</div>
      <div>Pin to this conversation <RiParkingLine /> </div>
      <div>Edit Message <BiEditAlt /></div>
      <div className="DmPollMore DmPollMoreSpecial"> <MdPoll/>  Turn question into poll</div> 
      <div className="DmPollMore">More message shortcuts <HiOutlineExternalLink /></div>
      </div>
     
     {
       secondPopupOpen && <div className="Dm-ThreeDotKebab-Menu-SecondPopup">
         <div>In 20 minutes</div>
          <div>In 1 hour</div>
         <div>In 3 hours</div>
         <div>Tomorrow</div>
         <div>Next week</div>
         <div className="Dm-ThreeDotKebab-Menu-SecondPopupCustom">Custom... <span>M</span> </div>
       </div>
     }
   </>
  )
  }
  export default ThreeDotKebab