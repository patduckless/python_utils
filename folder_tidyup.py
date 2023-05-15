import os, shutil

def main(folder="./"):
    os.chdir(folder)
    files = os.listdir("./")
    for item in files:
        if os.path.isdir(folder + item):
            print("skipping: ", item)
            continue
        point = item.rfind(".")
        filetype = item[(point+1):]
        space = 60 - len(item)
        print(item, " "*space, " filetype: ", filetype)
        if os.path.exists(folder + filetype) == False:
            os.mkdir(filetype)
        srcFldr = folder + item
        dstFldr = folder + "\\" + filetype + "\\" + item
        shutil.move(srcFldr, dstFldr)

if __name__ == "__main__":
    print("Running...")
    main()
