# ćwiczenie 8
class FileManager:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        try:
            sample_file = open(self.file_name, 'r', encoding='utf-8')
            return sample_file.read()
        except IOError:
            raise Exception("Error while reading file!")

    def update_file(self, text_data):
        try:
            open_file = open(self.file_name, 'a', encoding='utf-8')
            open_file.write(text_data)
            open_file.close()
        except IOError:
            raise Exception("Error while updating file!")