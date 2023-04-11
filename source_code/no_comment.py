def no_c_comment(line):
    last_char = ''
    flag = False
    line = list(line)
    for index in range(len(line)):
        char = line[index]
        if char == '\n':
            flag = False
        if flag:
            line[index] = ''
        if char == '/' and last_char == '/':
            line[index] = ''
            line[index-1] = ''
            flag = True
        last_char = char
    line = "".join(line)
    return line

def no_python_comment(line):
    flag = False
    line = list(line)
    for index in range(len(line)):
        char = line[index]
        if char == '\n':
            flag = False
        if flag:
            line[index] = ''
        if char == '#':
            line[index] = ''
            flag = True
    line = "".join(line)
    return line

def read_file(file_path):
    file_path = file_path.replace("\\", "/")
    file_format = file_path.split('.')[-1]
    file_name = file_path.split('.')[0].split("/")[-1]

    f = open(file_path, 'r', encoding="utf-8") # avoid cp950 error
    line = f.read()
    f.close()
    file_info = {'line':line, 'format': file_format, 'name': file_name}
    return file_info

def write_file(file_path, line):
    f = open(file_path, "w", encoding="utf-8")
    f.write(line)
    f.close()

if __name__ == "__main__":
    file_path = input()
    file_info = read_file(file_path)
    method = file_info['format']
    while(1):
        if method == 'c':
            file_info['line'] = no_c_comment(file_info['line'])
            break
        elif method == 'py':
            file_info['line'] = no_python_comment(file_info['line'])
            break
        else:
            print("Which no comment method do you prefer?(c, py)", end='')
            method = input()

    output_file = 'no_comment_' + file_info['name'] + '.txt'
    write_file(output_file, file_info['line'])
    
