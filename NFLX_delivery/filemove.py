import os
import subprocess
import pandas as pd

# A : 옮길폴더 이름 (에피소드)
# K : 옮길파일 이름
# L : 옮길 폴더이름 2 (exr, mask, mov)
# .mov 발라내는 정규표현식 : ^(.*?)\.

# 입력값 설정
source_path = '/Volumes/SH2/post/plate/plate/_S2/_SRC/230526_RE'
# source_path = '/Volumes/SH2/delivery/_check/230628_delivery/exr'
deliver_path = '/Volumes/SH2/post/plate/plate/_S2/_SRC/move'
# deliver_path = '/Volumes/SH2/delivery'
excel_file = '/Users/yeonsuseo/Desktop/tttttt.xlsx'
# excel_file = 'path/to/excel/file.xlsx'

# 엑셀 파일 로드
df = pd.read_excel(excel_file, usecols=[0,10,11])

# 각 행을 반복하며 폴더 이동 작업 수행
for column_name, item in df.iterrows() :

    folder_name = str(df.loc[column_name].values[0]) #A열 : 에피소드 (test1)
    origin_folder = str(df.loc[column_name].values[1]) #K열 : 파일이름
    sub_folder = str(df.loc[column_name].values[2]) #J열 : 서브폴더 이름

    if sub_folder == "MOV" :
        origin_folder = origin_folder + '.mov'

    new_source_path= os.path.join(source_path,sub_folder,origin_folder)
    sub_destination_path = os.path.join(deliver_path, folder_name, sub_folder)
    destination_path = os.path.join(deliver_path, folder_name, sub_folder, origin_folder)

    if os.path.exists(new_source_path):

        if not os.path.exists(sub_destination_path):
            os.makedirs(sub_destination_path)

        subprocess.run(["mv", new_source_path, destination_path])
        print(f"[SUCCESS] : {origin_folder}")

    else :
        print(f"[FAILED] : {origin_folder} -> No Such File/Directory")
