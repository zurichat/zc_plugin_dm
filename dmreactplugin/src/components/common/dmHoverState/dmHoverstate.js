import React, { useState } from "react";
import './../src/App.css';
import { CgSmile } from "react-icons/cg";
import { BsChatDots } from 'react-icons/bs';
import { FiShare2 } from 'react-icons/fi';
import { CgBookmark } from 'react-icons/cg';
import { CgMoreVertical } from 'react-icons/cg';
import ReactTooltip from 'react-tooltip'


function dmHoverstate() {
  const [isShown, setIsShown] = useState(false);

  return (
    <div className="dmHover">

      {isShown && (
        <div className="dmCover">
         <ul  className="dmIcons">
           <li className="dmLi"><CgSmile ref={ref => this.fooRef = ref} data-tip='Add reaction'/></li>
           <li className="dmLi"><BsChatDots ref={ref => this.fooRef = ref} data-tip='Reply in thread'/></li>
           <li className="dmLi"><FiShare2 ref={ref => this.fooRef = ref} data-tip='Share message...'/></li>
           <li className="dmLi"><CgBookmark ref={ref => this.fooRef = ref} data-tip='Add to saved items'/></li>
           <li className="dmLi"><CgMoreVertical ref={ref => this.fooRef = ref} data-tip='More actions'/></li>
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

export default dmHoverstate;
