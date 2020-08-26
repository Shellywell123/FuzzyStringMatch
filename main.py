

correct_string = 'Correct String!'
input_strings = ['correct_string','correct string','correct String','Correct string']

for input_string in input_strings:
    result = input_string == correct_string

    if result == False:
        # not inital match
        result = input_string.lower() == correct_string.lower()

        if result == False:
            #not a case problem
            print('no match found for: "{}"'.format(input_string))

        else:
            print('match found!')

    else:
        print('match found!')