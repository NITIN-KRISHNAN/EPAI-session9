# EPAI-session9

## Problem statement

1. Use the Faker library to get 10000 random profiles. Using namedtuple, calculate the
   largest blood type, mean-current_location, oldest_person_age, and average age (add proper doc-strings).
    - 250 (including 5 test cases)
2. Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250 (including 5 test cases)
3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies
   (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the
   stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high,
   close are not totally random. You can only use namedtuple. - 500  (including 10 test cases)
4. Please write a readme file that can help me understand your code. If you don't write a readme properly,
   I would not be evaluating that piece of the code. 
5. Add the notebook as well to your github where logs can be visible. Your github code must have cleared all the
   20 tests that you're writing (these 20 cannot be any of the ones you can already find in the code we shared earlier).
   
## ProfileNamedTuple
This file has the code to create the user profile from faker using Named tuple.

The Profile namedtuple profile is created with the following fields
###Data descriptors defined here:

| Field name | Field description |
| --- | --- |
|  job |      Job designation of the person |  
|  company |      Company where the person is employed in|  
 |  ssn|      Social security number of the person|  
 |  residence|      Residence of the person|  
|  current_location |      Current location coordinates (latitude, longitude) of the person|  
|  blood_group|      Blood group of the person|
 |  website|      List of websites of the person|  
 |  username|      username of the person|  
 |  name|      Name of the person|  
 |  sex|      Gender of the person|  
 |  address|      address of the person|  
 |  mail|      E-mail address of the person|  
 |  birthdate|      birthdate of the person|  

ProfileList namedtuple comtains all the profiles in a list 

### FUNCTIONS

    calculate_avg_age(profile_list) -> tuple
        Function to average person age
        :param profile_list: namedtuple which contains generated fake profiles
        :return: tuple of average person age and time taken to execute this function
    
    calculate_largest_blood_type(profile_list) -> tuple
        Function to calculate the blood type with most number of people
        :param profile_list: namedtuple which contains generated fake profiles
        :return: tuple of blood type with most number of people and time taken to execute this function
    
    calculate_mean_current_location(profile_list) -> tuple
        Function to mean current location
        :param profile_list: namedtuple which contains generated fake profiles
        :return: tuple of mean current location (which is a tuple of latitude and longitude coordinates)
        and time taken to execute this function
    
    calculate_oldest_person_age(profile_list) -> tuple
        Function to oldest person age
        :param profile_list: namedtuple which contains generated fake profiles
        :return: tuple of oldest person age and time taken to execute this function
    
    form_profile_named_tuple() -> ProfileNamedTuple.ProfileList
        Function to form the namedtuple which contains 10000 generated fake profiles
        :return: namedtuple which contains generated fake profiles


## ProfileDict
This file has the code to create the user profile from faker using dict. The ProfileNamedTuple function
form_profile_named_tuple is reused to populate the dict using faker by converting the named tuple into dict
The keys used in the profile dict is same as Data descriptors above.

###FUNCTIONS

    calculate_avg_age(profile_dict)
        Function to Average person age
        :param profile_dict: dict which contains generated fake profiles
        :return: tuple of average person age and time taken to execute this function
    
    calculate_largest_blood_type(profile_dict) -> tuple
        Function to calculate the blood type with most number of people
        :param profile_dict: dict which contains generated fake profiles
        :return: tuple of blood type with most number of people and time taken to execute this function
    
    calculate_mean_current_location(profile_dict) -> tuple
        Function to mean current location
        :param profile_dict: dict which contains generated fake profiles
        :return: tuple of mean current location (which is a tuple of latitude and longitude coordinates)
        and time taken to execute this function
    
    calculate_oldest_person_age(profile_dict) -> tuple
        Function to oldest person age
        :param profile_dict: dict which contains generated fake profiles
        :return: tuple of oldest person age and time taken to execute this function
    
    form_profile_dict() -> dict
        Function to form the dict which contains 10000 generated fake profiles
        :return: dict which contains generated fake profiles
    
    form_profile_dict_from_namedtuple(profile_named_tuple) -> dict
        Function to form the dict which contains 10000 generated fake profiles, this dict is generated
        from the profile named tuple that us given as parameter
        :return: dict which contains generated fake profiles

## Conclusion
### From the logs in DriverProfile notebook the time taken by namedtuple is less than dict
| Task | Time taken by namedtuple | Time taken by dict |
| --- | --- | --- |
| Largest Blood group | 0.003495931625366211 | 0.00608515739440918 |
| Mean current location | 0.008796215057373047 | 0.009984016418457031 |
| Oldest person age | 0.02734375 | 0.03199577331542969 |
| Average age | 0.020982027053833008 | 0.024750947952270508 |


## Stock
This file has the code to create stock market with random open, close, high, low values and also calculate
the index based on random weights allocated to the stocks

### Stock Named tuple
Stock Named tuple contains the fields that are used to define a stock.
This namedtuple represents a stock and its daily change

#### Data descriptors defined here:
 | Field name | Field description |
| --- | --- |
 |  name|      Stock name|
 |  symbol|      Stock symbol used on ticker|  
 |  open|      Day's Opening price of the stock|  
 |  high|      Day's High price of the stock|
 |  low|      Day's low price of the stock|  
 |  close|      Day's Closing price of the stock |

### StockExt Named tuple
StockExt Named tuple extends the Stock Named tuple, it contains all the fields that are present in Stock Named tuple
and additionally has the weightage of the stock in the index.
This namedtuple extends a stock and adds the weightage of the stock in the index

#### Data descriptors defined here:
 | Field name | Field description |
| --- | --- |
 |  weight|      Represents the weightage of the stock in the index|

### StockMarket Named tuple
This namedtuple represents the stock market which comprises of many stocks 

### Index named tuple
This namedtuple represents the daily movement of the index

#### Data descriptors defined here:
  | Field name | Field description |
| --- | --- |
 |  open|      Day's opening price of the index|  
 |  high|      Day's high price of the index|  
 |  low|      Day's low price of the index|  
 |  close|      Day's close price of the index|  

### FUNCTIONS

    calculate_index(stock_market) -> Stock.Index
        Function to calculate the index's price movement
        :param stock_market: namedtuple representing the stock market which comprises of many stocks
        :return: index namedtuple which contains the index's price movement (open, high, low, close)
    
    create_stock_market() -> Stock.StockMarket
        Function to create random stocks
        :return: namedtuple representing the stock market which comprises of many stocks
    
    get_random_stock() -> Stock.Stock
        Function to create random stock and its day's price movement using faker lib
        :return: randomly generated Stock
    
    get_random_weights(num) -> list
        Functions to create index weightage distribution
        :param num: number of stocks in the market
        :return: list of weights of stocks in the index

### Sample 10 stocks in the stock market and its price movement in a day
|Name                        |    Symbol      |Open price (Rs.)  |  High price (Rs.)  |  Low price (Rs.) |   Close price (Rs.)  |     Weight|
| --- | --- | --- | --- | --- | --- | --- |
|Greene Ltd                    |  Gre63          |     5621.53 |            6700             |  5084.42      |        6058.02 |  0.00971168|
|Wright, Lopez and Kane         | Wri46         |      4634.59  |           5157.14         |   4632.02       |       5011.68 |  0.0101038|
|Patterson, Reeves and James    | Pat12        |       7163.93   |          7723.26        |    5827.41        |      7447.03 |  0.00260452|
|Reese-Pratt                    | Ree24       |        6031.13    |         6552.33       |     5567.29         |     5629.03 |  0.0107153|
|Lopez PLC                      | Lop59      |         6061.38     |        7231.75      |      5005.82          |    6047.83 |  0.00789718|
|Camacho-Howe                   | Cam94     |          3571.5       |       3843.22     |       3234.55           |   3748.17 |  0.0134033|
|Conrad Ltd                     | Con43    |           8626.31       |     10029.4     |        7065.32            |  7195.88 |  0.0114776|
|Hines-Simmons                  | Hin97   |            4708.59        |     4892.58   |         4426.24             | 4749.92   |0.0194279|
|Randall, Edwards and King      | Ran58  |             1100.07         |    1182.94  |           938.907             |1013.9   | 0.011945|
|Harris Inc                     | Har53 |              1592.4           |   1763.19 |           1498.53              |1607.8  |  0.0160419|

## Test cases
|Test Name                        |    Test description      |
| --- | --- |
| test_form_profile_dict_from_namedtuple| Test to check if the profile dictionary is formed properly|
| test_dict_avg_age| To check if average age calculation is correct when dict is used |
| test_dict_oldest_age|To check if oldest age calculation is correct when dict is used |
| test_dict_mean_current_location| to check if mean current location calculation is correct when dict is used |
| test_dict_largest_blood_grp| to check if largest blood group calculation is correct when dict is used|
|test_form_profile_named_tuple |  Test to check if the profile named tuple is formed properly|
|test_namedtuple_avg_age |To check if average age calculation is correct when named tuple is used  |
| test_namedtuple_oldest_age|To check if oldest age calculation is correct when named tuple  is used |
|test_namedtuple_mean_current_location |to check if mean current location calculation is correct when named tuple is used  |
| test_namedtuple_largest_blood_grp| to check if largest blood group calculation is correct when named tuple is used |
| test_stock_types| To check if the type of Stock named tuple is correct|
|test_create_stock_market | to check if the required number of stocks are created|
|test_weights_add_to_one | to check if the weights add up to one |
| test_random_stock_sanity| to check the daily stock price levels are proper for a random stock |
| test_all_stock_sanity| to check the daily stock price levels are proper for sll stocks |
| test_index_sanity|to check the daily stock price levels are proper for a index  |
| test_index_calculation| to check the index calculation is correct  |
| test_unique_stock_ticker| to check that no stock name and symbol is duplicated |
| test_upper_circuits| to check that no stock crosses its upper circuit price|
| test_lower_circuits| to check that no stock crosses its lower circuit price|

Note: Normal README and coding style tests are not listed here.

## Test cases result
test_ProfileDict.py::test_form_profile_dict_from_namedtuple PASSED       [  3%]

test_ProfileDict.py::test_dict_avg_age PASSED                            [  7%]

test_ProfileDict.py::test_dict_oldest_age PASSED                         [ 11%]

test_ProfileDict.py::test_dict_mean_current_location PASSED              [ 14%]

test_ProfileDict.py::test_dict_largest_blood_grp PASSED                  [ 18%]

test_ProfileNamedTuple.py::test_form_profile_named_tuple PASSED          [ 22%]

test_ProfileNamedTuple.py::test_namedtuple_avg_age PASSED                [ 25%]

test_ProfileNamedTuple.py::test_namedtuple_oldest_age PASSED             [ 29%]

test_ProfileNamedTuple.py::test_namedtuple_mean_current_location PASSED  [ 33%]

test_ProfileNamedTuple.py::test_namedtuple_largest_blood_grp PASSED      [ 37%]

test_Stock.py::test_stock_types PASSED                                   [ 40%]

test_Stock.py::test_create_stock_market PASSED                           [ 44%]

test_Stock.py::test_weights_add_to_one PASSED                            [ 48%]

test_Stock.py::test_random_stock_sanity PASSED                           [ 51%]

test_Stock.py::test_all_stock_sanity PASSED                              [ 55%]

test_Stock.py::test_index_sanity PASSED                                  [ 59%]

test_Stock.py::test_index_calculation PASSED                             [ 62%]

test_Stock.py::test_unique_stock_ticker PASSED                           [ 66%]

test_Stock.py::test_upper_circuits PASSED                                [ 70%]

test_Stock.py::test_lower_circuits PASSED                                [ 74%]

test_common.py::test_readme_exists PASSED                                [ 77%]

test_common.py::test_readme_contents PASSED                              [ 81%]

test_common.py::test_readme_proper_description PASSED                    [ 85%]

test_common.py::test_readme_file_for_formatting PASSED                   [ 88%]

test_common.py::test_indentations PASSED                                 [ 92%]

test_common.py::test_function_name_had_cap_letter PASSED                 [ 96%]

test_common.py::test_mandatory_fuctions_availability PASSED              [100%]

======================== 27 passed in 62.03s (0:01:02) =========================

