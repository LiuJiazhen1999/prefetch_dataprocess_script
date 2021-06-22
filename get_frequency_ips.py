#用于从打印的日志文件中获取出现频率高的ip集合
import os
#日志文件的路径
file_name = "0615_valuless_pattern.log"

trace_names = os.listdir("./traces_pattern")
for trace_line in trace_names:
    is_start = False
    ips_result = []
    if(".xz" not in trace_line):
        continue
    if("gcc" not in trace_line and "mcf" not in trace_line and "soplex_kenn" not in trace_line and "omnetpp" not in trace_line and "astar_lakes" not in trace_line and "sphinx3" not in trace_line and "xalancbmk" not in trace_line):
        continue
    trace_name = trace_line.split(":")[1].strip()
    print(trace_name)
    read_file = open(file_name, "r+", encoding="utf-8")
    for line in read_file:
        if(trace_name in line and "ERROR" not in line):
            is_start = True
            print(line+"\n")
        if(is_start and "prefetch_num" in line):
            k_v_list = line.split(',')
            percentage = ((k_v_list[2].split(':'))[1]).strip()
            #if(float(percentage) > 0):
            if(True):
                ip_pair = k_v_list[0].split(':')
                ip_value = ip_pair[1].strip()
                ips_result.append(ip_value)
        if(is_start and "valuable_ips" in line):
                break
    read_file.close()

    write_file = open("frequency_ips/" +trace_name + ":frequency_ips.txt", "w+", encoding="utf-8")
    for i in range(0, len(ips_result)):
        write_file.write(ips_result[i]+"\n")
    write_file.close()

