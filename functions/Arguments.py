def year_of_birth(name,age):
    year=2023-age
    print(f"Hello {name},you are born in {year}")


def my_country (country="Kenya"):
    print (f"Hello you are from {country}")


def hello(*names):
    for name in names:
        print(f"Hello {name}")

        
def sum (*nums):
    answer=0
    for num in nums:
        answer +=num
    return answer



def multipy_many(**keywords):
    answer=1
    for num in keywords.values():
        answer*=num
    return answer
    

# Assignment

             #1
# A function named concatenate_args 
# that takes any number of string arguments in positional arguments format 
# and concatenates them into a single string
def concatenate_args(*names):
    results = ""
    for name in names:
        results += name
    return results


              #2
# A function named concatenate_kwargs 
# that takes any number of string arguments in keyword arguments  format 
# and concatenates them into a single string
def concatenate_kwargs(**persons):
    result = ""
    for person in persons.values():
        result += person
    return result