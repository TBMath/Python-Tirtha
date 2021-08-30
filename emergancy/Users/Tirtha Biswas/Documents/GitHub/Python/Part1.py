import csv
with open("flower.csv", "w") as csv_file:
    file_write = csv.writer(csv_file)
    file_write.writerow(["types", "flowers"])
    file_write.writerow(["Blue flower", 0.5])
    file_write.writerow(["Yellow flower", 25])
    file_write.writerow(["Pink flower", 25])