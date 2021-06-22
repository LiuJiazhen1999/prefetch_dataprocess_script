import os
from coverage_count import get_coverage

pattern_dir = "pagechange_ip_pattern/"
write_path = "coverage_result.txt"


def get_list(file_path, is_classify):
    read_file = open(file_path, "r+", encoding="utf-8")
    result_list = []
    sub_list = []
    if(is_classify):
        for line in read_file:
            if("ip_value" in line):
                sub_list.clear()
            elif("ip_end" in line):
                result_list.append(sub_list)
            else:
                sub_list.append(line.strip())
    else:
        for line in read_file:
            if ("ip_value" in line):
                continue
            elif ("ip_end" in line):
                continue
            else:
                sub_list.append(line.strip())
        result_list.append(sub_list)
    read_file.close()
    return result_list

write_file = open(write_path, "w+", encoding = "utf-8")
write_file.write("trace_name".rjust(20, " "))
write_file.write("ip_classify_coverage".rjust(20, " "))
write_file.write("ip_noclassify_coverage".rjust(20, " "))
write_file.write("\n")

file_names = os.listdir(pattern_dir)
for file_name in file_names:
    file_size = os.path.getsize(pattern_dir + file_name)#获取文件大小
    if file_size == 0:
        continue
    write_file.write(file_name.rjust(20, " "))
    cover_num = 0
    total_num = 0
    #ip分类的情况统计
    result_list = get_list(pattern_dir + file_name, True)
    for sub_list in result_list:
        cover_num += get_coverage(sub_list)
        total_num += len(sub_list)
    write_file.write(str(cover_num/total_num).rjust(20, " "))
    #ip不分类的情况统计
    result_list = get_list(pattern_dir + file_name, False)
    for sub_list in result_list:
        cover_num += get_coverage(sub_list)
        total_num += len(sub_list)
    write_file.write(str(cover_num / total_num).rjust(20, " "))
    write_file.write("\n")
write_file.close()