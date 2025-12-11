"""
Titanic Dataset Analysis 
Student Name: Jackson Lieberman
Date: _________________


Complete the functions below to analyze the Titanic dataset.
"""

def read_titanic_data(filename):
    """
    Reads the Titanic CSV file and returns the data as a list of lists.
    
    Args:
        filename (str): Path to the CSV file
    
    Returns:
        tuple: (headers, passengers) where headers is a list of column names
               and passengers is a list of lists containing passenger data
    """
    passengers = []
    headers = []
    
    try:
        # open file
        with open(filename, 'r') as titanic:
            counter = 0 # count each line so you can know what number line is being read
            for line in titanic: 
                counter += 1 #add one for each line
                row = line.strip().split(',') #slit the data by commas
                
                if counter == 1:
                    headers = row # Assign the list
                else:
                    # Append the row as a single element to the passengers list.
                    passengers.append(row) 
        
    except FileNotFoundError:
        print(f"Error: {filename} not found!") #fall back if it cant find the file
    
    return headers, passengers


def calculate_basic_stats(headers, passengers):
    """
    Calculates and displays basic statistics about the passengers.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records (each record is a list)
    """
    survived=0
    dead =0

    sex_index = headers.index('Sex') #finds the index of the sex column
    survived_index = headers.index('Survived') #finds the index of the survived column
  
    for line in passengers:
        if line[survived_index] == '1': #if they survived add one to the survived value
            survived += 1
        elif line[survived_index] == '0': #if they survived add one to the survived value
            dead += 1
        if line[sex_index] == 'male':
                male_total += 1
                if line[survived_index] == '1':
                    male_survived += 1
        elif line[sex_index] == 'female':
            female_total += 1
            if line[survived_index] == '1':
                female_survived += 1

    survive_rate = (survived/(survived+dead)) *100  #calculate the survival rate
 
    
    print("Basic survival stats:")
    print(f"Total Passengers: {survived+dead}")
    print(f"Survivors: {survived}")
    print(f"Survival Rate: {survive_rate:.1f}%")
    print()


def write_survivors(headers, passengers, output_file):
    """
    Writes information about all survivors to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    survived_index = headers.index("Survived") #finds the index of the survival column
    ID_index = headers.index('PassengerId') #finds the index of the the passenger ID column
    name_index = headers.index('Name') #finds the index of the names column
    age_index = headers.index('Age') #finds the index of the names column
    class_index = headers.index('Pclass') #finds the index of the class column

    with open(output_file, 'w') as out:  
        # Define the headers for write the new file
        output_headers = ['PassengerId', 'Name', 'Age', 'Class']
        
        out.write(",".join(output_headers) + "\n") #write them and start a new line under
        
        # go through all passengers
        for passenger in passengers:
            # Check if the passenger survived 
            if passenger[survived_index] == '1':
                passenger_id = passenger[ID_index]
                name = passenger[name_index]
                age = passenger[age_index]
                p_class = passenger[class_index]
                #if yes complile thier data
                row_data = [passenger_id, name, age, p_class]

                row_string = ",".join(str(item) for item in row_data)

                # Write the survivor's data to the new file in a single row
                out.write(row_string + "\n")


    print(f"Successfully wrote survivor data to {output_file}")

    # TODO: Write survivor information to file
    # Format: PassengerId,Name,Age,Class
    # Use headers to find the correct indices
    pass


def write_first_class(headers, passengers, output_file):
    """
    Writes information about first-class passengers to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
  
    survived_index = headers.index("Survived") #finds the index of the survival column
    ID_index = headers.index('PassengerId') #finds the index of the the passenger ID column
    name_index = headers.index('Name') #finds the index of the names column
    age_index = headers.index('Age') #finds the index of the names column
    class_index = headers.index('Pclass') #finds the index of the class column


    first_class_passengers = []
    survived_first_class = 0
    total_first_class = 0

    for passenger in passengers:
        # filter first class in the data
        if passenger[class_index] == '1':
            first_class_passengers.append(passenger)
            total_first_class += 1
            if passenger[survived_index] == '1':
                survived_first_class += 1

    # Calculate survival rate
    survival_rate = (survived_first_class / total_first_class) * 100



    with open(output_file, 'w', newline="") as out:
        #  the survival rate and how many survived
        rate_summary = f"First Class Survival Rate: {survival_rate:.1f}% ({survived_first_class} out of {total_first_class})\n\n"
        out.write(rate_summary)

        # Define the headers we want to write to the new file
        output_headers = ['PassengerId', 'Name', 'Age', 'Class', 'Survived']
        out.write(",".join(output_headers) + "\n")

        # go through ONLY the first class passengers by using the list made before
        for passenger in first_class_passengers:
            passenger_id = passenger[ID_index]
            name = passenger[name_index]
            age = passenger[age_index]
            p_class = passenger[class_index]
            survived = passenger[survived_index]
            #write their data
            row_data = [passenger_id, name, age, p_class, survived]
            row_string = ",".join(str(item) for item in row_data)
            out.write(row_string + "\n")

    print(f"Successfully wrote first-class data to {output_file}")
   
    # TODO: Filter first-class passengers and write to file
    # Include survival rate at the top
    pass



