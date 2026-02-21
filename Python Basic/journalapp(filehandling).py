from datetime import datetime

def add_entries():
    entry = input("Enter your journal entry - ")
    timestamp = datetime.now().strftime('%Y-%m-%D %H-%M-%S')
    with open('journal.txt', 'a') as file:
        file.write(f'[{timestamp}] {entry}\n')


def view_entries():
    try:
        with open("journal.txt", "r") as file:
            content = file.read()
            print("\nYour Journal Entries:")
            print(content)
    except FileNotFoundError:
        print("No journal entries found yet.")


while True:
    print("ADD ENTRIES")
    print("View Entries")
    print("Exit")

    choose = input("Choose your option - ")
    if choose == "1":
        add_entries()
    elif choose == "2":
        view_entries()
    elif choose =="3":
        break
    else:
        print("Invalid option")


import json

data = {"name": "adnan", "score": 95}

with open('data.json', 'w') as file:
    json.dump(data, file)

with open('data.json', 'r') as file:
    jsonfile = json.load(file)
    print(jsonfile.get("name"))
