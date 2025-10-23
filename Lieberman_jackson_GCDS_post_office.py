'''
Author:Jackson Lieberman
Sources:Mr. Campbell
Discription: Determines the price to ship a given peice of postage based off its dimentions and distance traveled
Challenges: 
Date:10/19
Bugs:
'''

def data_parse(data):
    '''
    Parses given data into variables for each value
    Args:
        data(str): the string of data the function takes in
    Returns:
        l: length of the given postage
        w: width of the given postage
        h: hight or thicknes of the given postage
        start_zip: the zipcode that the postage will start at
        end_zip: the zipcode that the postage is being delivered to
    '''
    data = data.split(', ') #splits data by commas to get a list of each individual peice of data
    #sets each peice of data to a variable and defines the its type
    l = float(data[0])
    w = float(data[1])
    h = float(data[2])
    start_zip = int(data[3])
    end_zip = int(data[4])
    return l , w, h ,start_zip, end_zip # returns each peice of data

    
def zip_zone(zip):
    '''
    calculates zone that a zipcode is in
    Args:
        zip(int): the zip code the piece of postage is being sent from
    Returns:
        zone: the zone that the zipcode is in
    '''
    # if the zip code is between two values 
    if 1 <= zip <= 6999:
    #set the zone variable to the according zone
        zone = 1
    elif 7000 <= zip <= 19999:
        zone = 2
    elif 20000 <= zip <= 35999:
        zone = 3        
    elif 36000 <= zip <= 62999:
        zone = 4
    elif 63000 <= zip <= 84999:
        zone = 5    
    elif 85000 <= zip <= 99999:
        zone = 6
    return zone


def postage_class(l, w, h, travel_dist):
    '''
    Uses the weight, hight and length of a peice of postage to detirmine its class and then price to ship based of the distance it will be traveling
    Args:
        l: length of the given peice of postage
        h: height of the given peice of postage
        w: width of the given peice of postage
        travel_dist: the number of zip codes the given peice of postage will travel
    Returns:
        price: the price of the delivery based off its size and distance that it will be travelling
    '''
    #if the length, width, and hight are within specified parameters 
    if 3.5 <= l <= 4.25 and 3.5 <= w <= 6 and 0.007 <= h <= 0.016: 
    #calcuate the specified price for those dimentions
        price = .20 + (.03*travel_dist)
        return price
    elif 4.25 < l <= 6 and 6 < w <= 11.5 and 0.007 <= h <= 0.015:
        price = .37 + (.03*travel_dist)
        return price
    elif 3.5 <= l <= 6.125 and 5 <= w <= 11.5 and 0.016 < h <= 0.25:
        price = .37 + (.04*travel_dist)
        return price
    elif 6.125 < l <= 24 and 11 < w <= 18 and 0.25 < h <= 0.5:
        price = .60 + (.05*travel_dist)
        return price

    package_sides = l + 2 * (w + h) #calculates the distance around the sides of the peice of postage
    #if either the length, width, or hight exeed certain values the peice of postage is classified as a package
    #packages are catagorized based on their length and distance around their other sides
    if package_sides <= 84: 
        price = 2.95 + (.25*travel_dist)
        return price
    elif 84 < package_sides <= 130:
        price = 3.95 + (.35*travel_dist)
        return price
    else:# if no values are meet then return that the piece of postage is unmailable.
        return 'UNMAILABLE'



def main():    
    '''
    Runs all funtions
    Args:
        none
    '''
    data = input('data:')
    l, w, h, start_zip, end_zip = data_parse(data) #parses the data into 5 individual variables
    travel_dist = abs(zip_zone(start_zip) - zip_zone(end_zip)) #takes the absolute value of the difference between the zipcodes

    price = postage_class(l, w, h, travel_dist) #finds the price

    if price == 'UNMAILABLE':   #fall back if package is unmailable
        print('UNMAILABLE')
    else:
        print(price) 


main()