def write_children(headers, passengers, output_file):
    """
    Writes information about passengers under 18 to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
      
    survived_index = headers.index("Survived") +1 #finds the index of the survival column
    ID_index = headers.index('PassengerId') +1 #finds the index of the passenger ID column
    name_index = headers.index('Name') +1 #finds the index of the name column
    age_index = headers.index('Age') +1 #finds the index of the age column
    class_index = headers.index('Pclass')+1 #finds the index of the class column
    Sex_index = headers.index('Sex')+1 #finds the index of the gender column
    
    children = []


    for passenger in passengers:
        # sets the age of each passenger to a string
        age_str = passenger[age_index] 
        

        if len(age_str) == 0:
            #fall back if age isnt there
            age_str = 0

        age = float(age_str) #sets the age to a float so we can do inequalities
        if age < 18: #check for children
            children.append(passenger)



    with open(output_file, 'w', newline="") as out:
        # Define the headers we want to write to the new file
        output_headers = ['PassengerId', 'Name', "Sex",'Age', 'Class', 'Survived']
        out.write(",".join(output_headers) + "\n")

        # Iterate through only the children passengers as filtered earlier
        for passenger in children:
            passenger_id = passenger[ID_index]
            name = passenger[name_index]
            sex= passenger[Sex_index]
            p_class = passenger[class_index]
            survived = passenger[survived_index]


            row_data = [passenger_id, name, sex, age, p_class, survived]
            row_string = ",".join(str(item) for item in row_data)
            out.write(row_string + "\n")

    print(f"Successfully wrote first-class data to {output_file}")

    # TODO: Filter passengers under 18 and write to file
    # Remember: some ages might be missing!
    pass


def generate_analysis_report(headers, passengers, output_file):
    """
    Generates a comprehensive analysis report.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """


    survived_index = headers.index("Survived")+1 #finds the index of the survival column
    age_index = headers.index('Age')+1#finds the index of the age column
    class_index = headers.index('Pclass')+1 #finds the index of the Class column
    sex_index = headers.index('Sex') +1 #finds the index of the gender column

    total_passengers = len(passengers) #sets teh total passengers to the length of passengers
    total_survived = 0 
    total_age_sum = 0
    age_count = 0


    for passenger in passengers: #for every passenger calculate their different values
        survived = int(passenger[survived_index])
        p_class = passenger[class_index]
        sex = passenger[sex_index]
        age = passenger[age_index]

        total_survived += survived

        # Calculate average age
        if age:
            total_age_sum += float(age)
            age_count += 1
            
        # count by class
        [p_class]['total'] += 1

        # Count by Gender
        [sex]['total'] += 1
        [sex]['survived'] += survived


            
    average_age = total_age_sum / age_count
 
    survival_rate = (total_survived / total_passengers) * 100 

    # Generate the report string
    report_content = f"analysis report\n"
    report_content += f"Total Passengers Analyzed: {total_passengers}\n"
    report_content += f"Total Survivors: {total_survived}\n"
    report_content += f"Overall Survival Rate: {survival_rate:.2f}%\n"
    report_content += f"Average Age (Excluding missing data): {average_age:.2f}\n"
    report_content += f"Survival Rates by Passenger Class\n"

    with open(output_file, 'w') as out:
        out.write(report_content)

    print(f"Successfully generated analysis report to {output_file}")

    # TODO: Calculate survival rates by class and gender
    # TODO: Calculate average ages
    # TODO: Write formatted report to file
    pass


def main():
    """
    Main function to run the analysis.
    """
    # Read the data
    print("Reading Titanic data...")
    headers, passengers = read_titanic_data("titanic.csv")
    
    if not passengers:
        print("Failed to load data. Exiting.")
        return
    
    print(f"Loaded {len(passengers)} passenger records.\n")
    
    # Part 1: Basic Statistics
    calculate_basic_stats(headers, passengers)
    
    # Part 2: Filter and Write Data
    print("Generating output files...")
    write_survivors(headers, passengers, "survivors.txt")
    write_first_class(headers, passengers, "first_class.txt")
    write_children(headers, passengers, "children.txt")
    
    # Part 3: Analysis Report
    #generate_analysis_report(headers, passengers, "analysis_report.txt")
    
    print("Analysis complete! Check the output files.")


# Run the program
if __name__ == "__main__":
    main()





"""
GCDS CS: Titanic Dataset Analysis 
Student Name: Jackson Lieberman
Date: _________________


