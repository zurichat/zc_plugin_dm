import React from 'react';
import { FaTimes } from 'react-icons/fa';

const SelectedUsersTag = ({ selectedUser, onClose }) => {
	return (
		<div className="alldms-seleteduserstag">
			<div
				className="user-picture"
				style={{
					backgroundImage: `url(${selectedUser.image_url})`,
				}}
			></div>
			<p>{selectedUser.user_name}</p>
			<div
				className="remove-selecteduser-btn"
				onClick={() => {
					onClose(selectedUser);
				}}
			>
				<FaTimes />
			</div>
		</div>
	);
};

export default SelectedUsersTag;
