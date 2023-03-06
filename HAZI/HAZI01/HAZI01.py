
def subset(input_list, start, end):
    return input_list[start:end]

def every_nth(input_list, n):
    return input_list[::n]

def unique(input_list : list) -> bool:
    for i in range(0, len(input_list), 1):
        for j in range(len(input_list)-1, -1, -1):
            if j != i:
                if input_list[i]==input_list[j]:
                    return False
    return True

def flatten(input_list):
    output_list = []
    for sublist in input_list:
        for item in sublist:
            output_list.append(item)
    return output_list

def merge_lists(*args):
    result = []
    for arg in args:
        result += arg
    return result

def reverse_tuples(input_list):
    output_list = []
    for tpl in input_list:
        output_list.append((tpl[1], tpl[0]))
    return output_list

def remove_tuplicates(input_list : list) -> list:
    removable=[]
    for i in range(0, len(input_list), 1):
        for j in range(len(input_list)-1, -1, -1):
            if j != i:
                if input_list[i]==input_list[j]:
                    if(input_list[i] not in removable):
                        removable.append(input_list[i])
    for x in removable:
        input_list.remove(x)
    return input_list

def transpose(input_list : list) -> list:
    result = []

    for i in range(len(input_list)):
        subresult=[]
        for j in range(len(input_list[i])):
            subresult.append(0)
        result.append(subresult)

    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            result[i][j]=input_list[j][i]
    
    return result

def split_into_chunks(input_list, chunk_size):
    chunks = []
    for i in range(0, len(input_list), chunk_size):
        chunks.append(input_list[i:i+chunk_size])
    return chunks

def merge_dicts(*args):
    merged_dict = {}
    for arg in args:
        merged_dict.update(arg)
    return merged_dict

def by_parity(input_list):
    result = {'even': [], 'odd': []}
    for num in input_list:
        if num % 2 == 0:
            result['even'].append(num)
        else:
            result['odd'].append(num)
    return result

def mean_key_value(d):
    result = {}
    for key in d:
        mean = sum(d[key]) / len(d[key])
        result[key] = mean
    return result

