import Levenshtein as lev #to be replaced by fuzzy

########################################################################################

# to be made into a class

def get_ratio_and_dist(input_string,correct_string):
    """
    returns the lev ratio, lev dist between two strings
    """
    ratio =lev.ratio(input_string,correct_string)
    distance=lev.distance(input_string,correct_string)

    return ratio,distance


def auto_correct(input_string,correct_string):
    """
    will attempt to find a match for a string
    INCOMPLETE
    """
    ratio,original_distance = get_ratio_and_dist(input_string,correct_string)
    distance = original_distance
    print(ratio,distance)

    if ratio < 1:
        # not inital match

        while distance != 0:
            input_string,correct_string = input_string.lower(),correct_string.lower()
            ratio,distance = get_ratio_and_dist(input_string,correct_string)

            print('no match found for: "{}"'.format(input_string))

        else:
            print('match found from {} fixes'.format(original_distance))
    else:
        print('initial match found!')

########################################################################################

correct_string = 'Correct String!'
input_strings = ['correct string','correct String','Correct string','Correct String!']

for input_string in input_strings:
    auto_correct(input_string,correct_string)
    

