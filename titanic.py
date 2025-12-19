"""
Titanic Dataset Analysis 
Student Name: Jackson Lieberman
Date: 12/18/25
Bonuses:
Bugs:
Log: 1.0

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
    survived_index = headers.index('Survived')                                          #finds the index of the survived column
  
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
    
    headers.append('FamilySize')
    age_index = headers.index('Age')+1                                                  #finds the index of the age column
    survived_index = headers.index('Survived')                                          #finds the index of the survived column
    
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

    
    sibsp_index = headers.index('SibSp')+1                                                #sibsp index
    parch_index = headers.index('Parch')+1                                                #parch index
    survived_index = headers.index('Survived')                                          #survived index

   
    if 'FamilySize' not in headers:                                                     #only will add the family size header if its not there
        headers.append('FamilySize')
        family_index = headers.index('FamilySize')+1                                      # set it to the last index
        
        for passenger in passengers:
            sibsp = int(passenger[sibsp_index])
            parch = int(passenger[parch_index])
                                                                                        # Append the calculation to the passenger list
            passenger.append(str(sibsp + parch + 1))
    else:
        family_index = headers.index('FamilySize')

    print("\n Family Survival Patterns Analysis")

                                                                                        # Dictionary to store totals and survivors for each family size
    family_stats = {}

    for passenger in passengers:
        if passenger[family_index] != 'N/A':                                                      # Use the added FamilySize value
            size = int(passenger[family_index])
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
        print("Conclusion: Survival chances were equal.")


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
    Generates a comprehensive survival analysis report:
    Overall stats
    Breakdown by gender, class, age group
    Makes a most likely to survie profile
    Handles missing ages (Unknown, excluded from average age)
    Saves report to a text file
    Args:   
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """

                                                                                            # Column indices
    survived_index = headers.index("Survived")
    sex_index = headers.index("Sex")+1
    pclass_index = headers.index("Pclass")
    age_index = headers.index("Age")+1

                                                                                            # initalize variables
    total = 0
    survivors = 0

                                                                                            # Avg age 
    age_sum = 0.0

                                                                                            # Gender counters: female, male and if they survived

    g_total_f = 0
    g_surv_f = 0
    g_total_m = 0
    g_surv_m = 0

                                                                                            # Class totals/survivors
    c1_total = c1_surv = 0
    c2_total = c2_surv = 0
    c3_total = c3_surv = 0

                                                                                            # Age group totals/survivors: child, adult, senior
    child_total = child_surv = 0
    adult_total = adult_surv = 0
    senior_total = senior_surv = 0

    for passenger in passengers:
            total += 1

            survived = int(passenger[survived_index])
            survivors += survived

            sex = str(passenger[sex_index]).strip().lower()
            clas = int(passenger[pclass_index])  # 1,2,3

            age_str = str(passenger[age_index]).strip()
            if age_str == "":
                age_value = 0
            else:
                age_value = float(age_str)

            age_sum += age_value

            # Age groups
            if age_value < 18:
                child_total += 1
                child_surv += survived
            elif age_value <= 60:
                adult_total += 1
                adult_surv += survived
            else:
                senior_total += 1
                senior_surv += survived

            # Class totals
            if clas == 1:
                c1_total += 1
                c1_surv += survived
            elif clas == 2:
                c2_total += 1
                c2_surv += survived
            else:
                c3_total += 1
                c3_surv += survived

            # Gender totals
            if sex == "female":
                g_total_f += 1
                g_surv_f += survived
            elif sex == "male":
                g_total_m += 1
                g_surv_m += survived

    survival_rate = (survivors / total) * 100
    avg_age = (age_sum / total)  

                                                                                           
                                                                                            #calculate survival rates for each characteristic
    
    c1_survival_rate = (c1_surv / c1_total) * 100                                              
    c2_survival_rate = (c2_surv / c2_total) * 100 
    c3_survival_rate = (c3_surv / c3_total) * 100 
    child_survival_rate = (child_surv/child_total)*100 
    adult_survival_rate = (adult_surv/adult_total)*100 
    senior_survival_rate = (senior_surv/senior_total)*100
    male_survival_rate = (g_surv_m/g_total_m)*100
    female_survival_rate=(g_surv_f/g_total_f)*100
                                                                                            #calcuate the best survival rate for each characteristic
    best_gender= "male" if  male_survival_rate> female_survival_rate else "female"
    best_class = "1" if (c1_survival_rate > c2_survival_rate and c1_survival_rate > c3_survival_rate) else \
             ("2" if c2_survival_rate > c3_survival_rate else "3")
    best_age_group = "Child (<18)" if (child_survival_rate > adult_survival_rate and child_survival_rate > senior_survival_rate) else \
                 ("Adult (18-60)" if adult_survival_rate > senior_survival_rate else "Senior (>60)")


    report = ""
    report += "titanic survival report\n"

    report += "totals\n"
    report += f"Total Passengers: {total}\n"
    report += f"Survivors: {survivors}\n"
    report += f"Survival Rate: {survival_rate:.1f}%\n"
    report += f"Average Age (missing ages counted as 0): {avg_age:.2f}\n\n"

    report += "breakdown by gender\n"
    report += f"female: {(g_surv_f/g_total_f)*100:.1f}% ({g_surv_f}/{g_total_f})\n" 
    report += f"male:   {(g_surv_m/g_total_m)*100:.1f}% ({g_surv_m}/{g_total_m})\n\n" 

    report += "Breakdwon by calss\n"
    report += f"Class 1: {(c1_surv/c1_total)*100:.1f}% ({c1_surv}/{c1_total})\n" 
    report += f"Class 2: {(c2_surv/c2_total)*100:.1f}% ({c2_surv}/{c2_total})\n" 
    report += f"Class 3: {(c3_surv/c3_total)*100:.1f}% ({c3_surv}/{c3_total})\n\n"

    report += "Breakdown by age group\n"
    report += f"Child (<18):   {(child_surv/child_total)*100:.1f}% ({child_surv}/{child_total})\n" 
    report += f"Adult (18-60): {(adult_surv/adult_total)*100:.1f}% ({adult_surv}/{adult_total})\n"
    report += f"Senior (>60):  {(senior_surv/senior_total)*100:.1f}% ({senior_surv}/{senior_total})\n\n" 

    report += "BEST PROFILE TO BOOST CHANCES OF SURVIVAL\n"
    report += f"A {best_gender} in class {best_class} who was a {best_age_group}!\n"
    


    with open(output_file, "w") as out:
        out.write(report)

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
        print("5. Generate Full Report")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ")

        if choice == '1':
            calculate_basic_stats(headers, passengers)
            write_survivors(headers, passengers, "survivors.txt")
        elif choice == '2':
            calculate_age_statistics(headers, passengers)
            write_children(headers, passengers, "children.txt")
        elif choice == '3':
            class_analysis(headers, passengers)
            write_first_class(headers, passengers, "first_class.txt")
        elif choice == '4':
            family_analysis(headers, passengers)
        elif choice == '5':
            print("Generating output file...")
            generate_analysis_report(headers, passengers, "analysis_report.txt")
        elif choice == '6':
            print("Exiting analysis.")
            break
        else:
            print("Invalid selection. Please try again.")

# Run the program
if __name__ == "__main__":
    main()


