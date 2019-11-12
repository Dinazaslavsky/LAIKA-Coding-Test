import pickle as Pick
import datetime
from openpyxl import Workbook
from openpyxl import styles

#TODO - make set up a function that only happens once
# - set name is code? why sometimes list and sometimes not? could it have multiple names then?
# - account for everything being None and make variables for the data


def main():
    with open('test_data.pkl', 'rb') as f:
        data = Pick.load(f)

    wb = Workbook()
    ws = wb.active

    ws["A1"].value = "Task Name"
    ws["B1"].value = "Set Part"
    ws["C1"].value = "Parent Build"
    ws["D1"].value = "Start Date"
    ws["E1"].value = "End Date"


   # print(data[0])
    #print(data[0]["entity"]["code"][0])
   # print(data[0]["sg_parent_build"]["code"])

    now = datetime.datetime.today()
    i = 2
    for item in data:
        print(item)
        rowNum = str(i)
        ws["A" + rowNum].value = item["content"]
        if isinstance(item["entity"]["code"], list):
            ws["B" + rowNum].value = item["entity"]["code"][0]
        else:
            ws["B" + rowNum].value = item["entity"]["code"]
        if not (item["sg_parent_build"] is None):
            ws["C" + rowNum].value = item["sg_parent_build"]["code"]
        ws["D" + rowNum].value = item["start_date"]
        ws["E" + rowNum].value = item["due_date"]
        #better to get due date from excel or data? probably data
        dueDate = datetime.datetime.strptime(item["due_date"], '%Y-%m-%d')
        if dueDate < now:
            ws[rowNum].fill = styles.fills.PatternFill(fgColor='FF0000', fill_type='solid') #FIXME
        i += 1


    wb.save("projects.xlsx")

if __name__ == '__main__':
    main()