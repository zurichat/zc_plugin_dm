import React, { useState } from 'react';
import './dmHoverstate.css';
import { VscReactions } from 'react-icons/vsc';
import { BsChatDots } from 'react-icons/bs';
import { FiShare2 } from 'react-icons/fi';
import { CgBookmark } from 'react-icons/cg';
import { CgMoreVertical } from 'react-icons/cg';
import ReactTooltip from 'react-tooltip';
import ThreeDotKebab from '../threeDotKebabMenu/threeDotKebab';

function MessageWrapper({ children, handleOpenThread, messages }) {
  const [isShown, setIsShown] = useState(false);
  const [isAppear, setIsAppear] = useState(false)

  return (
    <div
      className='dmHover'
      onMouseOver={() => setIsShown(true)}
      onMouseLeave={() => setIsShown(false)}
    >
      {isShown && (
        <div className='dmCover'>
          <ul className='dmIcons'>
            <li className='dmLi'>
              <VscReactions
                ref={(ref) => (this.fooRef = ref)}
                data-tip='Add reaction'
              />
            </li>
            <li className='dmLi' onClick={handleOpenThread}>
              <BsChatDots
                ref={(ref) => (this.fooRef = ref)}
                data-tip='Reply in thread'
              />
            </li>
            <li className='dmLi'>
              <FiShare2
                ref={(ref) => (this.fooRef = ref)}
                data-tip='Share message...'
              />
            </li>
            <li className='dmLi'>
              <CgBookmark
                ref={(ref) => (this.fooRef = ref)}
                data-tip='Add to saved items'
              />
            </li>
            <li className='dmLi'>
              <CgMoreVertical className="Dm-ThreeDotkebabMenu-MoreActions"
              onClick={() => setIsAppear(!isAppear)}
                ref={(ref) => (this.fooRef = ref)}
                data-tip='More actions'
              />
             
            </li>
          </ul>
          <ReactTooltip />
           
        </div>
      )}
      {children}
      {isAppear && <ThreeDotKebab className="Dm-ThreeDotKebabMenu-Appear" messages={messages}/>}
    </div>
  );
}

export default MessageWrapper;
