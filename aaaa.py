import os
import shutil

for i in range(1, 45):
    s = i
    if (s < 10):
        number = '0' + str(s)
        all_dir_name = 'data' + number

    else:
        number = str(s)
        all_dir_name = 'data' + number

    path_dir_txt = 'D:\\backup\JSON2YOLO\\new_dir\labels' + '\\' + all_dir_name

    txt_list = os.listdir(path_dir_txt)  # txt 파일 리스트
    # list_length=len(txt_list)
    # ind=list_length//2

    # txt_list.sort()
    # print(txt_list)
    # temp_list=txt_list[0:ind]
    
    for list in txt_list:
        shutil.copy(path_dir_txt + '\\' + list, 'D:\\aaa'+ '\\' + all_dir_name + '\\' + number + '_' + list)

    #print(temp_list)