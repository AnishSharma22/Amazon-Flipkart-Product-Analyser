import React from 'react';
import '../app/main.css';
import { LinearGradient } from 'react-text-gradients';

export const Title = () => {
  return (
    <div className='title flex justify-center items-center'>
        <h1>
            <LinearGradient gradient={['to bottom', '#ffffff ,#000000']}>
                Product Recommendation Engine
            </LinearGradient>
        </h1>
    </div>
  )
}