Complete the functions below to analyze the Titanic dataset.
"""

def read_titanic_data(filename):
    """
    Reads the Titanic CSV file and returns the data as a list of lists.
    
    Args:
        filename (str): Path to the CSV file
    
    Returns:
        tuple: (headers, passengers) where headers is a list of column names
               and passengers is a list of lists containing passenger data

    CHALLENGE GOALS:
    ----------------
    GOAL 1 (Beginner): Load and Display Data
    - Load the titanic.csv file.
    - Print the column names and the total number of passengers after reading.
    """
    passengers = []
    headers = []
    
    try:
        # open file
        with open(filename, 'r') as titanic:
            counter = 0 # count each line so you can know what number line is being read
            for line in titanic: 
                counter += 1 #add one for each line
                row = line.strip().split(',') #slit the data by commas
                
                if counter == 1:
                    headers = row # Assign the list
                else:
                    # Append the row as a single element to the passengers list.
                    passengers.append(row) 
        
        # --- GOAL 1 Implementation Step (Display Stats) ---
        print("--- Data Loading Complete (Goal 1) ---")
        print(f"Column Names: {headers}")
        print(f"Total Passengers Loaded: {len(passengers)}\n")
        
    except FileNotFoundError:
        print(f"Error: {filename} not found!") #fall back if it cant find the file
    
    return headers, passengers


def calculate_basic_stats(headers, passengers):
    """
    Calculates and displays basic statistics about the passengers.

    CHALLENGE GOALS:
    ----------------
    GOAL 2 (Beginner): Calculate Survival Rate
    - Calculate and print the overall survival rate (percentage of passengers who survived).

    GOAL 3 (Intermediate): Survival by Gender
    - Calculate the survival rate for males and females separately.
    - Display which gender had a higher survival rate.
    
    BONUS CHALLENGES:
    -----------------
    - Analyze survival rates by port of embarkation.
    - Investigate if cabin location affected survival.
    """
    survived=0
    dead =0
    male_survived = 0
    male_total = 0
    female_survived = 0
    female_total = 0

    survived_index = headers.index('Survived') #finds the index of the survived column
    sex_index = headers.index('Sex') # Added for Goal 3

    for line in passengers:
        is_survived = line[survived_index] == '1'
        if is_survived:
            survived += 1
        elif line[survived_index] == '0':
            dead += 1
        
        # --- GOAL 3 Implementation Steps ---
        if line[sex_index] == 'male':
            male_total += 1
            if is_survived:
                male_survived += 1
        elif line[sex_index] == 'female':
            female_total += 1
            if is_survived:
                female_survived += 1

    survive_rate = (survived/(survived+dead)) *100  #calculate the survival rate
    male_survival_rate = (male_survived / male_total) * 100 if male_total else 0
    female_survival_rate = (female_survived / female_total) * 100 if female_total else 0
 
    print("--- Basic Survival Stats (Goal 2) ---")
    print(f"Total Passengers: {survived+dead}")
    print(f"Survivors: {survived}")
    print(f"Survival Rate: {survive_rate:.1f}%")
    print()

    print("--- Survival by Gender Stats (Goal 3) ---")
    print(f"Male Survival Rate: {male_survival_rate:.1f}% ({male_survived}/{male_total})")
    print(f"Female Survival Rate: {female_survival_rate:.1f}% ({female_survived}/{female_total})")
    if male_survival_rate > female_survival_rate:
        print(f"Males had a higher survival rate.")
    else:
        print(f"Females had a higher survival rate.")
    print()


def calculate_age_statistics(headers, passengers):
    """
    Calculates and displays age statistics about the passengers.

    CHALLENGE GOALS:
    ----------------
    GOAL 4 (Intermediate): Age Analysis
    - Find and print the average age of all passengers.
    - Find and print the average age of survivors vs non-survivors.
    - Find and print the youngest and oldest passengers.
    """
    ages = []
    survivor_ages = []
    non_survivor_ages = []
    
    age_index = headers.index('Age')
    survived_index = headers.index('Survived')

    for passenger in passengers:
        try:
            age = float(passenger[age_index])
            ages.append(age)
            if passenger[survived_index] == '1':
                survivor_ages.append(age)
            else:
                non_survivor_ages.append(age)
        except ValueError:
            # Skips passengers with missing age data for this calculation
            continue 

    if not ages:
        print("No age data available for analysis.")
        return

    avg_age_total = sum(ages) / len(ages)
    avg_age_survivors = sum(survivor_ages) / len(survivor_ages) if survivor_ages else 0
    avg_age_non_survivors = sum(non_survivor_ages) / len(non_survivor_ages) if non_survivor_ages else 0
    youngest = min(ages)
    oldest = max(ages)

    print("--- Age Analysis (Goal 4) ---")
    print(f"Average Age of all passengers: {avg_age_total:.1f}")
    print(f"Average Age of Survivors: {avg_age_survivors:.1f}")
    print(f"Average Age of Non-Survivors: {avg_age_non_survivors:.1f}")
    print(f"Youngest Passenger Age: {youngest}")
    print(f"Oldest Passenger Age: {oldest}")
    print()


def calculate_class_statistics(headers, passengers):
    """
    Analyzes survival and fares based on passenger class.

    CHALLENGE GOALS:
    ----------------
    GOAL 5 (Intermediate): Class-Based Analysis
    - For each passenger class (1st, 2nd, 3rd):
        - Calculate the survival rate
        - Calculate the average fare paid
    - Create a summary showing which class had the best survival chances.
    """
    pclass_index = headers.index('Pclass')
    survived_index = headers.index('Survived')
    fare_index = headers.index('Fare')

    class_data = {
        '1': {'total': 0, 'survived': 0, 'fares': []},
        '2': {'total': 0, 'survived': 0, 'fares': []},
        '3': {'total': 0, 'survived': 0, 'fares': []},
    }

    for passenger in passengers:
        pclass = passenger[pclass_index]
        if pclass in class_data:
            class_data[pclass]['total'] += 1
            try:
                fare = float(passenger[fare_index])
                class_data[pclass]['fares'].append(fare)
            except ValueError:
                pass # Handle missing fares
            
            if passenger[survived_index] == '1':
                class_data[pclass]['survived'] += 1
    
    print("--- Class-Based Analysis (Goal 5) ---")
    best_survival_rate = -1
    best_class = ''
    for pclass, data in class_data.items():
        total = data['total']
        survived = data['survived']
        avg_fare = sum(data['fares']) / len(data['fares']) if data['fares'] else 0
        survival_rate = (survived / total) * 100 if total else 0

        print(f"Class {pclass}:")
        print(f"  Total Passengers: {total}, Survivors: {survived}")
        print(f"  Survival Rate: {survival_rate:.1f}%")
        print(f"  Average Fare: ${avg_fare:.2f}")

        if survival_rate > best_survival_rate:
            best_survival_rate = survival_rate
            best_class = pclass
    
    print(f"\nSummary: Class {best_class} had the best survival chances with a rate of {best_survival_rate:.1f}%")
    print()


def write_survivors(headers, passengers, output_file):
    """
    Writes information about all survivors to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    survived_index = headers.index("Survived") #finds the index of the survival column
    ID_index = headers.index('PassengerId') #finds the index of the the passenger ID column
    name_index = headers.index('Name') #finds the index of the names column
    age_index = headers.index('Age') #finds the index of the names column
    class_index = headers.index('Pclass') #finds the index of the class column

    with open(output_file, 'w') as out:  
        # Define the headers for write the new file
        output_headers = ['PassengerId', 'Name', 'Age', 'Class']
        
        out.write(",".join(output_headers) + "\n") #write them and start a new line under
        
        # go through all passengers
        for passenger in passengers:
            # Check if the passenger survived 
            if passenger[survived_index] == '1':
                passenger_id = passenger[ID_index]
                name = passenger[name_index]
                age = passenger[age_index]
                p_class = passenger[class_index]
                #if yes complile thier data
                row_data = [passenger_id, name, age, p_class]

                row_string = ",".join(str(item) for item in row_data)

                # Write the survivor's data to the new file in a single row
                out.write(row_string + "\n")


    print(f"Successfully wrote survivor data to {output_file}")


