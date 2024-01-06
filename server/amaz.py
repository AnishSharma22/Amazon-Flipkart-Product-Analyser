from bs4 import BeautifulSoup
import requests

def amazonScrape(url):
  """
    Embark on a daring quest to scrape valuable information from the mystical Amazon webpage.

    Parameters:
    url (str): The URL of the Amazon product page.

    Returns:
    tuple: A treasure trove of information including the item name, a list of ratings, and a list of reviews.
  """
  # Prepare for the epic battle by gathering your tools and allies.
  url = str(url)
  print("Waiting for Amazon ⏳")
  while True:
    response = requests.get(url)
    html_content = response.text
    if response.status_code < 500: break

  print("Successful breach in the website 🦹 \n Status code: ", response.status_code)
  soup = BeautifulSoup(html_content, 'html.parser')

  # Unveil the hidden item name, a valuable artifact sought by many.
  span_elements = soup.find_all('span', id='productTitle')
  item_name = [span.text for span in span_elements]
  item_name = [item.replace("\xa0", "") for item in item_name]
  print("Target has been spotted 🎯")

  # Be vigilant for deceptive traps and confirm the existence of reviews.
  review_elements = soup.find('span', {'data-hook':'top-customer-reviews-title'})
  if not review_elements: pass
  elif review_elements.text == 'No customer reviews':
    print('Target was a fake! No reviews found!')
    return [item_name, None, None]
  
  print('Target has been confirmed! 😼')
  review_elements = soup.find_all('div', {'data-hook':'top-customer-reviews-widget' ,'class': 'a-section review-views celwidget'})
  rate_page = soup.find('a', {'data-hook': 'see-all-reviews-link-foot'})

  # Harness the power of navigation to explore the uncharted lands of reviews on the next page.
  def nextPage():
    """
        Venture forth to the next page of reviews, where greater treasures await.

        Returns:
        tuple: A magnificent collection of ratings and reviews.
    """

    page = 'http://' + 'www.amazon.in' + rate_page['href']
    url = str(page) 
    while True:
      response =  requests.get(url)
      html_content = response.text
      if response.status_code == 200: break

    print("Breached in target's mansion 🏡")
    rating_list = []   # Forge an empty list to store the ratings

    for review in review_elements:
        rating_elements = review.find_all('span', {'class': 'a-icon-alt'})
        ratings = [rating.text for rating in rating_elements]
        rating_list.extend(ratings)
    rating_list = [item.replace("out of 5 stars", "") for item in rating_list]
    print("Retreived target's room! ")

    review_text = []  # Conquer and gather the reviews

    for review in review_elements:
        rating_elements = review.find_all('span', {'data-hook':'review-body'})
        ratings = [rating.text for rating in rating_elements]
        review_text.extend(ratings)
    review_text = [item.replace("READ MORE", "") for item in review_text]
    review_text = [item.replace("\n", "") for item in review_text]
    print("Retreived target's organs! 🫀 ")
    return rating_list, review_text


  # Stand your ground and explore the reviews on the current page if the enemy remains vigilant.
  def thisPage():
    """
        Conquer the current page of reviews and claim your spoils.

        Returns:
        tuple: A collection of ratings and reviews to strengthen your cause.
    """
    
    rating_list = []  # Forge an empty list to store the ratings

    for review in review_elements:
          rating_elements = review.find_all('span', {'class': 'a-icon-alt'})
          ratings = [rating.text for rating in rating_elements]
          rating_list.extend(ratings)

    rating_list = [item.replace("out of 5 stars", "") for item in rating_list]
    print("Retreived target's room! ")

    review_text = []  # Conquer and gather the reviews

    for review in review_elements:
          rating_elements = review.find_all('div', {'data-hook':'review-collapsed'})
          ratings = [rating.text for rating in rating_elements]
          review_text.extend(ratings)

    review_text = [item.replace("READ MORE", "") for item in review_text]
    review_text = [item.replace("\n", "") for item in review_text]
    print("Retreived target's organs! 🫀 ")
    return rating_list, review_text

  # Choose your strategy wisely and embark on the path to victory.
  if rate_page == None:
    print("Target located nearby 🗺️")
    rating_list, review_text = thisPage()
  else:
    print("Target moved to the next page! The chase will not end! 😤")
    rating_list, review_text = nextPage()
  
  print("Waiting for Bard AI ⏳")
  return item_name, rating_list, review_text