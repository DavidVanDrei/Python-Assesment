from websites.resources.data import WEBSITES
from functions import *

number2function = {
    '1': findData,
    '2': amendData,
    '3': cleanseData,
    '4': dataCalculation
}

def data_decorator(func):
    return(func(WEBSITES))



number = input("""Enter the number of the function you wish to use \n
1) Find Data
2) Amend Data
3) Cleanse Data
4) Perform data Calculation
""")

print(data_decorator(number2function[number]))



