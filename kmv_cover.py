import os
ips_pattern_file_dir = "fre_pc_pattern/"
write_dir = "kmv_cover/"

def get_addr_str(addr1, addr2):
    return str(addr1 + "_" + addr2)

def get_addr_pair(addr):
    return addr.split("_")

threshold = 0.005

chain_dict = dict()
pattern_list = []
pre_addr = ""
cur_addr = ""
storeNum = 0
all_line = 0
useful_line = 0
pre_key_list = []

ips_pattern_files = os.listdir(ips_pattern_file_dir)
for ips_pattern_file in ips_pattern_files:
    trace_name = ips_pattern_file.split(":")[0].strip()
    ips_pattern_file_name = ips_pattern_file_dir +  ips_pattern_file
    if not os.path.getsize(ips_pattern_file_name):
        continue

    write_file = open(write_dir + trace_name + ":coverage_info.txt", "w+", encoding = "utf-8")
    read_file = open(ips_pattern_file_name, "r+", encoding="utf-8")
    for line in read_file:
        if("ip_value" in line):
            sumNum = 0
            if(len(pattern_list) != 0):
                sort_kv_list = sorted(chain_dict.items(), key = lambda kv : (kv[1], kv[0]), reverse = True)
                pre_key_list.clear()
                for i in range(0, len(sort_kv_list)):
                    countNum = 0
                    addr_str = sort_kv_list[i][0]
                    addr_pair = get_addr_pair(addr_str)
                    #if(addr_pair[0] in pre_key_list):
                    #    continue
                    #pre_key_list.append(addr_pair[0])
                    for j in range(0, len(pattern_list)-1):
                        if(pattern_list[j][0] == addr_pair[0] and pattern_list[j+1][0] == addr_pair[1]):
                            countNum = countNum + 2 - pattern_list[j][1] - pattern_list[j+1][1]
                            pattern_list[j][1] = 1
                            pattern_list[j+1][1] = 1
                    if(countNum/len(pattern_list) < threshold):
                        break
                    write_file.write(str(countNum/len(pattern_list)))
                    write_file.write("\n")
                    storeNum += 1
                    sumNum += countNum
                write_file.write(str(sumNum/len(pattern_list)))
                write_file.write("\n")
                useful_line += sumNum
            write_file.write(line + "\n")
            chain_dict.clear()
            pattern_list.clear()
            pre_addr = ""
        else:
            all_line += 1
            line_list = line.split(":")
            cur_addr = line_list[1].strip()
            pattern_list.append([cur_addr, 0])
            if(pre_addr != ""):
                if(get_addr_str(pre_addr, cur_addr) in chain_dict):
                    chain_dict[get_addr_str(pre_addr, cur_addr)] += 1
                else:
                    chain_dict[get_addr_str(pre_addr, cur_addr)] = 1
            pre_addr = cur_addr

    sumNum = 0
    sort_kv_list = sorted(chain_dict.items(), key = lambda kv : (kv[1], kv[0]), reverse = True)
    pre_key_list.clear()
    for i in range(0, len(sort_kv_list)):
        countNum = 0
        addr_str = sort_kv_list[i][0]
        addr_pair = get_addr_pair(addr_str)
        #if(addr_pair[0] in pre_key_list):
        #    continue
        #pre_key_list.append(addr_pair[0])
        for j in range(0, len(pattern_list)-1):
            if(pattern_list[j][0] == addr_pair[0] and pattern_list[j+1][0] == addr_pair[1]):
                countNum = countNum + 2 - pattern_list[j][1] - pattern_list[j+1][1]
                pattern_list[j][1] = 1
                pattern_list[j+1][1] = 1
        if(countNum/len(pattern_list) < threshold):
            break
        write_file.write(str(countNum/len(pattern_list)))
        write_file.write("\n")
        storeNum += 1
        sumNum += countNum
    write_file.write(str(sumNum/len(pattern_list)))
    write_file.write("\n")
    useful_line += sumNum
    write_file.write("coverage:")
    write_file.write(str(useful_line/all_line))
    write_file.write("\n")
    write_file.write("storeNum:")
    write_file.write(str(storeNum))
    write_file.write("\n")
    write_file.close()
    chain_dict.clear()
    pattern_list.clear()
    pre_addr = ""
    cru_addr = ""
    storeNum = 0
    all_line = 0
    useful_line = 0