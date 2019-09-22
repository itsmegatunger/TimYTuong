import csv
import traceback

def writingToFile(self, ideas):
    try:
        filename = self.nameFile
        with open(filename, 'a') as f:
            w = csv.DictWriter(f, self.fieldsname)
            for idea in ideas:
                w.writerow(idea)
    except Exception:
        print('Error occurred while writing file!')
        print(traceback.format_exc())