#product

def product(a, b):
    multiply_nums = a * b
    return multiply_nums

#weekday

def weekday_name(day_of_week):
    DAYS = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    if day_of_week < 1 or day_of_week > 7:
        return None

    return DAYS[day_of_week - 1]

#last_element

def last_element(lst):
    if lst:
        return lst[-1]
  
#compare

def number_compare(a, b):

    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    else:
        return "Numbers are equal"

#reverse_string

def reverse_string(elementary):
    return elementary[::-1]

#single_letter

def single_letter_count(word, letter):

    return word.lower().count(letter.lower())

#multiple_letter

def multiple_letter_count(phrase):
    counter = {}

    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1

    return counter

#list_manipulation

def list_manipulation(lst, command, location, value=None):
    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)

    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst


#palindrome

def is_palindrome(phrase):
    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]

#frequency

def frequency(lst, search_term):
    return lst.count(search_term)



