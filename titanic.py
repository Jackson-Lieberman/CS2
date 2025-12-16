"""
Titanic Dataset Analysis 
Student Name: Jackson Lieberman
Date: _________________
Bonuses:
Bugs:
Log: 


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
            counter = 0                                                                 # count each line so you can know what number line is being read
            for line in titanic: 
                counter += 1                                                            #add one for each line
                row = line.strip().split(',')                                           #slit the data by commas
                
                if counter == 1:
                    headers = row                                                       # Assign the list
                else:
                                                                                        # Append the row as a single element to the passengers list.
                    passengers.append(row) 
        
    except FileNotFoundError:
        print(f"Error: {filename} not found!")                                          #fall back if it cant find the file
    
    return headers, passengers


def calculate_basic_stats(headers, passengers):
    """
    Calculates and displays basic statistics about the passengers.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records (each record is a list)
    """
    male_survived=0
    male_total =0
    female_survived=0
    female_total=0

    sex_index = headers.index('Sex')+1                                                  #finds the index of the sex column
    survived_index = headers.index('Survived')+1                                        #finds the index of the survived column
  
    for line in passengers:                                                             #for every line
        if line[sex_index] == 'male':                                                   #check if the passenger is male
                male_total += 1                                                         #if they are add one to the total males
                if line[survived_index] == '1':                                         #if they survived add one to the survived value
                    male_survived += 1
        elif line[sex_index] == 'female':                                               #check if female
            female_total += 1   
            if line[survived_index] == '1':                                             #if they survived add one
                female_survived += 1 

    survive_rate = ((male_survived+female_survived)/(female_total+male_total)) *100     #calculate the survival rate
    female_survival_rate = (female_survived / female_total) * 100                       #calculates female survival rate
    male_survival_rate = (male_survived / male_total) * 100                             #calculates  male survival rate
    
    print("Basic survival stats:")
    print(f"Total Passengers: {male_total+female_total}")
    print(f"Survivors: {male_survived+female_survived}")
    print(f"Survival Rate: {survive_rate:.1f}%")
   
    print(f"Male Survival Rate: {male_survival_rate:.1f}% ({male_survived}/{male_total})")
    print(f"Female Survival Rate: {female_survival_rate:.1f}% ({female_survived}/{female_total})")
    if male_survival_rate > female_survival_rate:
        print(f"Males had a higher survival rate.")
    else:
        print(f"Females had a higher survival rate.")


def write_survivors(headers, passengers, output_file):
    """
    Writes information about all survivors to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    survived_index = headers.index("Survived")                                          #finds the index of the survival column
    ID_index = headers.index('PassengerId')                                             #finds the index of the the passenger ID column
    name_index = headers.index('Name')                                                  #finds the index of the names column
    age_index = headers.index('Age')                                                    #finds the index of the names column
    class_index = headers.index('Pclass')                                               #finds the index of the class column

    

    with open(output_file, 'w') as out:  
                                                                                        # Define the headers for write the new file
        output_headers = ['PassengerId', 'Name', 'Age', 'Class']
        
        out.write(",".join(output_headers) + "\n")                                      #write them and start a new line under
        
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
    """
  
    survived_index = headers.index("Survived")                                          #finds the index of the survival column
    ID_index = headers.index('PassengerId')                                             #finds the index of the the passenger ID column
    name_index = headers.index('Name')                                                  #finds the index of the names column
    age_index = headers.index('Age')                                                    #finds the index of the names column
    class_index = headers.index('Pclass')                                               #finds the index of the class column


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
   
    




def calculate_age_statistics(headers, passengers):
    """
    Calculates and displays age statistics about the passengers.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    ages = []
    survivor_ages = []
    dead_ages = []
    
    age_index = headers.index('Age')+1                                                  #finds the index of the age column
    survived_index = headers.index('Survived')+1                                        #finds the index of the survived column
    
    for passenger in passengers:
                                                                                        # sets the age of each passenger to a string
        age_str = passenger[age_index] 
        
        if len(age_str) == 0:
                                                                                        #fall back if age isnt there
            age_str = 0

        age = float(age_str)                                                            #set the passenger ages to a float for data analysis
        ages.append(age)
        if passenger[survived_index] == '1':                                            #if the person survived add their age the to survived ages list
            survivor_ages.append(age)
        else:
            dead_ages.append(age)


    avg_age_total = sum(ages) / len(ages)                                               #calculate avg age
    avg_age_survivors = sum(survivor_ages) / len(survivor_ages)                         #calculate avg age of survivors
    avg_age_non_survivors = sum(dead_ages) / len(dead_ages)                             #calculate avg age of dead
    youngest = min(ages)                                                                #calculate highest
    oldest = max(ages)                                                                  #calculate lowest

    print("Age Analysis")
    print(f"Average Age of all passengers: {avg_age_total:.1f}")
    print(f"Average Age of Survivors: {avg_age_survivors:.1f}")
    print(f"Average Age of Non-Survivors: {avg_age_non_survivors:.1f}")
    print(f"Youngest Passenger Age: {youngest}")
    print(f"Oldest Passenger Age: {oldest}")
    print()


