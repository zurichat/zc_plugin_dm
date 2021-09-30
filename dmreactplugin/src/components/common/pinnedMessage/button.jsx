import React from 'react';
import style from 'styled-components';

const Button = style.button`
    border: ${({ close }) => (close ? '1px solid grey' : 'none')};
    width: 100px;
    padding:10px;
    background-color: ${close ? 'transparent' : 'green'};
    margin-right:${close ? '10px' : '0'};
    color: ${close ? 'black' : 'white'}
    `;

const ModalButton = ({ close, onClick, children }) => {
    return (
        <Button close={close} onClick={onClick}>
            {children}
        </Button>
    );
};

export default ModalButton;
