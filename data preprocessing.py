import os

# To transform the original non-standard json file to json objects array
# for further use

data = []

with open(os.path.join(os.path.dirname('__file__'), "Data/obfuscated_data.json"), 'rb') as f:
    for line in f:
        data.append(json.loads(line.decode()))

with open(os.path.join(os.path.dirname('__file__'), "Data/obfuscated_data_array.json"), 'w') as outfile:
    json.dump(data, outfile)
