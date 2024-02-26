import requests
import json

RAPIDAPI_KEY = "2c075b4f3fmshb5d3ce684922cf0p19def5jsncd23118591ad"

def get_hotel_info(hotel_data):
    hotel_id = hotel_data['hotel_id']
    print("[+] Getting info about hotel: {}".format(hotel_id))
    url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelDetails"

    querystring = {"hotel_id":hotel_id,"arrival_date":"2024-04-26","departure_date":"2024-05-11", "languagecode":"en-us","currency_code":"USD"}

    headers = {
    	"X-RapidAPI-Key": RAPIDAPI_KEY,
	    "X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()
    
    if (response['status'] == 'false'):
        return None

    response = response['data']
    
    min_price = response['product_price_breakdown']['gross_amount_per_night']
    max_price = response['product_price_breakdown']['all_inclusive_amount']
       
    ret = {
        "name": response['hotel_name'][0:50],
        "address": response['address'],
        "latitude": response['latitude'],
        "longitude": response['longitude'],
        "properties": list(map(lambda x: x['name'], response['facilities_block']['facilities'])),
        "min_price": min_price['value'],
        "max_price": max_price['value'],
        "review": hotel_data['review_score'],
        "image": hotel_data['main_photo_url'].replace("square60", "max750"),
        "hotel_id": hotel_id
    }
    ret["map"] = "https://www.google.com/maps/place/" + str(ret["latitude"]) + "," + str(ret["longitude"])
    return ret





def get_nearcoords(latitude, longitude, k=5):
    print("[+] Getting nearby hotels ({}, {})".format(latitude, longitude))
    url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotelsByCoordinates"
    
    querystring = { 
        "latitude": str(latitude),
        "longitude": str(longitude),
        "arrival_date": "2024-04-26", 
        "departure_date": "2024-05-11",
        "adults": "1", 
        "children_age": "0,17",
        "room_qty": "1",
        "languagecode": "en-us",
        "currency_code":"EUR"
    }
    
    headers = {
	    "X-RapidAPI-Key": RAPIDAPI_KEY,
    	"X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()['data']['result']
    return data[0:k]
