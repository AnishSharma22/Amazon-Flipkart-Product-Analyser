import React from 'react'
import { useRecoilState } from 'recoil';
import { textState } from '../store/state';
import "../app/main.css";


export const TextArea = () => {
    const [text] = useRecoilState(textState);
  return (
    <div className=' flex justify-center items-center text-white'>
        <div className=' mainText'>{text}</div>
    </div>
  )
}
