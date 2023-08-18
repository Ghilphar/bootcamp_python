class CsvReader():
    def __init__(self,  filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.csvLen = 0
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []
        self.header_data = []

    def __enter__(self):
        try:
            #readonly
            self.file = open(self.filename, 'r')
            self.parse_file()
        except FileNotFoundError:
            raise Exception(f'File {self.filename} not found.')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if hasattr(self, 'file'):
            self.file.close()

    def getdata(self):
        return self.data
    
    def getheader(self):
        return self.header_data if self.header else None
    
    def parse_file(self):
        lines = self.file.readlines()
        if self.skip_top > 0:
            lines = lines[self.skip_top:]
        if self.skip_bottom > 0:
            lines = lines[:-self.skip_bottom]

        for index, line in enumerate(lines):
            row = line.strip().split(self.sep)
            new_row = []
            for value in row:
                new_row.append(value.strip())
            if "" in new_row:
                raise Exception(f"Missing value detected. {index + 1}")
            if index == 0:
                self.csvLen = len(new_row)
                if self.header:
                    self.header_data.append(new_row)
                    continue
            if len(new_row) != self.csvLen:
                raise Exception(f"Mismatch between number of fields and number of records in {self.filename}.")

            #if index != 0 and (len(new_row) != self.csvLen):
            self.data.append(new_row)