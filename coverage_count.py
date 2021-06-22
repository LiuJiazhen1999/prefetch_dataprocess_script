def get_addr_str(addr1, addr2):
    return str(addr1 + "_" + addr2)

def get_addr_pair(addr):
    return addr.split("_")

def get_coverage(list):#计算一个k对应一个v的覆盖率
    chain_dict = dict()
    pre_key_list = [] #一个key对应一个value，记录此前统计过的key集合
    for i in range(0, len(list) - 1):#遍历数组，填充dict
        if (get_addr_str(list[i][0], list[i+1][0]) in chain_dict):
            chain_dict[get_addr_str(list[i][0], list[i+1][0])] += 1
        else:
            chain_dict[get_addr_str(list[i][0], list[i+1][0])] = 0
    #对dict按照value降序排列
    sort_kv_list = sorted(chain_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    #遍历降序的kv集合，计算覆盖率
    for i in range(0, len(sort_kv_list)):
        addr_pair_str = sort_kv_list[i]
        addr_pair = get_addr_pair(addr_pair_str)
        if(chain_dict[addr_pair_str] < 2):
            break
        if(addr_pair[0] in pre_key_list):#一个key只能有一个value
            continue
        pre_key_list.append(addr_pair[0])
        for j in range(0, len(list)-1):
            if(list[j][0] == addr_pair[0] and list[j+1][0] == addr_pair[1]):
                list[j][1] = 1
                list[j+1][1] = 1
    count = 0
    for i in range(0, len(list)):
        count += list[i][1]
    return count
