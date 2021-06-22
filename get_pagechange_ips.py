import os

pre_ips_dir = "frequency_ips/"
ips_pattern_file_pre = "traces_pattern/valuless:"
write_file_dir = "fre_pc_ips/"
pre_ips = []
filt_ips = []

pre_ips_files = os.listdir(pre_ips_dir)
for pre_ips_line in pre_ips_files:
    trace_name = pre_ips_line.split(":")[0].strip()
    pre_ips_file = pre_ips_dir + pre_ips_line
    read_file = open(pre_ips_file, "r+", encoding = "utf-8")
    for read_file_line in read_file:
        pre_ips.append(read_file_line.strip())
    read_file.close()
    for pre_ip in pre_ips:
        read_file = open(ips_pattern_file_pre + trace_name, "r+", encoding = "utf-8")
        print(ips_pattern_file_pre + trace_name)
        is_start = False
        pre_page = ""
        total_num = 0
        change_num = 0
        for line in read_file:
            if("ip" in line and pre_ip in line and "valuless" not in line):
                is_start = True
            elif(is_start and ("page" in line)):
                total_num += 1
                line_list = line.split()
                cur_page = line_list[5].strip()
                if(cur_page != pre_page):
                    change_num +=1
                pre_page = cur_page
            elif(is_start and ("page" not in line)):
                break
        if(change_num > total_num/2):
            filt_ips.append(pre_ip)
        elif(total_num == 0):
            print(pre_ip)
        else:
            print(change_num/total_num)
        read_file.close()
    write_file = open(write_file_dir + trace_name + ":pagechange_ips.txt", "w+", encoding = "utf-8")
    for filt_ip in filt_ips:
        write_file.write(filt_ip + "\n")
    write_file.close()

    pre_ips.clear()
    filt_ips.clear()