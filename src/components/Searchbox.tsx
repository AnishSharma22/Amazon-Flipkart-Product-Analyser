import React from "react";
import "../app/main.css";
import { useRecoilState } from "recoil";
import { amazonState, flipkartState, inputBoxState } from "@/store/state";
import {z} from 'zod';



export const Searchbox = () => {
  const [isAmazonActive, setIsAmazonActive] = useRecoilState(amazonState);
  const [isFlipkartActive, setIsFlipkartActive] = useRecoilState(flipkartState);
  const [input,setInput] = useRecoilState(inputBoxState);
  

  const handleButtonClick = (platform: string) => {
    if (platform === "amazon") {
      setIsAmazonActive(true);
      setIsFlipkartActive(false);
    } else if (platform === "flipkart") {
      setIsFlipkartActive(true);
      setIsAmazonActive(false);
    }
  };

  return (
    <div className="flex justify-center items-center flex-col my-5 mx-20">
      <div className="switcholder select-none">
        <span
          className={`slider ${isAmazonActive ? "amazon-active" : ""} ${
            isFlipkartActive ? "flipkart-active" : ""
          }`}
        ></span>
        <button
          style={{
            zIndex: "100",
            opacity: isAmazonActive ? "1" : "0.5",
            transition: "0.1s",
          }}
          onClick={() => handleButtonClick("amazon")}
        >
          Amazon
        </button>
        <button
          style={{
            zIndex: "100",
            opacity: isFlipkartActive ? "1" : "0.5",
            transition: "0.1s",
          }}
          onClick={() => handleButtonClick("flipkart")}
        >
          Flipkart
        </button>
      </div>
      <div className="w-4/5 flex justify-center items-center">
        <input
        placeholder="Enter Link"
        className="w-4/5 inputText"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        />
      </div>
    </div>
  );
};
