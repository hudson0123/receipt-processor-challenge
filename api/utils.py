import re
import math

def calculate_points(data):
    points = 0

    #  print(points)    
    # One point for every alphanumeric character in the retailer name.
    points += len(re.findall(r'[a-zA-Z0-9]', data['retailer']))
    
    print(points)
    # 50 points if the total is a round dollar amount with no cents.
    if data['total'][-2:] == "00":
        points += 50
        
    print(points)
    # 25 points if the total is a multiple of 0.25.
    if data['total'][-2:] == "00" or data['total'][-2:] == "25" or data['total'][-2:] == "50" or data['total'][-2:] == "75":
        points += 25
        
    print(points)
    # 5 points for every two items on the receipt.
    for x in range(len(data['items']) // 2):
        points += 5
        
    print(points)    
    # If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in data['items']:
        if len(item['shortDescription'].strip()) % 3 == 0:
            points += math.ceil(float(item['price']) / 5.0)    
     
    # 6 points if the day in the purchase date is odd.
    if data['purchaseDate'][-1] in "13579":
        points += 6
    
        
    print(points)
    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    if data['purchaseTime'][0:2] == "14" or data['purchaseTime'][0:2] == "15" or data['purchaseTime']== "16:00":
        points += 10
    
    
    return points