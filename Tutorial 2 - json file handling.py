import json
import os

# create a sample json  file
if(not(os.path.isfile("json_sample.json"))):
    # create some JSON:
    data =  '{ "name":"Tom", "age":33, "city":"New York"}'

    with open("json_sample.json", "w") as write_file:
        json.dump(data, write_file)
    
    print("New sample json file created....!")
    
# if sample json file found read it & edit it
else:
    # load JSON file:
    with open("json_sample.json", "r") as read_file:
        json_data = json.load(read_file)

    # parse json_data to python dictionary:
    pythonDictionary = json.loads(json_data)
    
    # print json file content
    print(json_data)
    
    # print python dictonary
    print(pythonDictionary)
    
    # specifically access object of json file
    print(pythonDictionary['city'])

    # edit python dictonary
    pythonDictionary['city'] = 'London'
    
    # phrase python to json
    dictionaryToJson = json.dumps(pythonDictionary)
    
    with open("json_sample.json", "w") as write_file:
        json.dump(dictionaryToJson, write_file)
        
    print("Sample json file edited....!")
