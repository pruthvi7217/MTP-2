from pathlib import Path

def PathCreation(curr_dir):
    i = 0
    cnt = 0
    for folder in curr_dir.iterdir():
        if(folder.is_dir()):
            for fle in folder.iterdir():
                if(fle.suffix == '.txt'):
                    cnt += 1
                    with open("MetaData_file_list.txt", 'a') as f:
                        f.write(str(Path(fle).absolute()))
                        f.write('\n')
        
    
    # for fle in curr_dir.iterdir():
    #     if fle.suffix == '.txt':
    #         i += 1
    #         with open("MetaData_file_list.txt", 'a') as f:
    #             f.write(str(Path(fle).absolute()))
    #             f.write('\n')
    #     if(i%10 == 0):
    #         cnt += 1
    #         print("#",end="")
    print()
    print(cnt)

if __name__ == "__main__":
    meta_info_path = Path(r"Anguli_200k_1M/Meta Info")
    PathCreation(meta_info_path)
    print(Path.cwd())
    print(Path.home())