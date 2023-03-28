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

    # txt 원본 파일의 경로
    path_dir_txt = 'D:\\backup\JSON2YOLO\\new_dir\labels' + '\\' + all_dir_name
    # txt 복사 파일의 경로
    move_path_dir_txt = 'D:\\backup\JSON2YOLO\\new_dir\labels' + '\\' + all_dir_name
    # jpg 원본 파일의 경로
    path_dir_jpg = 'D:\\backup\\trash-data_dataset' + '\\' + all_dir_name
    # jpg 복사 파일의 경로
    move_path_dir_jpg = 'D:\\backup\JSON2YOLO\\new_dir\images' + '\\' + all_dir_name

    txt_list = os.listdir(path_dir_txt)  # txt 파일 리스트
    jpg_list = os.listdir(path_dir_jpg)  # jpg 파일 리스트


    # loop 를 돌면서 txt 파일명과 jpg 파일명 확인
    for item in jpg_list:
        for list in txt_list:
            if item[:4] == list[:4]:
                # 원본경로 + 파일이름 , 옮길 경로 + 파일이름
                # shutil.copy(path_dir_jpg + '\\' + item, move_path_dir_jpg + '\\' + number + '_' + item)
                shutil.copy(path_dir_txt + '\\' + list, 'D:\\aaa'+ '\\' + all_dir_name + '\\' + number + '_' + list)
                # shutil.move(path_dir_txt + '\\' + list, 'D:\\aaa'+ '\\' )