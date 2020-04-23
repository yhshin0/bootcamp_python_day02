class CsvReader():
    def __init__(self, file_name, sep=',',
                 header=False, skip_top=0, skip_bottom=0):
        if not isinstance(file_name, str):
            raise Exception("file_name is not string.")
        else:
            self.file_name = file_name
        if not isinstance(sep, str):
            raise Exception("sep is not string.")
        else:
            self.sep = sep
        if not isinstance(header, bool):
            raise Exception("header is not boolean.")
        else:
            self.header = header
        if not isinstance(skip_top, int):
            raise Exception("skip_top is not integer.")
        else:
            self.skip_top = skip_top
        if not isinstance(skip_bottom, int):
            raise Exception("skip_bottom is not integer.")
        else:
            self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.file = open(self.file_name, 'r')
        except FileNotFoundError:
            raise
        temp = list(map(lambda x: x.strip('\n'), self.file.readlines()))
        idx = 0
        self.header_list = None
        self.data = []
        if self.header is True:
            self.header_list = list(map(
                lambda x: x.strip().strip('"').strip("'"),
                temp[idx].split(self.sep)))
            idx += self.skip_top + 1
        else:
            idx += self.skip_top
            self.header_list = list(map(
                lambda x: x.strip().strip('"').strip('"'),
                temp[idx].split(self.sep)))
            idx += 1
        if '' in self.header_list:
            raise Exception("The file is corrupted! Check {}'s the header."
                            .format(self.file_name))
        for i in range(idx, len(temp) - self.skip_bottom):
            line = list(filter(
                lambda x: x != '',
                list(map(
                    lambda x: x.strip().strip('"').strip("'"),
                    temp[i].split(self.sep)))))
            if len(line) != len(self.header_list):
                raise Exception("The file is corrupted! Check {}'s the line {}"
                                .format(self.file_name, i))
            temp_dic = dict()
            for i in range(len(line)):
                if line[i].isdigit():
                    temp_dic[self.header_list[i]] = int(line[i])
                else:
                    temp_dic[self.header_list[i]] = str(line[i])
            self.data.append(temp_dic)
            del line
            del temp_dic
        del temp
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file is not None:
            self.file.close()

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header_list
