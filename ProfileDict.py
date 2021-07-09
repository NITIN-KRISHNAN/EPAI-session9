from faker import Faker
import time
import datetime

faker = Faker()
NUM_PROFILE = 10000


def form_profile_dict() -> dict:
    """
    Function to form the dict which contains 10000 generated fake profiles
    :return: dict which contains generated fake profiles
    """
    profile_dict = {}
    for i in range(NUM_PROFILE):
        profile_dict[i] = faker.profile()
    return profile_dict


def form_profile_dict_from_namedtuple(profile_named_tuple) -> dict:
    """
    Function to form the dict which contains 10000 generated fake profiles, this dict is generated
    from the profile named tuple that us given as parameter
    :return: dict which contains generated fake profiles
    """
    profile_dict = {}
    i = 0
    for profile in profile_named_tuple:
        profile_dict[i] = dict(profile._asdict())
        i += 1
    return profile_dict


def calculate_largest_blood_type(profile_dict) -> tuple:
    """
    Function to calculate the blood type with most number of people
    :param profile_dict: dict which contains generated fake profiles
    :return: tuple of blood type with most number of people and time taken to execute this function
    """
    start_time = time.time()
    grp_count = {}
    for profile in profile_dict.values():
        grp = profile['blood_group']
        count = grp_count.get(grp, 0)
        count += 1
        grp_count[grp] = count
        # print(grp_count)
    max_blood_grp = max(grp_count, key = grp_count.get)
    # print(max_blood_grp)
    end_time = time.time()
    return max_blood_grp, end_time-start_time


def calculate_mean_current_location(profile_dict) -> tuple:
    """
    Function to mean current location
    :param profile_dict: dict which contains generated fake profiles
    :return: tuple of mean current location (which is a tuple of latitude and longitude coordinates)
    and time taken to execute this function
    """
    start_time = time.time()
    sum_x = 0
    sum_y = 0
    for profile in profile_dict.values():
        sum_x += profile['current_location'][0]
        sum_y += profile['current_location'][1]
    mean_current_location = sum_x/ len(profile_dict) , sum_y / len(profile_dict)
    end_time = time.time()
    return mean_current_location, end_time - start_time


def calculate_oldest_person_age(profile_dict) -> tuple:
    """
    Function to oldest person age
    :param profile_dict: dict which contains generated fake profiles
    :return: tuple of oldest person age and time taken to execute this function
    """
    start_time = time.time()
    max_age = max((datetime.date.today() - profile['birthdate']).days for profile in profile_dict.values()) / 365.25
    end_time = time.time()
    return max_age, end_time - start_time


def calculate_avg_age(profile_dict):
    """
    Function to Average person age
    :param profile_dict: dict which contains generated fake profiles
    :return: tuple of average person age and time taken to execute this function
    """
    start_time = time.time()
    avg_age = sum((datetime.date.today() - profile['birthdate']).days for profile in profile_dict.values()) / len(profile_dict) / 365.25
    end_time = time.time()
    return avg_age, end_time - start_time
