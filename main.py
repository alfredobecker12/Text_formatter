import functions

filepath, filename, separator = functions.get_file_path()

with open(filepath + filename, 'r') as f:
    file = f.read()
    f.close()

formated_file = filename + 'formated.txt'
with open(filepath + formated_file, 'a') as f:
    for index, value in enumerate(file):
        if index == 0:
            f.write(value)
            continue
        if file[index-1] == separator:
            f.write('\n' + value)
        f.write(value)
