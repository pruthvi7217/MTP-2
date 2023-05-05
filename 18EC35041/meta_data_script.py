from pathlib import Path
from multiprocessing import Pool

def ListCreation(curr_dir, tot_contents):
    for folder in curr_dir.iterdir():
        if(folder.is_dir()):
            for fle in folder.iterdir():
                if(fle.suffix == '.txt'):
                    try:
                        with open(fle) as f:
                            contents = [line.rstrip() for line in f]
                        contents.append([folder.name, fle.name])
                        tot_contents.append(contents)
                    except Exception as e:
                        with open("errors.txt", 'a') as f:
                            f.write(e)
                            f.write("\n")
    return tot_contents


def dictionaryCreation(tot_contents, cls):
    for con in tot_contents:
        Type, value  = con[0].split(':')
        if(value == ' Arch'):
            if(value not in cls.keys()):
                arch_lst = [con[-1]]
                arch_pt = [float(con[1])]
                cls[value] = [arch_lst, arch_pt]
            else:
                cls[value][0].append(con[-1])
                cls[value][1].append(con[1])
        else:
            if(value not in cls.keys()):
                type_lst = [con[-1]]
                loop = []
                delta = []
                for t in con[1:-1]:
                    ld, pst = t.split(':')
                    x,y = pst.split('\t')
                    x = float(x)
                    y = float(y)
                    if ld == 'Loop':
                        loop.append((x, y))
                    else:
                        delta.append((x,y))
                cls[value] = [type_lst, loop, delta]
            else:
                cls[value][0].append(con[-1])
                for t in con[1:-1]:
                    ld, pst = t.split(':')
                    x,y = pst.split('\t')
                    x = float(x)
                    y = float(y)
                    if ld == 'Loop':
                        cls[value][1].append((x, y))
                    else:
                        cls[value][2].append((x,y))


    return cls


if __name__ == "__main__":
    pth = 'Anguli_200k_1M/Meta Info'
    pth = "Anguli_200k_1M"
    print("Hello minutiae")

    