def family_analysis(headers, passengers):
    """
    Create a new column called 'FamilySize' (SibSp + Parch + 1).
    Analyze survival rates based on family size.
    Determine if traveling alone or with family improved survival chances.

    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
    """

    headers.append('FamilySize')                                                        #adds a new header for new column

    sibsp_index = headers.index('SibSp')+1                                              #finds the index of the sibsp column
    parch_index = headers.index('Parch')                                                #finds the index of the parch column
    survived_index = headers.index('Survived')                                          #finds the index of the survived column

    for passenger in passengers:
                                                                                        # Convert SibSp and Parch to integers and calculate FamilySize
        sibsp = int(passenger[sibsp_index])
        parch = int(passenger[parch_index])
        family_size = sibsp + parch + 1                                                 #adds one for the passenger
                                                                                        # to the passenger's data list
        passenger.append(str(family_size))

    print("\n Family Survival Patterns Analysis")

                                                                                        # Dictionary to store totals and survivors for each family size
    family_stats = {}

    for passenger in passengers:
        if passenger[-1] != 'N/A':                                                      # Use the added FamilySize value
            size = int(passenger[-1])
            survived = int(passenger[survived_index])

            if size not in family_stats:
                family_stats[size] = [0, 0]                                             # Initialize for size

            family_stats[size][0] += 1                                                  #total
            family_stats[size][1] += survived                                           #survivors if survived == 1

    print("\nSurvival Rates by Family Size:")
    for size in sorted(family_stats.keys()):
        total = family_stats[size][0]
        survivors_count = family_stats[size][1]
        if total > 0:
            rate = (survivors_count / total) * 100
            print(f"Family Size {size}: {rate:.1f}% survival rate ({survivors_count}/{total})")


    alone_total = family_stats.get(1, [0, 0])[0]                                        #if the person is alone their size will only be one, then check if survived
    alone_survived = family_stats.get(1, [0, 0])[1]  
    alone_rate = (alone_survived / alone_total) * 100                                   #calculate the rate


    family_travelers_total = 0
    family_travelers_survived = 0

    for size, (total, survived) in family_stats.items():
        if size > 1:                                                                    #adds the number of travelers and survivers to their variables
            family_travelers_total += total
            family_travelers_survived += survived

    family_rate = (family_travelers_survived / family_travelers_total) * 100 

    print("\nSummary: Traveling Alone vs. With Family:")
    print(f"Traveling Alone (Size 1): {alone_rate:.1f}% survival rate")
    print(f"Traveling With Family (Size > 1): {family_rate:.1f}% survival rate")

    if family_rate > alone_rate:
        print("Conclusion: Traveling with family improved survival chances compared to traveling alone.")
    elif alone_rate > family_rate:
        print("Conclusion: Traveling alone improved survival chances compared to traveling with family.")
    else:
        print("Conclusion: Survival chances were roughly equal.")


def class_analysis(headers, passengers):
    '''
    For each passenger class (1st, 2nd, 3rd):
    - Calculate the survival rate
    - Calculate the average fare paid
    Creates a summary showing which class had the best survival chances.
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    '''
                                                                                        #makes a dictionaty for each class
    class_data = {
        '1': {'total': 0, 'survived': 0, 'fares': []},
        '2': {'total': 0, 'survived': 0, 'fares': []},
        '3': {'total': 0, 'survived': 0, 'fares': []},
    }

    pclass_index = headers.index('Pclass')
    survived_index = headers.index('Survived')
    fare_index = headers.index('Fare')+1

    for passenger in passengers:
        pclass = passenger[pclass_index]                                                #finds the class
        class_data[pclass]['total'] += 1                                                #adds one to related class of the passenger
        if passenger[survived_index] == '1':                                            #adds one to the survival value if the passenger survived
            class_data[pclass]['survived'] += 1
        fare_value = float(passenger[fare_index])                                       #converts their fare to a float so we can do math with it
        class_data[pclass]['fares'].append(fare_value)                                  #adds the fare to the fare value


    print("\n Class Analysis Summary")
    best_class = None                                                                   #initalizes the best class
    best_rate = -1 

    sorted_data = sorted(class_data.items())                                            #sorts the data
    for pclass, data in sorted_data:                                                    #for every class
        total = data['total']                                                           #finds each value 
        survived = data['survived']
        fares = data['fares']
        
        
        survival_rate = (survived / total) * 100                                        # Calculate survival rate for the class
        
        average_fare = sum(fares) / len(fares)                                          #calculate avg fares
        
        print(f"\nPassenger Class {pclass}:")
        print(f"Survival Rate: {survival_rate:.1f}% ({survived}/{total})")
        print(f"Average Fare: ${average_fare:.2f}")
        

        if survival_rate > best_rate:                                                   #for each class it will check if the survival is higher than the last
            best_rate = survival_rate
            best_class = pclass

    

    print(f"\nSummary: Class {best_class} had the best survival chances with a rate of {best_rate:.1f}%.")




