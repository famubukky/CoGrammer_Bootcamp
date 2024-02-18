#codes to calculate user's total holiday cost that inludes his plane cost, hotel cost and car-rental cost
def hotel_cost(num_nights):
# Let's assume the hotel cost per night is $100  
    return num_nights * 100  
def plane_cost(city_flight):
#Lets assume sample flight cost for different cities
    if city_flight == "New York":
        return 500
    elif city_flight == "Paris":
        return 700
    elif city_flight == "Tokyo":
        return 900
    else:
        return 0 #Default case, no flight cost for unknown city
def car_rental(rental_days):
    #Assumming the daily car rental cost is $50
      return rental_days * 50
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental
if __name__ == "__main__":
    city_flight = input("Enter the city you will be flying to (New York, Paris, Toyko): ") #This line of code ask user to input the city he will be flying to between New york, Paris and Tokyo
    num_nights = int(input("Enter the number of nights you will be staying at a hotel: ")) #This line of code ask user to input the number of days he will be staying in hotel
    rental_days = int(input("Enter the number of days you will be hiring a car:  ")) #This line of code ask user to input the number of days he will hire a car 
    
    total_hotel_cost = hotel_cost(num_nights) #Line of code that display total hotel cost
    total_plane_cost = plane_cost(city_flight) #Line of code that display total plane cost
    total_car_rental_cost = car_rental(rental_days) #Line of code that display total car rental cost
    total_holiday_cost = holiday_cost(total_hotel_cost, total_plane_cost, total_car_rental_cost) #Line of code that display total holiday cost

    
    
print("\nHoliday Details:") #Line of code that print holiday details
print(f"City Flight: {city_flight}") #Line of code that print city flight details
print(f"Hotel Cost for {num_nights} nights: ${total_hotel_cost}") #Line of code that prints total hotel cost
print(f"Flight Cost: ${total_plane_cost}") #Line of code that prints total plane cost details
print(f"Car Rental Cost for {rental_days} days: ${total_car_rental_cost}") #Line of code that prints total car rental cost
print(f"Total Holiday Cost: ${total_holiday_cost}") #Line of code that prints total holiday cost 
