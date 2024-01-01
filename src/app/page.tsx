"use client"
import { Navbar } from '@/components/Navbar';
import './main.css';
import { Title } from '@/components/Title';
import { Searchbox } from '@/components/Searchbox';
import { Button } from '@/components/Button';
import { RecoilRoot } from 'recoil';
import { TextArea } from '@/components/TextArea';
import { Line } from '@/components/Line';

export default function Home() {
  return (
    <RecoilRoot>
      <Line/>
      <Navbar />
      <Title />
      <Searchbox />
      <Button />
      <TextArea />
    </RecoilRoot>
  );
}
