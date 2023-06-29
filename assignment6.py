
import requests
from bs4 import BeautifulSoup
import pandas

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num = 3
scrapped_info_list = [] 
connect.connect(args.dbname)

for page_num in range(1, page_num_MAX):
    url = oyo_url + str(page_num)
    print("GET Request for:" + url )
    req = request.get(url)
    content = req.content

   soup = BeautifulSoup(content, "html.parser")

   all_hotels = soup.find_all("div", {"class": "hotelCaedListing"})
   
   for hotel in all_hotels:
       
       hotel_dict = {}
       hotel_dict["name"] = hotel.find("h3", {"class":"listinghotelDecsription__hotelName"}).text
       hotel_dict["address"] = hotel.find("span", {"itemprop":"streetAddress"})
       hotel_dict["price"] = hotel.find("span", {"class": "listingPrice_finalPrice"}).text
       # try .... expect
       try:
           hotel_dict["rating]" = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
       expept AttributeError: 
        pass
    
    parent_amenities_element = hotel.find("div", {"class": "amenitiesWrapper"})
    
    amenities_list = []
    for amenity in parent_amenities_element.find_all("div", {"class": "amenitiesWrapper__amenity"}):
        amenities_list.append(amenity.find("span", {"class": "d-body-sm.d-textEllipsis"}).text.strip())
    
    hotel_dict["amenities"] = ', '.join(amenities_list[:-1])
    
    scrapped_info_list.append(hotel_dict):
    # print(hotel_name, hotel_address, hotel_price, hotel_rating, amenities_list)
    
dataFrame = pandas.DataFrame(scrapped_info_list)
print("Creating csv file...")
dataframe.to_csv("Oyo.csv")    
    