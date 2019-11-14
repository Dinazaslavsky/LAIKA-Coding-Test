#!/usr/bin/env python
import cPickle as pickle

# Bug 1: task_name was not defined before the if/elif statement meaning that if neither if statement applies, task_name
# won't have a value and therefore will cause an error when the program tries to add it to the item_string. To fix this
# I assigned task_name an empty string.

# Bug 2: The program checks if the task name is design or first build but the test_data pickle file contains a third
# option, which is duplicate build. With the bug 1 fix, the email body would contain an empty string, when it should say
# duplicate build. To fix this, I added another elif statement.

# Bug 3: Link, which is taken from the code in entity is originally expected to always be a list but in one case in
# the test_data.pkl file it is just a string and thus when the 0th index of it is taken, it outputs just the first
# letter of the full string so instead of outputting Test Prop 2, it outputs just T. To fix this, I check if it's a
# list and if so, I take the first value. Otherwise, I just output the whole string. In this case I am not accounting
# for if there are multiple values in the list and if the user wants to output all of them.

# Other issues: I noticed that all the names for items stayed the same as challenge 1 (Task Name, Parent Build, etc)
# except for Set Part, which changed to Link. I'm not sure if this was meant to be one of the bugs but I just wanted
# to mention that and if it was, then to fix it, I would change the string from "Link: %s\n" to "Set Part: %s\n".
# There are also issues in terms of the program not accounting for the test_data.pkl file to have all the data
# and formatted as expected. One of the biggest issue is the program doesn't have any way to account for if the
# test_data.pkl file doesn't exist.


def getItemString(item):
    task_name = ""   # Bug 1 fixed here
    if item['content'] == 'design':
        task_name = "Design/Concept"
    elif item['content'] == 'first build':
        task_name = "First Build"
    # Bug 2 fixed here
    elif item['content'] == "duplicate build":
        task_name = "Duplicate Build"
    item_string = 'Task Date Change\n'
    item_string += 'Task Name: %s\n' % task_name
    # Bug 3 fixed here
    if isinstance(item["entity"]["code"], list):
        item_string += 'Link: %s\n' % item['entity']['code'][0]
    else:
        item_string += 'Link: %s\n' % item['entity']['code']
    item_string += 'Parent Build: %s\n' % item['sg_parent_build']['code'] if item['sg_parent_build'] else ''
    item_string += 'Start: %s\n' % item['start_date']
    item_string += 'End: %s\n' % item['due_date']
    return item_string


def main():
    with open('test_data.pkl', 'rb') as f:
        data = pickle.load(f)

    email_body = ''
    for item in data:
        item_string = getItemString(item)
        email_body += '%s\n' % item_string

    print email_body


if __name__ == '__main__':
    main()
