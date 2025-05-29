# school_data.py
# Manuja Senanayake
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc.
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import (
    year_2013,
    year_2014,
    year_2015,
    year_2016,
    year_2017,
    year_2018,
    year_2019,
    year_2020,
    year_2021,
    year_2022,
)

# Declare any global variables needed to store the data here
years = (2013,2014,2015,2016,2017,2018,2019,2020,2021,2022)
grades = (10, 11, 12)
schools = ("Centennial High School" , "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", "Forest Lawn High School",
           "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", "James Fowler High School",
           "Ernest Manning High School", "William Aberhart High School", "National Sport School", "Henry Wise Wood High School",
           "Bowness High School", "Lord Beaverbrook High School", "Jack James High School", "Sir Winston Churchill High School",
           "Dr. E. P. Scarlett High School", "John G Diefenbaker High School", "Lester B. Pearson High School")
schools_code = ("1224", "1679", "9626", "9806", "9813", "9815", "9816", "9823", "9825", "9826", "9829", "9830", "9836", "9847", "9850",
              "9856", "9857", "9858", "9860", "9865")
# Create a mapping from code to name for easy lookup (if needed)
school_code_to_name = dict(zip(schools_code, schools))


# You may add your own additional classes, functions, variables, etc.

num_years = 10
num_grades = 3 # Grades  10, 11, 12
num_schools = 20
array_shape = (num_years, num_schools, num_grades)

# Reshaping to 2D arrays
year_2013_2d = year_2013.reshape(num_schools, num_grades)
year_2014_2d = year_2014.reshape(num_schools, num_grades)
year_2015_2d = year_2015.reshape(num_schools, num_grades)
year_2016_2d = year_2016.reshape(num_schools, num_grades)
year_2017_2d = year_2017.reshape(num_schools, num_grades)
year_2018_2d = year_2018.reshape(num_schools, num_grades)
year_2019_2d = year_2019.reshape(num_schools, num_grades)
year_2020_2d = year_2020.reshape(num_schools, num_grades)
year_2021_2d = year_2021.reshape(num_schools, num_grades)
year_2022_2d = year_2022.reshape(num_schools, num_grades)

# converting to 3D array Resulting shape: (Number of Years, Number of Schools, Number of Grades)
all_years_2d_arrays = [year_2013_2d, year_2014_2d, year_2015_2d, year_2016_2d, year_2017_2d, year_2018_2d, year_2019_2d, year_2020_2d, year_2021_2d, year_2022_2d]

def get_valid_school_input():
    """
    Prompts the user to enter a school name or code and validates it.
    Raises ValueError if the input is not found in the data.
    Returns the validated school name.
    """
    user_input = input("Enter either the name or numerical code of a school: ").lower().title().strip()

    # Check if input is a school name
    if user_input in schools:
        return user_input # Return the name directly

    # Check if input is a school code
    elif user_input in schools_code:
        school_name = school_code_to_name[user_input]
        return school_name # Return the corresponding name

    # If neither name nor code is found, raise a ValueError
    else:
        raise ValueError("You must enter a valid school name or code.")

def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    enrollment_3d_array = np.stack(all_years_2d_arrays, axis=0)
    print("Shape of full data array: ", enrollment_3d_array.shape)
    print("Dimensions of full data array: ", enrollment_3d_array.ndim)

    # Prompt for user input
    try:
        selected_school_name = get_valid_school_input()
        # print(f"Proceeding with data for: {selected_school_name}")  //test

        # Print Stage 2 requirements here
        print("\n***Requested School Statistics***\n")

        # Get the numerical index for the selected school
        school_idx = schools.index(selected_school_name)
        selected_school_code = schools_code[school_idx]

        print(f"School Name: {selected_school_name}, School Code: {selected_school_code}")

        # Extract data for the selected school across all years and grades
        school_data = enrollment_3d_array[:, school_idx, :] # Shape (num_years, num_grades)

        # Mean enrollment for Grade 10, 11, 12 across all years
        mean_g10 = school_data[:, grades.index(10)].mean()
        mean_g11 = school_data[:, grades.index(11)].mean()
        mean_g12 = school_data[:, grades.index(12)].mean()
        print(f"Mean enrollment for grade {grades[grades.index(10)]:.0f}: {mean_g10:.0f}")
        print(f"Mean enrollment for grade {grades[grades.index(11)]:.0f}: {mean_g11:.0f}")
        print(f"Mean enrollment for grade {grades[grades.index(12)]:.0f}: {mean_g12:.0f}")

        # Highest and Lowest enrollment for a single grade within the entire time period
        highest_enrollment = school_data.max()
        lowest_enrollment = school_data.min()
        print(f"Highest enrollement for a single greade: {highest_enrollment:.0f}")
        print(f"Lowest enrollement for a single greade: {lowest_enrollment:.0f}")

        # Total enrollment for each year
        yearly_totals = []
        for i, year in enumerate(years):
            total_for_year = school_data[i, :].sum() # Sum across grades for current year
            yearly_totals.append(total_for_year)
            print(f"Total enrollment for {year:.0f}: {total_for_year:.0f}")

        # Total ten-year enrollment
        total_ten_year_enrollment = school_data.sum() # Sum all enrollments for the school
        print(f"Total ten-year enrollment: {total_ten_year_enrollment:.0f}")

        # Mean total yearly enrollment over 10 years
        mean_total_yearly_enrollment = np.mean(yearly_totals)
        print(f"Mean total yearly enrollment over 10 years: {mean_total_yearly_enrollment:.0f}")

        # Enrollment numbers over 500 and median of those
        enrollments_over_500 = school_data[school_data > 500]

        if enrollments_over_500.size == 0:
            print("No enrollments over 500.")
        else:
            median_over_500 = np.median(enrollments_over_500)
            print(f"Median value of enrollments > 500: {median_over_500:.0f}")

        # Print Stage 3 requirements here
        print("\n***General Statistics for All Schools***\n")

        year_2013_idx = years.index(2013) 
        year_2022_idx = years.index(2022) 
        grade_12_idx = grades.index(12)

        # All the nan versions of the functions below is using masking (Nan values is are ignored)

        # Mean enrollment in 2013 (across all schools and all grades for that year)
        mean_enrollment_2013 = np.nanmean(enrollment_3d_array[year_2013_idx, :, :])
        print(f"Mean enrollment in {years[year_2013_idx]:.0f}: {mean_enrollment_2013:.0f}")
        # Mean enrollment in 2022 (across all schools and all grades for that year)
        mean_enrollment_2022 = np.nanmean(enrollment_3d_array[year_2022_idx, :, :])
        print(f"Mean enrollment in {years[year_2022_idx]:.0f}: {mean_enrollment_2022:.0f}")

        # Total graduating class of 2022 across all schools (Grade 12 for 2022)
        total_graduating_2022 = np.nansum(enrollment_3d_array[year_2022_idx, :, grade_12_idx])
        print(f"Total graduating class of {years[year_2022_idx]:.0f} (Grade 12): {total_graduating_2022:.0f}")

        # Highest enrollment for a single grade within the entire time period (across all schools)
        highest_overall_enrollment = np.nanmax(enrollment_3d_array)
        print(f"Highest enrollment for a single grade: {highest_overall_enrollment:.0f}")
        # Lowest enrollment for a single grade within the entire time period (across all schools)
        lowest_overall_enrollment = np.nanmin(enrollment_3d_array)
        print(f"Lowest enrollment for a single grade: {lowest_overall_enrollment:.0f}")     

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    

if __name__ == "__main__":
    main()
