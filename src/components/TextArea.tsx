import React from 'react';
import { useRecoilState } from 'recoil';
import { flipkartState, loadingState, notFoundState, textState } from '../store/state';
import '../app/main.css';

export const TextArea = () => {
  const [text] = useRecoilState(textState);
  const [loading] = useRecoilState(loadingState);
  const [nfs] = useRecoilState(notFoundState);
  const [flipState] = useRecoilState(flipkartState);

  const createMarkup = () => {
    return { __html: text };
  };

  return (
    <div className='flex justify-center items-center text-white flex-col'>
      {!loading && text.length > 0 && !nfs && (
        <div className='mt-8 p-4 mainText' style={{
          backgroundColor: 'rgba(255, 108, 108, 0.2)',
          borderRadius: '0.3em',
          color: 'rgb(255, 222, 222)',
          fontSize: '1em'
        }}>
          No reviews found, our product rating might not be accurate...
        </div>
      )}
      {loading ? (
        <div className="lds-ellipsis my-20"><div></div><div></div><div></div><div></div></div>
      ) : (
        !flipState ? (
          <div className='mainText' dangerouslySetInnerHTML={createMarkup()}></div>
        ) : (
          <div></div>
        )
      )}
    </div>
  );
};
