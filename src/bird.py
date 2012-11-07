import csv


def get_data(fileString):
    file = open(fileString)
    heading=file.readline()
    newfile = file.readlines()
    file.close()

    writer = csv.writer(open("../data.csv", "a"))

    for line in newfile:
        all_line=line.split()

        writer.writerow([(' '.join(all_line[0:-2])), ' '.join(all_line[-2:]), ''.join(heading)])


for i in range(1):
    get_data('../list'+str(i+1)+'.txt')
