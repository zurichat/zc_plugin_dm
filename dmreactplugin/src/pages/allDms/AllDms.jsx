import moment from 'moment';
import { Link } from 'react-router-dom';
import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import './AllDms.css';
import SearchUsers from './dmSearchBox/SearchUsers';
import { handleAllDms } from '../../Redux/Actions/dmActions';

const AllDms = () => {
	const dispatch = useDispatch();

	const authReducer = useSelector(({ authReducer }) => authReducer);
	const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);
	const membersReducer = useSelector(({ membersReducer }) => membersReducer);

	useEffect(() => {
		dispatch(handleAllDms(authReducer.organisation, authReducer.user._id));
	}, []);

	return (
		<div className="alldms">
			<header className="alldms-header d-flex align-items-center">
				<div className="alldms-header-text d-flex align-items-center">
					<p>#</p>
					<p>All direct messages</p>
				</div>
			</header>

			<SearchUsers
				orgUsers={membersReducer.members}
				org_id={authReducer.organisation}
				loggedInUser_id={authReducer.user._id}
			/>

			<div className="DM-AllDMs">
				<div className="DM-AllDMs-MessageWrapper">
					{roomsReducer.all_dms === null ? (
						<div className="DM-AllDMs-MessageWrapper-Loading">
							<div className="DM-AllDMs-MessageWrapper-Loading-Spinner">
								<div className="DM-AllDMs-MessageWrapper-Loading-Spinner-1"></div>
								<div className="DM-AllDMs-MessageWrapper-Loading-Spinner-2"></div>
								<div className="DM-AllDMs-MessageWrapper-Loading-Spinner-3"></div>
							</div>
							<p>Loading...</p>
						</div>
					) : (
						<>
							{roomsReducer.all_dms &&
								roomsReducer.all_dms.results.map((dm) => {
									return (
										<Link to={`/${dm.room_id}`} key={dm.id}>
											<div className="DM-AllDMs-MessageWrapper">
												<div className="DM-AllDMs-Message">
													<div className="DM-AllDMs-MessageDetail-Left">
														<img
															src="https://images.unsplash.com/photo-1513152697235-fe74c283646a?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fHByb2ZpbGUlMjBwaG90b3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
															alt="logo"
														/>
														<div className="DM-AllDMs-MessageContent">
															<h4 className="DM-AllDMs-MessageSender">
																{dm.sender_id}
															</h4>
															<p className="DM-AllDMs-MessageText">
																{dm.sender_id}:{' '}
																{dm.message}
															</p>
														</div>
													</div>
													<div className="DM-AllDMs-MessageDetail-Right">
														<p className="DM-AllDMs-MessageTime">
															{moment(
																dm.created_at
															).format('h:mm a')}
														</p>
													</div>
												</div>
											</div>
										</Link>
									);
								})}

							{roomsReducer.all_dms.results.length === 0 ? (
								<div className="DM-AllDMs-MessageWrapper-NoDMs">
									<p>No direct messages yet</p>
								</div>
							) : null}
						</>
					)}
				</div>
			</div>
		</div>
	);
};

export default AllDms;
