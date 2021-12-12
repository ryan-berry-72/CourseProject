from pprint import pprint


def print_object(obj):
    pprint(vars(obj))


# X falls between A and B, but I want it to fall between C and D
def linear_mapping(X, A, B, C, D):
    return (X-A)/(B-A)*(D-C)+C


# ensures that value falls between the bounds (inclusive)
def contain_value_in_range(value, lower_bound, upper_bound):
    return min(max(value, lower_bound), upper_bound)