def write_first_class(headers, passengers, output_file):
    """
    Writes information about first-class passengers to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file

    CHALLENGE GOALS:
    ----------------
    GOAL 5 (Intermediate Implementation Detail): 
    - This function implements specific logic to calculate and write survival rates for a single class.
    """
  
    survived_index = headers.index("Survived") #finds the index of the survival column
    ID_index = headers.index('PassengerId') #finds the index of the the passenger ID column
    name_index = headers.index('Name') #finds the index of the names column
    age_index = headers.index('Age') #finds the index of the names column
    class_index = headers.index('Pclass') #finds the index of the class column


    first_class_passengers = []
    survived_first_class = 0
    total_first_class = 0

    for passenger in passengers:
        # filter first class in the data
        if passenger[class_index] == '1':
            first_class_passengers.append(passenger)
            total_first_class += 1
            if passenger[survived_index] == '1':
                survived_first_class += 1

    # Calculate survival rate
    survival_rate = (survived_first_class / total_first_class) * 100



    with open(output_file, 'w', newline="") as out:
        #  the survival rate and how many survived
        rate_summary = f"First Class Survival Rate: {survival_rate:.1f}% ({survived_first_class} out of {total_first_class})\n\n"
        out.write(rate_summary)

        # Define the headers we want to write to the new file
        output_headers = ['PassengerId', 'Name', 'Age', 'Class', 'Survived']
        out.write(",".join(output_headers) + "\n")

        # go through ONLY the first class passengers by using the list made before
        for passenger in first_class_passengers:
            passenger_id = passenger[ID_index]
            name = passenger[name_index]
            age = passenger[age_index]
            p_class = passenger[class_index]
            survived = passenger[survived_index]
            #write their data
            row_data = [passenger_id, name, age, p_class, survived]
            row_string = ",".join(str(item) for item in row_data)
            out.write(row_string + "\n")

    print(f"Successfully wrote first-class data to {output_file}")
   
    # TODO: Filter first-class passengers and write to file
    # Include survival rate at the top


