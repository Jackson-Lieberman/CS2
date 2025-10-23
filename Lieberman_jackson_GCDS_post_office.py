'''
Author:Jackson Lieberman
Sources:Mr. Campbell, https://stackoverflow.com/questions/41585078/how-do-i-read-and-write-csv-files, https://stackoverflow.com/questions/10303797/print-floating-point-values-without-leading-zero
Description: Determines the price to ship a given peice of postage based off its dimentions and distance traveled
Challenges: Takes the data in a CSV
Date:10/
Bugs: doesnt give like .80 gives .8 instead
'''
import csv


def open_file(filepath):
    '''
    Opens a CSV file for reading.
    Args:
        filepath (str): path to the CSV file
    Returns:
        f (file object): the file with data
        reader (csv.reader): CSV reader over the file
    '''
    file = open(filepath, mode='r', newline='')
    data = csv.reader(file)
    return data

def read_file(reader):
    '''
    Iterates over rows from a CSV reader
    Args:
        reader (csv.reader): CSV reader
    Returns:
        l: length of the given postage
        w: width of the given postage
        h: hight or thicknes of the given postage
        start_zip: the zipcode that the postage will start at
        end_zip: the zipcode that the postage is being delivered to
    '''
    first_row_peeked = False #variable for if the code has checked for a header
    for row in reader:
        # blank lines
        if not row or all(c.strip() == '' for c in row):    
            continue

        # if there is a header than skip that row
        if not first_row_peeked: #if the first row hasnt been checked
            first_row_peeked = True
            try: #try and if you cant make the data a float you know its a header because there must be a string
                float(row[0])
            except ValueError:
                
                continue

    
        l = float(row[0])
        w = float(row[1])
        h = float(row[2])
        start_zip = int(row[3])
        end_zip = int(row[4])
        return l, w, h, start_zip, end_zip

    
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
    Runs all functions
    Args:
        none
    '''
    
    data = open_file(r'C:\Users\jlieberman27\Desktop\CS2\Postage_data.csv')
    while True:
        try: #tries to run the code
            l, w, h, start_zip, end_zip = read_file(data) #parses the data into 5 individual variables
            travel_dist = abs(zip_zone(start_zip) - zip_zone(end_zip)) #takes the absolute value of the difference between the zipcodes

            price = str(postage_class(l, w, h, travel_dist)).lstrip('0') #finds the price and makes it a string so it can strip leading zeros

            if price == 'UNMAILABLE':   #fall back if package is unmailable
                print('UNMAILABLE')
            else:
                print(price)
        except TypeError: #if the code cant run then break due to blank lines then stop the code
            break


main()

