import csv
import random
import time

x_value = 0
total_1 = 1000
total_2 = 1000

# headers list
fieldnames = ["x_value", "total_1", "total_2"]

# opening and writing our csv
with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    # 'a' mode to append to our newly opened csv file
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        # generating our random values
        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)

    # puts program to sleep for 1 second, so we get data only every second. 
    time.sleep(1)
