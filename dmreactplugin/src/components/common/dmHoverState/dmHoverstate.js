import React, { useState } from "react";
import '../dmHoverState/dmHoverstate.css';
import { BiSmile } from 'react-icons/bi';
import { BsFillChatDotsFill } from 'react-icons/bs';
import { FiShare2 } from 'react-icons/fi';
import { GiSaveArrow } from 'react-icons/gi';
import { AiOutlineMore } from 'react-icons/ai';
import ReactTooltip from 'react-tooltip'


function dmHoverState() {
    const [isShown, setIsShown] = useState(false);
  
    return (
      <div className="dmHover">
  
        {isShown && (
          <div>
           <ul  className="dmIcons">
             <li><BiSmile ref={ref => this.fooRef = ref} data-tip='Add reaction'/></li>
             <li><BsFillChatDotsFill ref={ref => this.fooRef = ref} data-tip='Reply in thread'/></li>
             <li><FiShare2 ref={ref => this.fooRef = ref} data-tip='Share message...'/></li>
             <li><GiSaveArrow ref={ref => this.fooRef = ref} data-tip='Add to saved items'/></li>
             <li><AiOutlineMore ref={ref => this.fooRef = ref} data-tip='More actions'/></li>
           </ul>
           <ReactTooltip />
          </div>
        )}
        <span  className="dmState"
          onMouseEnter={() => setIsShown(true)}
          onMouseLeave={() => setIsShown(true)}>
          Sample Message Thread
        </span>
        
      </div>
    );
  }
  
  export default dmHoverState;
  