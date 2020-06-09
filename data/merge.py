import os

source_dir = "nturgbd_raw/nturgb+d_skeletons"
target_dir = "nturgbd_raw/newnturgbd"

file_list = os.listdir(source_dir)
for file in file_list:
    cmd = "cp "+source_dir+"/"+file+" "+ target_dir
    print(cmd)
    os.system(cmd)