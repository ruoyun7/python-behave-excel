import configparser
import os
import xlrd
import json

# #row,col获取哪行那列的值
# def run_select_shool(row=1,col=1):
#     #打开excel文件读取数据
#     data = xlrd.open_workbook(filename)
#     table = data.sheet_by_index(0)
#
#     row = row-1
#     col = col-1
#     #获取整行整列的值
#     nrows = table.row_values(row)
#     ncols = table.col_values(0)
#     print(nrows[col])

def run_select_school2(filename,sheet_index=0,table_header_row=0):
    # 打开excel文件读取数据
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(sheet_index)
    nrows = table.nrows
    nclos = table.ncols

    #获取表头行的信息，为一个列表
    header_row_data = table.row_values(table_header_row)
    #将每行的信息放入一个字典，再将字典放入一个列表中
    list = []
    for rownum in range(1,nrows):
        rowdata = table.row_values(rownum)
        #如果rowdata有值，
        if rowdata:
            dict = {}
            for j in range(0,len(header_row_data)):
             #将excel中的数据分别设置成键值对的形式，放入字典，如‘标题’：‘name’；
                dict[header_row_data[j]] = rowdata[j]
            list.append(dict)
    # print(list)
    return list
def get_excle(num,str,filename):
    result= run_select_school2(filename)
    if num < len(result):
        for i in range(0,len(result)):
            if i==num:
                rows=result[i]
                # print("\n每行结果",rows)
                for key,value in rows.items():
                    if key==str:
                        # print("\n每个字段",value)
                        return value
                    else:
                        pass
            else:
                pass
    else:
        return "超过excel行数！"

def excute_excel(str,filename):
    result= run_select_school2(filename)
    for i in range(0,len(result)):
        rows=result[i]
        for key,value in rows.items():
            if key==str:
                print("\n每个字段",value)
                return value
            else:
                pass



if __name__ == '__main__':
   case= get_excle(1,"testId","E:\\test\\test_xietong\data\\test2.xlsx")
   print("\n值",case)
