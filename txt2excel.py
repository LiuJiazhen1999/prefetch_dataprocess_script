import xlwt
import os

wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('Sheet1') #sheet页第一页
txt_dir = "C:\\Users\\17799\\Desktop\\prefetch\champsim_results\\bimodal-no-no-no-no-lru-1core_results_200M"

#标题行
first_row = ["trace_name", "IPC", "l1d_issued", "l1d_useful", "l1d_useless", "l1d_latency", "l1i_issued", "l1i_useful", "l1i_useless", "l1i_latency", "l2c_issued", "l2c_useful", "l2c_useless", "l2c_latency", "llc_issued", "llc_useful", "llc_useless", "llc_latency"]
for i in range(0, len(first_row)):
    ws.write(0, i, first_row[i])

row_excel = 1  # 行

traces = os.listdir(txt_dir)
for trace in traces:
    trace_name = trace.split("bimodal")[0][:-1]
    ws.write(row_excel, 0, trace_name)

    f = open(txt_dir + '\\' + trace, encoding='utf-8')
    for line in f:
        if "CPU 0 cumulative IPC:" in line:
            line = line.strip('\n')
            contents = line.split()
            ws.write(row_excel, 1, contents[4])
        elif "L1D PREFETCH  REQUESTED" in line:
            line = line.strip('\n')
            contents = line.split()
            ws.write(row_excel, 2, contents[5])
            ws.write(row_excel, 3, contents[7])
            ws.write(row_excel, 4, contents[9])
        elif "L1D AVERAGE MISS LATENCY" in line:
            line = line.strip('\n')
            contents = line.split()
            ws.write(row_excel, 5, contents[4])
        elif "L1I PREFETCH  REQUESTED" in line:
            line = line.strip('\n')
            contents = line.split()
            ws.write(row_excel, 6, contents[5])
            ws.write(row_excel, 7, contents[7])
            ws.write(row_excel, 8, contents[9])
        elif "L1I AVERAGE MISS LATENCY" in line:
            line = line.strip('\n')
            contents = line.split()
            ws.write(row_excel, 9, contents[4])
        elif "L2C PREFETCH  REQUESTED" in line:
            line = line.strip('\n')
            contents = line.split()
            ws.write(row_excel, 10, contents[5])
            ws.write(row_excel, 11, contents[7])
            ws.write(row_excel, 12, contents[9])
        elif "L2C AVERAGE MISS LATENCY" in line:
            line = line.strip('\n')
            contents = line.split()
            ws.write(row_excel, 13, contents[4])
        elif "LLC PREFETCH  REQUESTED" in line:
            line = line.strip('\n')
            contents = line.split()
            ws.write(row_excel, 14, contents[5])
            ws.write(row_excel, 15, contents[7])
            ws.write(row_excel, 16, contents[9])
        elif "LLC AVERAGE MISS LATENCY" in line:
            line = line.strip('\n')
            contents = line.split()
            ws.write(row_excel, 17, contents[4])
        wb.save(txt_dir+'\\'+'result.xls')  # 输出在同一目录
    f.close()
    row_excel += 1