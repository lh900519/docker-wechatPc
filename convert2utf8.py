import os
import chardet
import codecs


def WriteFile(filePath, u, encoding="utf-8"):
    with codecs.open(filePath, "w", encoding) as f:
        f.write(u)


def GBK_2_UTF8(src, dst):
    #     检测编码，coding可能检测不到编码，有异常
    f = open(src, "rb")
    coding = chardet.detect(f.read())["encoding"]
    f.close()
    if coding != "utf-8" and coding != "ascii": # 同时忽略 ascii 
        with codecs.open(src, "r", coding) as f:
            try:
                WriteFile(dst, f.read(), encoding="utf-8")
                try:
                    print(src + "  " + coding + " to utf-8  converted!")
                except Exception:
                    print("print error")
            except Exception:
                print(src +"  "+ coding+ "  read error")

# 把目录中的 *.h & *.cpp 编码由gbk转换为utf-8
def ReadDirectoryFile(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        for dirname in dirnames:
          	#递归函数，遍历所有子文件夹
            ReadDirectoryFile(dirname)
        for filename in filenames:
            if filename.endswith(".cpp") or filename.endswith(".h"):
                GBK_2_UTF8(os.path.join(parent, filename),
                           os.path.join(parent, filename))

if __name__ == "__main__":
    src_path = "WechatDll/WechatDll"
    ReadDirectoryFile(src_path)
    src_path = "WechatRobot/WechatRobot"
    ReadDirectoryFile(src_path)
    print("All done!")
