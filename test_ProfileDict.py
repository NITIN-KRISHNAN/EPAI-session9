from decimal import Decimal

import ProfileDict
import datetime
import ProfileNamedTuple


def test_form_profile_dict_from_namedtuple():
    profile_named_tuple = ProfileNamedTuple.form_profile_named_tuple()
    profile_dict = ProfileDict.form_profile_dict_from_namedtuple(profile_named_tuple)
    assert len(profile_dict) == ProfileNamedTuple.NUM_PROFILE
    assert type(profile_dict) == dict
    assert type(profile_dict.get(0)) == dict
    # profile_dict = Dict.form_profile_dict()


def test_dict_avg_age():
    profile_dict = {"0":{"birthdate":datetime.date(1980, 1, 1)}, "1":{"birthdate":datetime.date(2000, 1, 1)}}
    assert round(ProfileDict.calculate_avg_age(profile_dict)[0], 2) == 31.52


def test_dict_oldest_age():
    profile_dict = {"0":{"birthdate":datetime.date(1980, 1, 1)}, "1":{"birthdate":datetime.date(2000, 1, 1)}}
    assert round(ProfileDict.calculate_oldest_person_age(profile_dict)[0], 2) == 41.52


def test_dict_mean_current_location():
    profile_dict = {"0":{"current_location":(Decimal(20),Decimal(300))}, "1":{"current_location":(Decimal(100),Decimal(400))}}
    assert ProfileDict.calculate_mean_current_location(profile_dict)[0] == (Decimal('60'), Decimal('350'))


def test_dict_largest_blood_grp():
    profile_dict = {"0":{"blood_group":'AB+ve'}, "1":{"blood_group":'AB+ve'}, "2":{"blood_group":'O+ve'}}
    assert ProfileDict.calculate_largest_blood_type(profile_dict)[0] == 'AB+ve'
