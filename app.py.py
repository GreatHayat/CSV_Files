import csv
import os

def load_csv(path):
    return [file for file in os.listdir(path) if file.endswith(".csv") & os.path.isfile(os.path.join(path, file))]

def read_csv_files(csv_file):
    max_temp = []
    min_temp = []
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            max_temp.append(row['Max'])
            min_temp.append(row['Min'])
        print(f"Max Temp {max(max_temp)} | Min Temp {min(max_temp)} from {csv_file}")
        print(f"Max Temp {max(min_temp)} | Min Temp {min(min_temp)} from {csv_file}")
if __name__ == "__main__":
    csv_files = load_csv(".")
    load_csv_files = []
    for file in csv_files:
        load_csv_files.append(file)

    for csv_file in load_csv_files:
        read_csv_files(csv_file)
