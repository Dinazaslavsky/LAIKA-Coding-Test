#!/usr/bin/env python
import pickle as pick

#task name not defined first
#entity code is not always a list
#parantheses with print.. probably a python version and not actual bug
#didnt account for name being duplicate build

def getItemString(item):
    task_name = "" #added
    if item['content'] == 'design':
        task_name = "Design/Concept"
    elif item['content'] == 'first build':
        task_name = "First Build"
    #addeed
    elif item['content'] == "duplicate build":
        task_name = "Duplicate Build"
    item_string = 'Task Date Change\n'
    item_string += 'Task Name: %s\n' % task_name
    #added
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
        data = pick.load(f)

    email_body = ''
    for item in data:
        item_string = getItemString(item)
        email_body += '%s\n' % item_string

    print(email_body)

if __name__ == '__main__':
    main()
