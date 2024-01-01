from bs4 import BeautifulSoup
import requests
import sys

def scrapeFlip(url):
  """
    Embark on a daring quest to scrape valuable information from the mystical Amazon webpage.

    Parameters:
    url (str): The URL of the Amazon product page.

    Returns:
    tuple: A treasure trove of information including the item name, a list of ratings, and a list of reviews.
  """

  # Prepare for the epic battle by gathering your tools and allies.
#   print("Waiting for Flipkart ⏳")
  while True:
    response = requests.get(url)
    html_content = response.text
    if response.status_code < 500: break

#   print("Successful breach in the website 🦹 \n Status code: ", response.status_code)
  soup = BeautifulSoup(html_content, 'html.parser')

  # Unveil the hidden item name, a valuable artifact sought by many.
  span_elements = soup.find_all('span', class_='B_NuCI')
  item_name = [span.text for span in span_elements]
  item_name = [item.replace("\xa0", "") for item in item_name]
#   print("Target has been spotted 🎯")

  # Be vigilant for deceptive traps and confirm the existence of reviews.
  rev0 = soup.find('span', {'class': '_13vcmD'})
  if rev0==None: 
    print('Target was a fake! No reviews found!')
    return item_name, None, None
  else:
    rev0 = rev0.find_next_sibling('span')
    rev0.text

#   print('Target has been confirmed! 😼')
  rate_page = soup.find('div', {'class': '_2c2kV-'})
  link = rate_page.find_next_sibling('a')
  review_elements = soup.find_all('div', {'class': '_1YokD2 _3Mn1Gg col-9-12'})

  # Harness the power of navigation to explore the uncharted lands of reviews on the next page.
  def nextPage():
    """
        Venture forth to the next page of reviews, where greater treasures await.

        Returns:
        tuple: A magnificent collection of ratings and reviews.
    """

    link = rate_page.find_next_sibling('a')
    link['href']
    page = 'http://' + 'www.flipkart.com' + link['href']
    url = str(page)  # Replace with the actual product URL
    while True:
      response = requests.get(url)
      html_content = response.text
      if response.status_code == 200: break

    soup = BeautifulSoup(html_content, 'html.parser')
    review_elements = soup.find_all('div', {'class': '_1YokD2 _3Mn1Gg col-9-12'})
    # print("Breached in target's mansion 🏡")
    rating_list = []  # Forge an empty list to store the ratings

    for review in review_elements:
        rating_elements = review.find_all('div', {'class': '_3LWZlK _1BLPMq'})
        ratings = [rating.text for rating in rating_elements]
        rating_list.extend(ratings)
    # print("Retreived target's room! ")
    review_text = []  # Conquer and gather the reviews

    for review in review_elements:
        rating_elements = review.find_all('div', {'class':'t-ZTKy'})
        ratings = [rating.text for rating in rating_elements]
        review_text.extend(ratings)

    review_text = [item.replace("READ MORE", "") for item in review_text]
    # print("Retreived target's organs! 🫀 ")
    return rating_list, review_text

  # Stand your ground and explore the reviews on the current page if the enemy remains vigilant.
  def thisPage():
    """
        Conquer the current page of reviews and claim your spoils.

        Returns:
        tuple: A collection of ratings and reviews to strengthen your cause.
    """

    s = soup.find_all('div', {'class': 't-ZTKy'})
    review_text = [] # Conquer and gather the reviews
    for item in s:
      review_text.append(item.text)
    review_text = [item.replace("READ MORE", "") for item in review_text]
    # print("Retreived target's organs! 🫀 ")
    return None, review_text

  rev0.text[3:]
  rev0
  # Choose your strategy wisely and embark on the path to victory.
  if rev0.text == '\xa00 Reviews': 
    # print('Target was a fake! No reviews found!')
    return item_name, None, None
  elif not link: 
    # print("Target located nearby 🗺️")
    rating_list, review_text = thisPage()
  else: 
    # print("Target moved to the next page! The chase will not end! 😤")
    rating_list, review_text = nextPage()

  return item_name, rating_list, review_text

if __name__ == "__main__":
    
    # url = sys.argv[1]
    # url = "https://www.flipkart.com/vikrida-smoke-360-degree-rotating-flip-acq/p/itma0a87f92f18b4?pid=RCTGPF454BJBJUR7&lid=LSTRCTGPF454BJBJUR7ZWQC46&marketplace=FLIPKART&store=tng%2F56a%2Ffq8&srno=b_1_11&otracker=hp_omu_Beauty%252C%2BFood%252C%2BToys%2B%2526%2Bmore_3_7.dealCard.OMU_JU776054Y0PY_5&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Beauty%252C%2BFood%252C%2BToys%2B%2526%2Bmore_NA_dealCard_cc_3_NA_view-all_5&fm=neo%2Fmerchandising&iid=en_JijsRQkiBpfwdjp0jhCNe8UfD3qAq6yNMuZ9p44m4glZ_sHpZmbcI2UIEuxFe49R_x0_3M64EgbikqXVeiKYQw%3D%3D&ppt=browse&ppn=browse"
    # item_name, rating_list, review_text = scrapeFlip(url)
    # print(item_name,rating_list,review_text)
    print("python function ran")