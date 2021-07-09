from decimal import Decimal
from collections import namedtuple
import ProfileNamedTuple
import datetime


def test_form_profile_named_tuple():
    profile_named_tuple = ProfileNamedTuple.form_profile_named_tuple()
    assert len(profile_named_tuple) == ProfileNamedTuple.NUM_PROFILE
    assert type(profile_named_tuple[1]) == ProfileNamedTuple.Profile
    assert type(profile_named_tuple) == ProfileNamedTuple.ProfileList
    assert profile_named_tuple[1].__doc__ is not None
    assert profile_named_tuple[1]._fields == ProfileNamedTuple.Profile._fields
    profile1 = ProfileNamedTuple.Profile('job1', 'comp1', 'ssn1', 'res1', (Decimal(20), Decimal(300)), 'AB+ve', 'w', 'u',
                                         'nam1', 'M', 'a', 'mail', datetime.date(2000, 1, 1))
    profile2 = ProfileNamedTuple.Profile('job1', 'comp1', 'ssn1', 'res1', (Decimal(20), Decimal(300)), 'AB+ve', 'w', 'u',
                                         'nam1', 'M', 'a', 'mail', datetime.date(2000, 1, 1))
    assert  profile1 == profile2


def test_namedtuple_avg_age():
    ProfileListExt = namedtuple("ProfileListExt",  list(range(2)), rename=True)
    profile1 = ProfileNamedTuple.Profile('job1', 'comp1', 'ssn1', 'res1', (Decimal(20),Decimal(300)), 'AB+ve', 'w', 'u',
                                         'nam1', 'M', 'a', 'mail', datetime.date(2000, 1, 1))
    profile2 = ProfileNamedTuple.Profile('job2', 'comp2', 'ssn2', 'res2', (Decimal(20),Decimal(300)), 'AB+ve', 'w', 'u',
                                         'nam2', 'M', 'a', 'mail', datetime.date(1990, 1, 1))
    profile_list = ProfileListExt(*[profile1, profile2])
    assert round(ProfileNamedTuple.calculate_avg_age(profile_list)[0], 2) == 26.52


def test_namedtuple_oldest_age():
    ProfileListExt = namedtuple("ProfileListExt",  list(range(2)), rename=True)
    profile1 = ProfileNamedTuple.Profile('job1', 'comp1', 'ssn1', 'res1', (Decimal(20),Decimal(300)), 'AB+ve', 'w', 'u',
                                         'nam1', 'M', 'a', 'mail', datetime.date(2000, 1, 1))
    profile2 = ProfileNamedTuple.Profile('job2', 'comp2', 'ssn2', 'res2', (Decimal(300),Decimal(20)), 'AB+ve', 'w', 'u',
                                         'nam2', 'M', 'a', 'mail', datetime.date(1990, 1, 1))
    profile_list = ProfileListExt(*[profile1, profile2])
    assert round(ProfileNamedTuple.calculate_oldest_person_age(profile_list)[0], 2) == 31.52


def test_namedtuple_mean_current_location():
    ProfileListExt = namedtuple("ProfileListExt",  list(range(2)), rename=True)
    profile1 = ProfileNamedTuple.Profile('job1', 'comp1', 'ssn1', 'res1', (Decimal(20),Decimal(300)), 'AB+ve', 'w', 'u',
                                         'nam1', 'M', 'a', 'mail', datetime.date(2000, 1, 1))
    profile2 = ProfileNamedTuple.Profile('job2', 'comp2', 'ssn2', 'res2', (Decimal(300),Decimal(20)), 'AB+ve', 'w', 'u',
                                         'nam2', 'M', 'a', 'mail', datetime.date(1990, 1, 1))
    profile_list = ProfileListExt(*[profile1, profile2])
    assert ProfileNamedTuple.calculate_mean_current_location(profile_list)[0] == (Decimal('160'), Decimal('160'))


def test_namedtuple_largest_blood_grp():
    ProfileListExt = namedtuple("ProfileListExt",  list(range(3)), rename=True)
    profile1 = ProfileNamedTuple.Profile('job1', 'comp1', 'ssn1', 'res1', (Decimal(20),Decimal(300)), 'AB+ve', 'w', 'u',
                                         'nam1', 'M', 'a', 'mail', datetime.date(2000, 1, 1))
    profile2 = ProfileNamedTuple.Profile('job2', 'comp2', 'ssn2', 'res2', (Decimal(300),Decimal(20)), 'AB+ve', 'w', 'u',
                                         'nam2', 'M', 'a', 'mail', datetime.date(1990, 1, 1))
    profile3 = ProfileNamedTuple.Profile('job3', 'comp2', 'ssn2', 'res2', (Decimal(300),Decimal(20)), 'B+ve', 'w', 'u',
                                         'nam3', 'M', 'a', 'mail', datetime.date(1980, 1, 1))
    profile_list = ProfileListExt(*[profile1, profile2, profile3])
    assert ProfileNamedTuple.calculate_largest_blood_type(profile_list)[0] == 'AB+ve'
