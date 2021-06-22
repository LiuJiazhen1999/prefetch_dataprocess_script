import os

def compile_prefetcher(branch_predicor, l1i_prefetcher, l1d_prefetcher, l2c_prefetcher, llc_prefetcher, llc_replacement, core_num):
    os.system("./build_champsim.sh {} {} {} {} {} {} {}".format(branch_predicor, l1i_prefetcher, l1d_prefetcher, l2c_prefetcher, llc_prefetcher, llc_replacement, core_num))

def get_ip_pattern(trace, prefetcher, n_warm, n_sim, relod_valuable_path):
    os.system("./run_champsim.sh {} {} {} {}".format(prefetcher, n_warm, n_sim, trace))
    print(trace + "执行完毕，开始复制")
    os.system("cp ./pagechange_ip_pattern.txt pagechange_ip_pattern/{}", relod_valuable_path)
    print("复制完毕")

if __name__ == '__main__':
    ip_pattern_file = ""
    trace_dir = "dpc3_traces"
    n_warm = 1
    n_sim = 10
    ip_valuable_analysisor = "bimodal-no-ip_page_change_frequency-no-no-lru-1core"

    # build
    branch_predicor = "bimodal"
    l1i_prefetcher = "no"
    l1d_prefetcher = "ip_page_change_frequency"
    l2c_prefetcher = "no"
    llc_prefetcher = "no"
    llc_replacement = "lru"
    core_num = "1"

    # compile
    print(
        "Start compile {} {} {} {} {} {} {}...".format(branch_predicor, l1i_prefetcher, l1d_prefetcher, l2c_prefetcher,
                                                       llc_prefetcher, llc_replacement, core_num))
    compile_prefetcher(branch_predicor, l1i_prefetcher, l1d_prefetcher, l2c_prefetcher, llc_prefetcher, llc_replacement,
                       core_num)

    # make experiment
    traces = os.listdir(trace_dir)
    for trace in traces:
        print("Start make experiment on {}".format(trace))
        print("Start find valuable ips ...")
        # bimodal-no-ipcp_ip_value-ipcp-ipcp-lru-1core
        get_ip_pattern(trace, ip_valuable_analysisor, n_warm, n_sim, trace+":pagechange_ip_pattern")

