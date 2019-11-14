# Written by Dina Zaslavsky
# For Challenge 1 of LAIKA Coding Test

# This program creates pickle files that are purposely not as they should be based on the test_data.pkl file

import cPickle as pickle
import copy

# removes values from first and second items in data pickle file
# saves as test_data_values_missing.pkl
def create_missing_data(data):
    missing_data = copy.deepcopy(data)
    missing_data[0]["due_date"] = None
    missing_data[0]["entity"]["code"] = None
    missing_data[1]["entity"] = None
    missing_data[0]["content"] = None
    missing_data[0]["start_date"] = None
    missing_data[0]["sg_parent_build"]["code"] = None
    outfile = open("test_data_values_missing.pkl", 'wb')
    pickle.dump(missing_data, outfile)


# removes keys from first and second items in data pickle file
# saves as test_data_incorrect_key.pkl
def create_incorrect_key(data):
    incorrect_key = copy.deepcopy(data)
    incorrect_key[0].pop("due_date")
    incorrect_key[0]["entity"].pop("code")
    incorrect_key[1].pop("entity")
    incorrect_key[0].pop("content")
    incorrect_key[0].pop("start_date")
    incorrect_key[0]["sg_parent_build"].pop("code")
    incorrect_key[1].pop("sg_parent_build")
    outfile = open("test_data_incorrect_key.pkl", 'wb')
    pickle.dump(incorrect_key, outfile)


# changes values to ints and lists instead of string in first and second items in pickle file
# saves as test_data_unexpected_type.pkl
def create_unexpected_type(data):
    unexpected_type = copy.deepcopy(data)
    unexpected_type[0]['content'] = 456
    unexpected_type[1]['content'] = ["incorrect", "format"]
    unexpected_type[0]['due_date'] = 456
    unexpected_type[1]['due_date'] = ["incorrect", "format"]
    unexpected_type[0]['entity'] = 456
    unexpected_type[0]['start_date'] = 456
    unexpected_type[1]['start_date'] = ["incorrect", "format"]
    unexpected_type[0]['sg_parent_build'] = 456
    unexpected_type[1]['sg_parent_build']['code'] = ["incorrect", "format"]
    outfile = open("test_data_unexpected_type.pkl", 'wb')
    pickle.dump(unexpected_type, outfile)

# reorders some of the data to make it not chronological
# saves as test_data_unordered.pkl
def create_unordered(data):
    unordered = copy.deepcopy(data)
    temp = unordered[0]
    unordered[0] = unordered[1]
    unordered[1] = temp
    temp = unordered[4]
    unordered[4] = unordered[6]
    unordered[6] = temp
    outfile = open("test_data_unordered.pkl", 'wb')
    pickle.dump(unordered, outfile)

def main():

    # open data pickle file
    try:
        with open('test_data.pkl', 'rb') as f:
            data = pickle.load(f)
    except:
        print("ERROR: Test Data Pickle File Not Found or Empty")
        return

    # creates all testing pickle files
    create_missing_data(data)
    create_incorrect_key(data)
    create_unexpected_type(data)
    create_unordered(data)


if __name__ == '__main__':
    main()
