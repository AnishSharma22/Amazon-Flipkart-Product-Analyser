import React from "react";
import "../app/main.css";
import { useRecoilState, useSetRecoilState } from "recoil";
import { siteState } from "@/store/state";

export const Searchbox = () => {
    const setSite = useSetRecoilState(siteState);
    const [site] = useRecoilState(siteState);
    return (
        <div className="flex justify-between items-center my-5 mx-20 w-full h-20">
            <div className="flex justify-center items-center flex-col">
                {site==='amazon' ? <button className="common Amazon" onClick={() => setSite('amazon')}>Amazon</button> : <button className="Amazon" onClick={() => setSite('amazon')}>Amazon</button>}
                {site==='flipkart' ? <button className="common Flipkart" onClick={() => setSite('flipkart')}>Flipkart</button> :<button className="Flipkart" onClick={() => setSite('flipkart')}>Flipkart</button>}
            </div>
            <div className="w-4/5 flex justify-center items-center absolute">
                <input placeholder="Enter Link" className="w-4/5 inputText" />
            </div>
            <div className="w-64">
            </div>
        </div>
    );
};
