import React from 'react';
import Image from 'next/image';
import githubLogo from '../images/github.png';
import amazonLogo from '../images/amazon.png';
import flipkartLogo from '../images/flipkart.png';
import Link from 'next/link';

export const Navbar = () => {
  return (
    <div className='flex justify-between items-center m-4 p-4 text-white'>
        <div>Target Locked! 🎯</div>
        <div className='flex'>
            <Link href="https://github.com/AnishSharma22/Amazon-Flipkart-Product-Analyser" target='_blank'><Image src={githubLogo} className='image' alt="github logo" /></Link>
            <Link href="https://amazon.in" target='_blank'><Image src={amazonLogo} className='image' alt="amazon logo" /></Link>
            <Link href="https://flipkart.in" target='_blank'><Image src={flipkartLogo} className='image' alt="flipkart logo" /></Link>
        </div>
    </div>
  )
}
 