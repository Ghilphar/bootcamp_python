from csvreader import CsvReader
import pprint

if __name__ == "__main__":
    with CsvReader(filename='./bad.csv', header=True, skip_bottom=0, skip_top=0) as file:
        data = file.getdata()
        header = file.getheader()
    
    pprint.pprint(header)
    pprint.pprint(data)