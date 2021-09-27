import React from 'react';

import  '../assets/css/dmBoxInput.css';
import { FaAngleDown, FaSlash} from 'react-icons/fa';
import {  BsLightning, BsLink45Deg, BsListUl, BsTypeItalic, } from 'react-icons/bs';
import { FiAtSign, FiBold, FiSend, FiPaperclip} from 'react-icons/fi';





const dmBoxInput = () => {
    return (
        <div className="inputboxcontainer">
            <div className="first-box">
                <input type="text" placeholder="Send a message to John"></input>
            </div>

            <div className="second-box">

                <div>
                < BsLightning className='bslight'/>
                </div>

                <div>
                <FaSlash  className='line'/>
                </div>


                <div>
                <FiBold className='bold'/>
                </div>

                <div>
                <BsTypeItalic  className='italic'/>  
                </div>

                <div>
                < BsLink45Deg  className='link'/>
                </div>

                <div>
                <BsListUl  className='list'/>
                </div>

                <div>
                <FiAtSign className='at'/>

                </div>
                <FiPaperclip  className='clip'/>

                <div>                
                <FiSend  className='send'/>   
                </div>

                <div>
                <FaSlash  className='line'/>
                </div>

                <div>
                <FaAngleDown  className='angledown'/> 
                </div>
            
            
            
            </div>

        </div>
    )
}

export default dmBoxInput
