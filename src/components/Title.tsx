import React from 'react';
import '../app/main.css';
import { LinearGradient } from 'react-text-gradients';

export const Title = () => {
  return (
    <div className='title flex justify-center items-center'>
        <h1 className='select-none'>
            <LinearGradient gradient={['to bottom', '#ffffff ,#000000']}>
                Product Recommendation Engine
                {process.env.NEXT_APP_BACKEND_URL}
            </LinearGradient>
        </h1>
    </div>
  )
}
