import os

pre_ips_dir = "fre_pc_ips/"
ips_pattern_file_pre = "valuless:"
write_file_dir = "fre_pc_pattern/"
pre_ips = []
filt_ips = []

pre_ips_files = os.listdir(pre_ips_dir)
for pre_ips_line in pre_ips_files:
    trace_name = pre_ips_line.split(":")[0].strip()
    pre_ips_file = pre_ips_dir + pre_ips_line
    read_file = open(pre_ips_file, "r+", encoding = "utf-8")
    for line in read_file:
        pre_ips.append(line.strip())
    read_file.close()

    write_file = open(write_file_dir + trace_name + ":ips_pattern.txt", "w+", encoding = "utf-8")

    for pre_ip in pre_ips:
        read_file = open(ips_pattern_file_pre + trace_name, "r+", encoding = "utf-8")
        is_start = False
        write_file.write("ip_value:" + pre_ip +"\n")
        for line in read_file:
            if("ip" in line and pre_ip in line and "valuless" not in line):
                is_start = True
            elif(is_start and ("addr" in line)):
                line_list = line.split()
                addr = line_list[2].strip()
                write_file.write("    addr_value:" + addr + "\n")
            elif(is_start and ("page" not in line)):
                break
        read_file.close()
    write_file.close()
    pre_ips.clear()
    filt_ips.clear()