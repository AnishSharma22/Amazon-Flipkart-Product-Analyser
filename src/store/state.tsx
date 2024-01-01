import { Settings } from "http2";
import { atom } from "recoil";

export const textState = atom({
    key: 'textState', // unique ID (with respect to other atoms/selectors)
    default: `
    **Summary of Amazon Reviews:**
    
    - Overall positive reviews with an average rating of 3.9 out of 5.
    - Praised for its sturdiness, durability, and dishwasher safety.
    - Some reviewers found it comfortable to use and effective in making rotis.
    - A few complaints about the thinness and lack of comfort in handling the rolling pin.
    - Concerns raised about potential injuries if accidentally dropped on the feet.
    - Mixed opinions on the weight, with some finding it too heavy and others appreciating its stability.
    
    **Pros:**
    
    - Sturdy and durable stainless steel construction.
    - Dishwasher safe for easy cleaning.
    - Some reviewers found it comfortable to use and effective in making rotis.
    - Some reviewers found the weight to be good or appreciated its stability.
    
    **Cons:**
    
    - Some reviewers found it too thin and uncomfortable to handle.
    - Concerns raised about potential injuries if accidentally dropped on the feet.
    - Some reviewers found the weight to be too heavy.
    
    **Score:**
    
    7 out of 10.
    
    While the product has received mixed reviews, it seems to be a durable and functional rolling pin for making rotis. The main concerns are related to comfort and potential injuries, which may vary from person to person. Ultimately, the decision to purchase should be based on individual preferences and needs.
    ` // default value (aka initial value)
  });


  export const siteState = atom({
    key : 'siteState',
    default : 'amazon'
  });

  export const loadingState = atom({
    key : 'loadingState',
    default : false
  })