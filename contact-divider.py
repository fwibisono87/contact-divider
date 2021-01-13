import csv
import random
import os
import glob

manager_name_index = 1 ##change this if you need to alter the manager name index

print("welcome to")
print("fwibisono's contact divider!")
print("to input your data, please modify the contacts.csv and managers.csv in the data directory! ")
input("press enter to continue")
print("="*80)
print("choose an option")
print("enter 1 to start processing")
print("enter 2 to open data folder")
print("enter 3 to purge output and start processing")
print("enter 0 to exit")
control = input(">>")


if control == "1":
    pass
    print("="*80)
elif control == "2":
    input("Program will now exit, and open the data folder. Press enter to continue.")
    path = os.path.realpath("data")
    os.startfile(path)
    quit()
elif control == "3":
    input("Program will now purge output folder from csv files. Press enter to continue.")
    try:
        path = os.path.realpath("data/output")
        files = glob.glob(path)
        for f in files:
            os.remove(f)
        input("Program has finished the purge. Press enter to begin processing.")
    except PermissionError:
        print("Program is unable to purge output folder. Please run in administrator or remove files manually.")
        input("To enforce data integrity, program will exit. Please enter to continue")
        quit()
elif control == "0":
    quit()
contactsList = []
managersList = []
pathList = []
contactHeader = []
with open('data/managers.csv') as managers:
    managersreader = csv.reader(managers)
    for row in managersreader:
        managersList.append(row[1])
with open('data/contacts.csv') as contacts:
    contactsreader = csv.reader(contacts)
    for row in contactsreader:
        contactsList.append(row)

contactHeader = contactsList.pop(0)
managerHeader = managersList.pop(0)

print("Detected %d managers" % len(managersList))
print("Detected %d contacts" % len(contactsList))
contacts_per_managers = len(contactsList)//len(managersList)
print("="*80)

for panit in managersList:
    print("now processing for %s" % panit)
    current_contactslist = []
    for i in range(contacts_per_managers):
        secret_number = random.randint(0, len(contactsList)-1)
        current_contactslist.append(contactsList[secret_number])
        del contactsList[secret_number]
    print("your contacts are %s " % current_contactslist)
    filename = "data/output/"+panit
    filename_csv = filename +".csv"
    pathList.append(filename)
    with open(filename_csv, 'w', newline="") as current_file:
        current_writer = csv.writer(current_file)
        current_writer.writerow(contactHeader)
        for data in current_contactslist:
            current_writer.writerow(data)

if contactsList:
    print("there are reminders")
    with open ('data/output/reminder.csv', 'w', newline="") as sisa:
        sisa_writer = csv.writer(sisa)
        for contacts in contactsList:
            print(contacts)
            sisa_writer.writerow(contacts)

input("Program will now exit and open the output folder. Press enter to continue.")
path = os.path.realpath("data/output")
os.startfile(path)
quit()
