import React from "react";
import "../app/main.css";
import { useRecoilState, useSetRecoilState } from "recoil";
import { amazonState, inputBoxState, loadingState, notFoundState, textState } from "@/store/state";
import {z} from 'zod';
import axios from "axios";

const flipkartProductLinkSchema = z.string().refine((val) => {
  const flipkartRegex = /https?:\/\/(www\.)?flipkart\.com\/.*/;
  return flipkartRegex.test(val);
}, {
  message: 'Please enter a valid Flipkart product link',
});

const amazonProductLinkSchema = z.string().refine((val) => {
  const amazonRegex = /https?:\/\/(www\.)?amazon\.in\/.*/;
  return amazonRegex.test(val);
}, {
  message: 'Please enter a valid Amazon product link',
});

export const Button = () => {
  const backend_url = process.env.NEXT_PUBLIC_BACKEND_URL || 'localhost:8000';
  const [link] = useRecoilState(inputBoxState);
  const [site] = useRecoilState(amazonState);
  const [loading,setLoading] = useRecoilState(loadingState);

  const setText = useSetRecoilState(textState);
  const setNotFoundState = useSetRecoilState(notFoundState);

  const handleGoButton = async () => {
    try {
      if (site === true) {
        if (flipkartProductLinkSchema.safeParse(link).success) {
          throw new Error('Please provide an Amazon link, not a Flipkart link');
        }
        amazonProductLinkSchema.parse(link);
      } else if (site === false) {
        if (amazonProductLinkSchema.safeParse(link).success) {
          throw new Error('Please provide a Flipkart link, not an Amazon link');
        }
        flipkartProductLinkSchema.parse(link);
      } else {
        throw new Error('Site value is invalid');
      }
      
      
      setLoading(true);
      const response = await axios.post(`http://${backend_url}/backend/api`, {
        site: site ? 'amazon' : 'flipkart',
        link: String(link),
      });
  
      setText(response.data[0]);
      setLoading(false);
      setNotFoundState(response.data[1]);
      console.log(response.data);
    } catch (error) {
      if (error instanceof Error) {
        console.log("Error:", error.message); // Correctly accesses the 'message' property
        // Handle the error message in your UI state or display it to the user
      } else {
        console.log("Unknown error occurred:", error);
      }
    }
  };
  

  return (
    <div className="flex justify-center items-center">
    {site && (
    <button
      className="button-85"
      style={loading ? { opacity: '0.3' } : {}}
      role="button"
      onClick={handleGoButton}
      disabled={loading} // Disable the button if loading is true
    >
      Go
    </button>
  )}
    
  {!site && (
    <div className='mt-8 p-4 mainText' style={{ backgroundColor: 'rgba(255,108,108,0.2)', borderRadius: '0.3em', color: 'rgb(255,222,222)', fontSize: '1em' }}>
      Flipkart Servers are currently unable to respond...
    </div>
  )}
</div>

  );
};
