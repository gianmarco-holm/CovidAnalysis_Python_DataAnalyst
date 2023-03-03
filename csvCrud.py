import csv

def read_csv(path):
  with open(path, 'r') as csvFile:
    file = csv.reader(csvFile, delimiter=',')
    header = next(file)
    data = [dict(zip(header, row)) for row in file]
    return data


def write_csv(path, diccionary):
  with open(path, mode='a', newline='') as csvFile:
    file = csv.writer(csvFile)
    #file.writerow(diccionary[0].keys())
    for row in diccionary:
      file.writerow(row.values())