def write_children(headers, passengers, output_file):
    """
    Writes information about passengers under 18 to a file.
    
    Args:   
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
      
    survived_index = headers.index("Survived") +1                                       #finds the index of the survival column
    ID_index = headers.index('PassengerId') +1                                          #finds the index of the passenger ID column
    name_index = headers.index('Name') +1                                               #finds the index of the name column
    age_index = headers.index('Age') +1                                                 #finds the index of the age column
    class_index = headers.index('Pclass')+1                                             #finds the index of the class column
    Sex_index = headers.index('Sex')+1                                                  #finds the index of the gender column
    
    children = []


    for passenger in passengers:
                                                                                        # sets the age of each passenger to a string
        age_str = passenger[age_index] 
        

        if len(age_str) == 0:
                                                                                        #fall back if age isnt there
            age_str = 0

        age = float(age_str)                                                            #sets the age to a float so we can do inequalities
        if age < 18:                                                                    #check for children
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

    

def generate_analysis_report(headers, passengers, output_file):
    """
    Generates a comprehensive analysis report.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """


    survived_index = headers.index("Survived")+1                                        #finds the index of the survival column
    age_index = headers.index('Age')+1                                                  #finds the index of the age column
    class_index = headers.index('Pclass')+1                                             #finds the index of the Class column
    sex_index = headers.index('Sex') +1                                                 #finds the index of the gender column

    total_passengers = len(passengers)                                                  #sets teh total passengers to the length of passengers
    total_survived = 0 
    total_age_sum = 0
    age_count = 0


    for passenger in passengers:                                                        #for every passenger calculate their different values
        survived = int(passenger[survived_index])
        age = passenger[age_index]

        total_survived += survived 
        
        if len(age) == 0:
                                                                                        #fall back if age isnt there
            age = 0
        
        total_age_sum += float(age)                                                     #adds the age to the totalsum of ages
        age_count += 1
        
                                                                                        # Calculate average age by adding all ages and diving by the number of ages
    average_age = total_age_sum / age_count
 
    survival_rate = (total_survived / total_passengers) * 100 

                                                                                        # Generate the report string
    report_content = f'''analysis report\n
    Total Passengers Analyzed: {total_passengers}\n
    Total Survivors: {total_survived}\n
    Overall Survival Rate: {survival_rate:.2f}%\n
    Average Age: {average_age:.2f}\n
    Survival Rates by Passenger Class'''

    with open(output_file, 'w') as out:
        out.write(report_content)

    print(f"Successfully generated analysis report to {output_file}")

    
    





def main():
    """
    Interactive menu for Titanic data analysis.
    """
    print("Reading Titanic data...")
    headers, passengers = read_titanic_data("titanic.csv")
    
    if not passengers:
        print("Failed to load data. Exiting.")
        return
    
    print(f"Loaded {len(passengers)} passenger records.")

    while True:
        print("Titanic Analysis Menu")
        print("1. View Basic Statistics")
        print("2. View Age Statistics")
        print("3. View Class Analysis")
        print("4. View Family Analysis")
        print("5. Generate All Output Files & Full Report")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ")

        if choice == '1':
            calculate_basic_stats(headers, passengers)
        elif choice == '2':
            calculate_age_statistics(headers, passengers)
        elif choice == '3':
            class_analysis(headers, passengers)
        elif choice == '4':
            family_analysis(headers, passengers)
        elif choice == '5':
            print("Generating output files...")
            write_survivors(headers, passengers, "survivors.txt")
            write_first_class(headers, passengers, "first_class.txt")
            write_children(headers, passengers, "children.txt")
            generate_analysis_report(headers, passengers, "analysis_report.txt")
            print("Files generated: survivors.txt, first_class.txt, children.txt, analysis_report.txt")
        elif choice == '6':
            print("Exiting analysis.")
            break
        else:
            print("Invalid selection. Please try again.")

# Run the program
if __name__ == "__main__":
    main()


