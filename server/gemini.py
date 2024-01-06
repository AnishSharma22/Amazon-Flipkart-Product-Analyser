import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('GOOGLE_API_KEY') # google api key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')




def fetchGeminiResponse(item_name, rating_list, review_text,site):
    item_name = str(item_name)
    if(rating_list):
        rating_str = ", ".join(str(rating) for rating in rating_list)
    if(review_text):
        review_str = ", ".join(str(review) for review in review_text)

    if not review_text:
        print('No reviews found, our product rating might not be accurate...')
        prompt = (
            f"I found this item on {site} named {item_name}. "
            "Summarize this product based off its ratings and product description within 30 lines "
            "and generate a table containing pros and cons of this product. "
            "Also, give a score out of 10 whether one should buy this product or not." 
        )
    else:
        prompt = (
            f"I found this item on {site} named {item_name}. "
            "Summarize these Amazon reviews based off its product ratings and description on its webpage within 30 lines. "
            "Generate a table containing pros and cons of this product. "
            f"The reviews are: {review_str} and their respective ratings are: {rating_str}. "
            "Also, give a score out of 10 whether one should buy this product or not."
        )
    
    print("Waiting for Gemini ⏳")
    response = model.generate_content(prompt)  # Ensure await here if this operation is asynchronous
    response = response.text
    return response
