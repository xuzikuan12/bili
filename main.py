import sys
import os
from urllib import error

work_path = r"D:\Program Files\bili_1.2.6.36"
storage_path = r"C:\Users\xuzik\OneDrive - mail.ustc.edu.cn\Backup\bilibili\C4\Live\\"


def main(fill=""):
    os.chdir(work_path)
    if fill == "":
        start_value = "start.exe"
    else:
        if os.path.exists("%s.txt" % fill):
            start_value = r"start.exe<%s.txt" % fill
        else:
            print("fill file %s.txt not exist." % fill)
            return
    while True:
        os.chdir(work_path)
        result_start = os.system(start_value)
        if result_start == 0:
            print("recording is normally finished.")
        else:
            print(result_start)
            print("recording is interrupted.")
            print("normally, recording will be restarted soon.")
        flv_handle();

def flv_handle():
    os.chdir(work_path + r"\download")
    for file in os.listdir():
        print(file)
    print("%s file(s) total." % len(os.listdir()))

    flv_files_success = []
    flv_files_fail = []
    for file in os.listdir():
        if file[-4:] == ".flv":
            filename = file[:-4]
            result_ffmpeg = os.system('ffmpeg -i "%s" -vcodec copy -acodec copy "%s.mp4"' % (file, filename))
            if result_ffmpeg == 0:
                print("reverting is normally completed.")
                result_copy_del = os.system(r'cp "%s.mp4" "%s" && del "%s" && del "%s.mp4"' % (filename, storage_path, file, filename))
                flv_files_success.append(file)
            else:
                print("reverting is failed. something must happened.")
                print("relax! the cp and del were not executed.")
                flv_files_fail.append(file)

    for file in flv_files_success:
        print(file)
    print("%s file(s) success." % len(flv_files_success))
    for file in flv_files_fail:
        print(file)
    print("%s file(s) fail." % len(flv_files_success))
    
if __name__ == "__main__":
    argv = sys.argv[1] if len(sys.argv) == 2 else ""
    if argv == 'handle':
        flv_handle()
    else:
        main(argv)
