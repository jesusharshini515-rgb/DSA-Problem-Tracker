import csv

FILE_NAME = "dsa_problems.csv"

def add_problem():
    name = input("Problem Name: ")
    topic = input("Topic (Array/String/etc): ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, topic, difficulty])

    print("Problem added successfully.\n")

def view_problems():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            print("\nProblem Name | Topic | Difficulty")
            print("---------------------------------")
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No records found.\n")

def main():
    while True:
        print("\n--- DSA Problem Tracker ---")
        print("1. Add Problem")
        print("2. View Problems")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_problem()
        elif choice == '2':
            view_problems()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
