from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gemini
import amaz
import flip
import markdown

app = FastAPI()

# Define allowed origins for CORS (you might want to adjust this based on your requirements)
origins = ["*"]

# Add CORS middleware to allow requests from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/backend/api")
def receive_data(payload: dict):  # Remove the ': json' type hint
    link = payload.get('link')
    site = payload.get('site')
    
    if site == 'amazon':
        try:
            [item_name, rating_list, review_text] = amaz.amazonScrape(link)
        except Exception as e:
            return {"error": f"Error while scraping Amazon: {str(e)}"}
    elif site == 'flipkart':
        try:
            [item_name, rating_list, review_text] = flip.scrapeFlip(link)
        except Exception as e:
            return {"error": f"Error while scraping Flipkart: {str(e)}"}
    else:
        return {"error": "Wrong site"}
    
    try:
        response = gemini.fetchGeminiResponse(item_name, rating_list, review_text,site)
        print(response)
        review_val = False if review_text is None else True

        if response:
            htmlContent = markdown.markdown(response, extensions=['markdown.extensions.tables'])
            return [htmlContent,review_val]
        else:
            return {"error": "Error generating Gemini response"}
    except Exception as e:
        return {"error": f"Error in Gemini response generation: {str(e)}"}
