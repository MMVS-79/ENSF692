# calgary_dogs.py
# Manuja Senanayake
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.
import pandas as pd

def  data_frame_creation(file_path='CalgaryDogBreeds.xlsx'):
    """
    Data frame creation / loading data from an Excel file.

    Parameters:
        file_path (str): The path to the Excel file containing the dog breed data.
    
    Returns:
        df (pd.DataFrame): The pandas dataframe
    
    """
    try:
        # Stage 1: DataFrame Creation
        df = pd.read_excel(file_path)
        # Convert 'Breeds' column to uppercase for case-insensitive matching later
        df['Breed'] = df['Breed'].str.upper()
        # Set 'Breeds' and 'Year' as a multi-index for efficient lookup
        df = df.set_index(['Breed', 'Year'])
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()
    except Exception as e:
        print(f"An error occurred during data loading: {e}")
        exit()

def user_input(dataframe):
    """
    Prompts the user to enter a dog breed and validates the input against the DataFrame's
    'Breed' column (case-insensitively). Continues prompting until a valid breed
    is provided. Exit if q is entered.

    Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the dog breed data.
                                  It's assumed that the 'Breed' column exists
                                  and has been converted to uppercase for matching.

    Returns:
        str: The validated dog breed name in uppercase.
    """
    # Get unique breed names from the DataFrame, assuming they are already in uppercase
    # from a preprocessing step
    available_breeds = dataframe.index.get_level_values('Breed').unique()

    while True:
        breed_input = input("Enter a dog breed (or q to quit): ").strip().upper()
        if breed_input in available_breeds:
            return breed_input
        elif(breed_input == 'Q'):
            exit()
        else:
            # Raise a KeyError equivalent by printing the specified message
            print("Dog breed not found in the data. Please try again.")

def data_analysis(breed_name , yearly_df):
    """
    Analyze and print various statistics for a specified dog breed.

    This function retrieves registration data for the given breed, then:
      1. Identifies and prints all the years where the breed appeared among the top breeds.
      2. Computes and prints the total number of registrations for the breed.
      3. Calculates and prints the percentage of the breed's registrations relative to the total registrations per year.
      4. Determines and prints the overall percentage of the breed's registrations across all years.
      5. Finds and prints the month(s) in which the breed was most popular for registrations.

    Parameters:
        breed_name (str): The name of the dog breed (in uppercase) to analyze.
        yearly_df (pd.DataFrame): A pandas DataFrame containing registration data with a multi-index 
                                  ('Breed', 'Year') and columns including 'Total' and 'Month'.

    Returns:
        None
    """
    # get data frme for specific breed
    breed_yearly_data = yearly_df.loc[breed_name]

    # 1. Find and print all years where the selected breed was listed in the top breeds.
    unique_years = breed_yearly_data.index.get_level_values('Year').unique().tolist()
    print(f"The {breed_name} was found in the top breeds for the years: {' '.join(map(str, unique_years))} ")

    # 2. Calculate and print the total number of registrations of the selected breed
    # Sum the 'Total' column for the selected breed across all years it was listed
    total_breed_registrations = breed_yearly_data['Total'].sum()
    print(f"There have been {int(total_breed_registrations)} {breed_name} dogs registered total.") # Print as integer

    # 3. Calculate and print the percentage of selected breed registrations out of the total percentage for each year (2021, 2022, 2023).
    # need denominator for percentage calculation for each year.
    total_registrations_per_year_all_breeds = yearly_df.groupby('Year')['Total'].sum()
    # numerator
    total_registrations_per_year_chosen_breed = breed_yearly_data.groupby('Year')['Total'].sum()
    # print out per year precentage of breed
    for year in unique_years:
        precentage = (total_registrations_per_year_chosen_breed[year] / total_registrations_per_year_all_breeds[year]) * 100
        print(f"The {breed_name} was {precentage:.6f}% of top breeds in {year}.")

    # 4. Calculate and print the percentage of selected breed registrations out of the total three-year percentage.
    precentage = (breed_yearly_data['Total'].sum()/yearly_df['Total'].sum()) * 100
    print(f"The {breed_name} was {precentage:.6f}% of top breeds across all years.")

    # 5. Find and print the months that were most popular for the selected breed registrations. Print all months that tie.
    # breed_month_totals = breed_yearly_data.groupby('Month')['Total'].sum()
    # sorted_monthly_counts = breed_month_totals.sort_values(ascending=False)
    # sorted_monthly_tolist = sorted_monthly_counts.index.tolist()
    # print(f"Most popular month(s) for {breed_name} dogs: {', '.join(map(str, sorted_monthly_tolist))} ")

    breed_month_count_across_years = breed_yearly_data["Month"].value_counts()
    filtered_counts_list = breed_month_count_across_years[breed_month_count_across_years >= breed_month_count_across_years.max()].index.tolist()
    print(f"Most popular month(s) for {breed_name} dogs: {' '.join(map(str, filtered_counts_list))} ")

def main():

    # Import data here
    imported_data = data_frame_creation()
    # print(imported_data)
    print("ENSF 692 Dogs of Calgary")

    # User input stage
    validated_breed = user_input(imported_data)
    print(validated_breed)

    # Data anaylsis stage
    data_analysis(validated_breed, imported_data)

if __name__ == '__main__':
    main()
