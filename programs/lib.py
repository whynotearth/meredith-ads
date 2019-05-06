class File:
    def write(self, filename, content):
        file = open(filename, "w")
        file.write(content + "\n")
        file.close()

    def append(self, filename, content):
        file = open(filename, "a")
        file.write(content.encode("utf-8") + "\n")
        file.close()

    def readLines(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        return lines

    def read(self, filename):
        file = open(filename, 'r')
        content = file.read()
        file.close()
        return content

    def toArray(self, filename):
        array = []
        for line in self.readLines(filename):
            formattedLine = line.rstrip()
            if formattedLine != '':
                array.append(formattedLine)
        return array
