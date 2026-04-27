import glob

def main():
    
    print("Testing")
    # for name in glob.glob('Data/Data?.txt','', root_dir=None, dir_fd=None, recursive=False):
    #     print(name)
    for f in glob.glob("Data/Data*.txt"):
        print(f)
        with open(f) as stringArray:
            print(stringArray.read())
    return

main()
   