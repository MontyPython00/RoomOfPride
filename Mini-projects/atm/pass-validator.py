import string


# pass_validation
user_pass = input()
def pass_validator(user_pass):

    char_upper = False
    char_lower = False
    char_punct = False
    char_digit = False
    if (6 <= len(user_pass))&(len(user_pass) <= 12):
        for validator in user_pass:

            if validator.islower():
                char_lower = True

            if validator.isupper():
                char_upper = True

            if validator.isdigit():
                char_digit = True

            if((char_digit)and(char_lower)and(char_digit)):
                for validator in user_pass:
                    for punct in string.punctuation:
                        if punct == validator:
                            char_punct = True
                                                   

pass_validator(user_pass)
