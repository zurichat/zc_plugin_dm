import React from 'react';
import './dmSingleMessageContainer.css';

const dmSingleMessageContainer=()=>{
    return (
    <div class="row align-items-end message-box">
        <div className="d-flex flex-column">
            <div className="d-flex fw-bolder">
                <div className="card-texting">
                    <img src="https://in.images.search.yahoo.com/search/images;_ylt=AwrwS5lvFE5htjUAawC7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3Nj?p=image+placeholder&type=E211IN826G91521&ei=UTF-8&fr=mcafee&th=105.1&tw=100.2&imgurl=https%3A%2F%2Fwww.dovercourt.org%2Fwp-content%2Fuploads%2F2019%2F11%2F610-6104451_image-placeholder-png-user-profile-placeholder-image-png.jpg&rurl=https%3A%2F%2Fwww.dovercourt.org%2Fhome__trashed%2F610-6104451_image-placeholder-png-user-profile-placeholder-image-png%2F&size=16KB&name=610-6104451_image-placeholder-png-user-profile-placeholder-image-png+...&oid=5&h=881&w=840&turl=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.iYpFSu2O2kVP1OptEdJ-uwHaHx%26pid%3DApi%26rs%3D1%26c%3D1%26qlt%3D95%26w%3D100%26h%3D105&tt=610-6104451_image-placeholder-png-user-profile-placeholder-image-png+...&sigr=5ovOL12n1RmR&sigit=Xq.mzWQMUjJX&sigi=84E.pqZQMEpi&sign=AmqZxT7rvC5E&sigt=AmqZxT7rvC5E"/>
                </div>
                <div className="card-text ms-3">
                    <span>John</span> 
                        <DateHeader>YYMMDD</DateHeader>
                    <div className="timings"> 
                        <p>
                            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. 
                            The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here,
                            content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum
                            as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. 
                            Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like). 
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div className="d-flex flex-column">
            <div className="d-flex fw-bolder">
                <div className="card-texting">
                    <img src="https://in.images.search.yahoo.com/search/images;_ylt=AwrwS5lvFE5htjUAawC7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3Nj?p=image+placeholder&type=E211IN826G91521&ei=UTF-8&fr=mcafee&th=105.1&tw=100.2&imgurl=https%3A%2F%2Fwww.dovercourt.org%2Fwp-content%2Fuploads%2F2019%2F11%2F610-6104451_image-placeholder-png-user-profile-placeholder-image-png.jpg&rurl=https%3A%2F%2Fwww.dovercourt.org%2Fhome__trashed%2F610-6104451_image-placeholder-png-user-profile-placeholder-image-png%2F&size=16KB&name=610-6104451_image-placeholder-png-user-profile-placeholder-image-png+...&oid=5&h=881&w=840&turl=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.iYpFSu2O2kVP1OptEdJ-uwHaHx%26pid%3DApi%26rs%3D1%26c%3D1%26qlt%3D95%26w%3D100%26h%3D105&tt=610-6104451_image-placeholder-png-user-profile-placeholder-image-png+...&sigr=5ovOL12n1RmR&sigit=Xq.mzWQMUjJX&sigi=84E.pqZQMEpi&sign=AmqZxT7rvC5E&sigt=AmqZxT7rvC5E"/>
                </div>
                <div className="card-text ms-3">John
                    YYMMDD
                    <div className="timings">
                        <li>
                            <p>
                                It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. 
                                The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here,
                                content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum
                                as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. 
                                Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like). 
                            </p>
                        </li>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
)}

export default dmSingleMessageContainer;

{/* <Container ref={messageListRef}>
      <ul>
        {error ? error : null}
        {!data || !data.Mesage ? <p>Select a channel</p> : null}
        {!loading && data && data.Mesage
          ? Object.keys(dates).map(key => (
              <div key={key}>
                <DateHeader>
                  {isToday(new Date(dates[key][0].date))
                    ? rtf.format(0, 'day')
                    : isYesterday(new Date(dates[key][0].date))
                    ? rtf.format(-1, 'day')
                    : key}
                </DateHeader>
                {dates[key].map((message: any) => {
                  return (
                    <li key={message.id}>
                      <Username>{message.User.username}</Username>
                      <DateSpan>{df.format(new Date(message.date))}</DateSpan>
                      <p>{message.body}</p>
                    </li>
                  );
                })}
              </div>
            ))
          : null}
      </ul>
    </Container> */}
// /*
