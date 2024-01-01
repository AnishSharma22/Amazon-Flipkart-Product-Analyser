import React from 'react'
import "../app/main.css";
import { useRecoilState } from 'recoil';
import { loadingState } from '@/store/state';

export const Line = () => {
    const [loading] = useRecoilState(loadingState);
  return (
    <div>
        {loading && <hr className='w-full bg-white h-1 gradient-line' />}
    </div>
    
  )
}
