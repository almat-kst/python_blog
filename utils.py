from exceptions import *

def option_input(string):
    result = input(string)
    if not result.isdigit():
        raise UserInputOptionException
    return result


def get_option_input():
    try:
        input_function = option_input
    except NameError:
        input_function = input

    return input_function


def username_input(string):
    result = input(string)
    if not result[0].isalpha() or len(result) < 5:
        raise InvalidUsernameException
    return result


def get_username_input():
    try:
        input_function = username_input
    except NameError:
        input_function = input

    return input_function


def password_input(string):
    result = input(string)
    if len(result) < 8:
        raise InvalidPasswordException
    return result


def get_password_input():
    try:
        input_function = password_input
    except NameError:
        input_function = input

    return input_function


def name_input(string):
    name = input(string)
    for i in name:
        if not i.isalpha():
            raise InvalidNameException
    return name


def get_name_input():
    try:
        input_function = name_input
    except NameError:
        input_function = input

    return input_function

def age_input(string):
    age = input(string)
    for i in age:
        if i.isalpha():
            raise InvalidNameException
    return age

def get_age_input():
    try:
        input_function = age_input
    except Exception as ex:
        input_function = input

    return input_function


def title_input(string):
    title = input(string)
    return title


def get_title_input():
    try:
        input_function = title_input
    except NameError:
        input_function = input

    return input_function

def description_input(string):
    description= input(string)
    return description


def get_description_func():
    try:
        input_function = description_input
    except NameError:
        input_function = input

    return input_function

def id_input(string):
    id = input(string)
    for i in id:
        if i.isalpha():
            raise InvalidNameException
    return id

def get_id_func():
    try:
        input_function = id_input
    except NameError:
        input_function = input

    return input_function

# def id_input(string):
#     id = input(string)
#     if id <= 0:
#         raise InvalidInputIdException
#     return id 

# def get_id_func():
#     try:
#         input_function = id_input
#     except NameError:
#         input_function = input

#     return input_function

def raise_exception(ex):
    raise ex