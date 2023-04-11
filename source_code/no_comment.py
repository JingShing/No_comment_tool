def no_one_line_comment(line:str, prefix:str)->str:
    line_list = list(line)
    line_index = line.find(prefix)
    while line_index!=-1:
        while line_list[line_index] != '\n':
            line_list[line_index] = ''
            line_index += 1
            if line_index==len(line_list): # if in the last line has comment need to use this to avoid out of index
                break
        line = "".join(line_list)
        line_list = list(line)
        line_index = line.find(prefix)
    return line

def no_block_comment(line:str, prefix:str, profix:str)->str:
    line_list = list(line)
    pre_index = line.find(prefix)
    pro_index = line.find(profix)
    while pre_index!=-1 and pro_index!=-1:
        while pre_index < pro_index+len(profix):
            line_list[pre_index] = ''
            pre_index += 1
            if pre_index==len(line_list):
                break
        line = "".join(line_list)
        line_list = list(line)
        pre_index = line.find(prefix)
        pro_index = line.find(profix)
    print(pro_index)
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
            file_info['line'] = no_block_comment(file_info['line'], '/*', '*/')
            file_info['line'] = no_one_line_comment(file_info['line'], '//')
            break
        elif method == 'py':
            file_info['line'] = no_block_comment(file_info['line'], '"""', '"""')
            file_info['line'] = no_block_comment(file_info['line'], "'''", "'''")
            file_info['line'] = no_one_line_comment(file_info['line'], '#')
            break
        else:
            print("Which no comment method do you prefer?(c, py)", end='')
            method = input()

    output_file = 'no_comment_' + file_info['name'] + '.txt'
    write_file(output_file, file_info['line'])
