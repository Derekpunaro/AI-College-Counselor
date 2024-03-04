# Import Libraries
import csv
import requests
# Import Libraries
import requests, random, csv
from math import radians, sin, cos, sqrt, atan2


# Recommendation Algorithm
def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance (in miles) between two geographical coordinates using the Haversine formula.
    """
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    radius_of_earth = 3958.8  # Radius of Earth in miles
    distance = radius_of_earth * c
    return distance


def get_coordinates(city_name, key):
    """
    Get the geographical coordinates (latitude and longitude) of a city using the Google Maps Geocoding API.
    """
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": city_name,
        "key": key
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200 and data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
        else:
            print(f"Error: Unable to retrieve coordinates for {city_name}. Status Code: {response.status_code}")
            return None, None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None, None


def filter_colleges_by_location(user_colleges, user_preferred_location, user_max_distance=None):
    latitude, longitude = get_coordinates(user_preferred_location, api_key)
    if latitude is not None and longitude is not None:
        print(f"Coordinates for {user_preferred_location}: Latitude={latitude}, Longitude={longitude}")
    else:
        return []
    # Filter colleges based on user preferences
    result_colleges = []

    for college in user_colleges:
        college_lat, college_lon = get_coordinates(college['location'], api_key)
        if college_lat is not None and college_lon is not None:
            distance = calculate_distance(latitude, longitude, college_lat, college_lon)
            if (user_max_distance is None or distance <= user_max_distance) or meets_user_criteria(college, GPA_requirement, SAT_requirement, ACT_requirement, majors_offered, financial_aid):
                result_colleges.append(college)
        else:
            print(f"Error: Unable to retrieve coordinates for {college['location']}")

    return result_colleges


def meets_user_criteria(college_, user_gpa, user_sat, user_act, user_desired_major, user_financial_aid):
    # Check GPA
    if college_['GPA_requirement'] > user_gpa:
        return False

    # Check SAT score
    if college_['SAT_requirement'] > user_sat:
        return False

    # Check ACT score
    if college_['ACT_requirement'] > user_act:
        return False

    # Check desired major
    if user_desired_major not in college_['majors_offered']:
        return False

    # Check financial aid
    if user_financial_aid == 'Y' and not college_['financial_aid_available']:
        return False

    return True


# User Profile Creation
# TODO: Allow users to input their academic information and preferences, such as GPA,
# TODO: standardized test scores (SAT/ACT), preferred location, desired major, and any other relevant criteria.
# Define the dataset of colleges with admission statistics
# User Interface
if __name__ == "__main__":
    api_key = "AIzaSyD3BT1pkLeIAmMT5bpAtIZyF3fEnTTosPo"  # Replace with your actual API key

    # Academic Information
    GPA_requirement = float(input(f"Please enter your GPA: "))
    SAT_requirement = int(input(f"Please enter your SAT: "))
    ACT_requirement = int(input(f"Please enter your ACT: "))
    preferred_location = input("Please enter your preferred city: ")
    radius = float(input("Please enter the radius (in miles): "))
    max_distance = float(input("Please enter the maximum distance in miles from the preferred location: "))
    majors_offered = input(f"Please enter your top desired major(s) separated by commas: ").split(',')
    financial_aid = input(f"Please enter Y/N if finances are a factor: ")
    if financial_aid == 'Y':
        financial_aid = True
    else:
        financial_aid = False
    # Define the dataset of colleges with admission statistics
    colleges = [
        {
            'name': 'Harvard University',
            'location': 'Cambridge',
            'GPA_requirement': 4.0,
            'SAT_requirement': 1550,
            'ACT_requirement': 34,
            'majors_offered': ['Computer Science', 'Economics', 'Biology'],
            'financial_aid_available': True
        },
        {
            'name': 'Stanford University',
            'location': 'Standford',
            'GPA_requirement': 3.9,
            'SAT_requirement': 1540,
            'ACT_requirement': 33,
            'majors_offered': ['Engineering', 'Humanities', 'Business'],
            'financial_aid_available': True
        },
        {
            'name': 'Massachusetts Institute of Technology (MIT)',
            'location': 'Cambridge',
            'GPA_requirement': 3.8,
            'SAT_requirement': 1560,
            'ACT_requirement': 35,
            'majors_offered': ['Engineering', 'Computer Science', 'Physics'],
            'financial_aid_available': True
        },
        # Add more colleges with similar attributes
        {
            'name': 'University of California, Berkeley',
            'location': 'Berkeley',
            'GPA_requirement': 3.7,
            'SAT_requirement': 1500,
            'ACT_requirement': 32,
            'majors_offered': ['Computer Science', 'Engineering', 'Economics'],
            'financial_aid_available': True
        },
        {
            'name': 'Yale University',
            'location': 'New Haven',
            'GPA_requirement': 3.8,
            'SAT_requirement': 1520,
            'ACT_requirement': 33,
            'majors_offered': ['Political Science', 'History', 'Biology'],
            'financial_aid_available': True
        },
        # Add more colleges with similar attributes
        {
            'name': 'University of Chicago',
            'location': 'Chicago',
            'GPA_requirement': 3.7,
            'SAT_requirement': 1510,
            'ACT_requirement': 32,
            'majors_offered': ['Economics', 'Biology', 'Political Science'],
            'financial_aid_available': True
        },
        # Add more colleges with similar attributes
        {
            'name': 'Columbia University',
            'location': 'New York City',
            'GPA_requirement': 3.8,
            'SAT_requirement': 1530,
            'ACT_requirement': 34,
            'majors_offered': ['Political Science', 'Engineering', 'English'],
            'financial_aid_available': True
        },
        # Add more colleges with similar attributes
        {
            'name': 'University of Pennsylvania',
            'location': 'Philadelphia',
            'GPA_requirement': 3.7,
            'SAT_requirement': 1505,
            'ACT_requirement': 32,
            'majors_offered': ['Finance', 'Biology', 'Computer Science'],
            'financial_aid_available': True
        },
        # Add more colleges with similar attributes
        {
            'name': 'Johns Hopkins University',
            'location': 'Baltimore',
            'GPA_requirement': 3.8,
            'SAT_requirement': 1500,
            'ACT_requirement': 33,
            'majors_offered': ['Medicine', 'Public Health', 'Computer Science'],
            'financial_aid_available': True
        },
        # Add more colleges with similar attributes
        {
            'name': 'Duke University',
            'location': 'Durham',
            'GPA_requirement': 3.7,
            'SAT_requirement': 1520,
            'ACT_requirement': 33,
            'majors_offered': ['Biology', 'Economics', 'Computer Science'],
            'financial_aid_available': True
        },
        # Add more colleges with similar attributes
        {
            'name': 'Northwestern University',
            'location': 'Evanston',
            'GPA_requirement': 3.7,
            'SAT_requirement': 1505,
            'ACT_requirement': 33,
            'majors_offered': ['Journalism', 'Economics', 'Engineering'],
            'financial_aid_available': True
        },
        # Add more colleges with similar attributes
        {
            'name': 'University of Michigan, Ann Arbor',
            'location': 'Ann Arbor',
            'GPA_requirement': 3.6,
            'SAT_requirement': 1450,
            'ACT_requirement': 31,
            'majors_offered': ['Business', 'Engineering', 'Psychology'],
            'financial_aid_available': True
        },
        # Add more colleges with similar attributes
        {
            'name': 'University of Virginia',
            'location': 'Charlottesville',
            'GPA_requirement': 3.6,
            'SAT_requirement': 1460,
            'ACT_requirement': 32,
            'majors_offered': ['History', 'Biology', 'Economics'],
            'financial_aid_available': True
        }
    ]

    # Select the first 15 colleges
    random_schools = colleges[:15]

    # Display the selected schools
    for school in random_schools:
        print("Name:", school['name'])
        print("GPA Requirement:", school['GPA_requirement'])
        print("SAT Requirement:", school['SAT_requirement'])
        print("ACT Requirement:", school['ACT_requirement'])
        print("Majors Offered:", ", ".join(school['majors_offered']))
        print("Financial Aid Available:", "Yes" if school['financial_aid_available'] else "No")
        print()

    csv_file = 'colleges.csv'

    # Define the field names for the CSV file
    fieldnames = ['name', 'location', 'GPA_requirement', 'SAT_requirement', 'ACT_requirement', 'majors_offered',
                  'financial_aid_available']

    # Write the dataset to a CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data for each college
        for college in colleges:
            writer.writerow(college)

    filtered_colleges = filter_colleges_by_location(colleges, preferred_location, max_distance)

    if filtered_colleges:
        print("Colleges within the specified distance:")
        for college in filtered_colleges:
            print(college['name'], "-", college['location'])
    else:
        print("No colleges found within the specified distance.")
