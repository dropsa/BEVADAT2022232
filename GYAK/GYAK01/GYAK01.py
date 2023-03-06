def contains_odd(input_list):
    for number in input_list:
        if number % 2 != 0:
            return True
    return False

def is_odd(input_list):
    mask = []
    for number in input_list:
        if number % 2 == 0:
            mask.append(False)
        else:
            mask.append(True)
    return mask

def element_wise_sum(input_list_1, input_list_2):
    output_list = []
    for i in range(min(len(input_list_1), len(input_list_2))):
        output_list.append(input_list_1[i] + input_list_2[i])
    return output_list

def dict_to_list(input_dict : dict) -> list:
    outputlist=[]
    for key,value in input_dict.items():
        outputlist.append((key,value))
    return outputlist
