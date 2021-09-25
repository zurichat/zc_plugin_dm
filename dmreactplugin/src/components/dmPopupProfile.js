import React from 'react';
import  '../assets/css/dmPopupProfile.css';



const dmpopupProfile = () => {
    return (
        
            <div className="dmUserContainer shadow bg-white">
               
            <div className="dmPopupImg">
                <img src="https://picsum.photos/200/300" alt="userimg" />
            </div>

            <div className="px-3">

                <div className="dmPopupName">
                    <h1>Mama Gee</h1>
                </div>
                <div className="dmPopupStack">
                    <p>Frontend Design Mentor</p>

                </div>
                <div className="dmPopupPronouns">
                    <p>She/her</p>

                </div>

                <div className="dmViewProfile mt-4">
                    <p>View Full Profile</p>
                </div>
                <div className="dmPopupStatus text-muted">
                    <p className="text-muted">Status</p>
                    <div className="dmFoxIcon">
                        <p>&#x1F43A;</p>
                    </div>
                
                </div>

                <div className="dmPopupTime text-muted">
                    <p>Local Time</p>
                    <p>3.15PM</p>
                    

                </div>
                <div className=" dmPopupFooter d-flex justify-content-between mb-3 popup_footer">
                    <button size="sm" variant="outline-secondary" className="lh-1"
                        >Message
                    </button>
                    <button size="sm" variant="outline-secondary" className="lh-1"
                        >Mute
                    </button>
                </div>
            </div>
                
                

            </div>
       
    )
}

export default dmpopupProfile