def write_children(headers, passengers, output_file):
    """
    Writes information about passengers under 18 to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file

    CHALLENGE GOALS:
    ----------------
    GOAL 8 (Challenge Implementation Detail): 
    - This function assists in breaking down data by age group (children <18).
    """
      
    # NOTE: I fixed the index retrieval below. You were adding +1 to the index,
    # but list indices in Python start at 0, so headers.index() already returns the correct integer index.
    survived_index = headers.index("Survived") 
    ID_index = headers.index('PassengerId') 
    name_index = headers.index('Name')
    age_index = headers.index('Age')
    class_index = headers.index('Pclass')
    Sex_index = headers.index('Sex')
    
    children = []


    for passenger in passengers:
        # sets the age of each passenger to a string
        age_str = passenger[age_index] 
        

        if len(age_str) == 0:
            #fall back if age isnt there
            continue # Skip children analysis for passengers with missing age

        age = float(age_str) #sets the age to a float so we can do inequalities
        if age < 18: #check for children
            children.append(passenger)



    with open(output_file, 'w', newline="") as out:
        # Define the headers we want to write to the new file
        output_headers = ['PassengerId', 'Name', "Sex",'Age', 'Class', 'Survived']
        out.write(",".join(output_headers) + "\n")

        # Iterate through only the children passengers as filtered earlier
        for passenger in children:
            passenger_id = passenger[ID_index]
            name = passenger[name_index]
            sex = passenger[Sex_index] # Added Sex index variable
            age = passenger[age_index]
            p_class = passenger[class_index]
            survived = passenger[survived_index] # Added Survived index variable
            
            # Write the data row
            row_data = [passenger_id, name, sex, age, p_class, survived]
            row_string = ",".join(str(item) for item in row_data)
            out.write(row_string + "\n")
            
    print(f"Successfully wrote children data to {output_file}")