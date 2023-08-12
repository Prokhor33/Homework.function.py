my_dict = {1: 'one', 2: ['Two'], '3': ('Three',)}

def inverse_try(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        try:
            new_dict[value] = key
        except:
            new_dict[str(value)] = key
    return new_dict

def inverse_instance(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        if not isinstance(value, list | set | dict):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
    return new_dict




print(inverse_try(one=1, two=['2'], three=(3,)))
print(inverse_instance(one=1, two=['2'], three=(3,)))


