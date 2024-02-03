import subprocess


"""
config.txt structure:
0 line: number of neurons on every layer
1 line: activate function (1 - sigmoid; 2 - modRELu; 3 - th)
2 line: using mode (0 - using from console; 1 - using from file; 2 - learning from datafile)
"""
file = open("config.txt")
readfile = file.readlines()
file.close()

cfg = readfile[0].split()
cfg.append(readfile[1])  # adding function number in the end
match readfile[2]:
    case "0":
        inputstring = input()  # working with 1d arrays rn
        cfg.append(inputstring)
        process = subprocess.run(['python', 'only Run network.py', *cfg])
    case "1":
        inputfile = open("input.txt")
        cfg.append(inputfile.readlines()[0])
        process = subprocess.run(['python', 'only Run network.py', *cfg])
    case "2":
        process = subprocess.run(['python', 'Learning.py', *cfg])
"""output = process.stdout.strip()
print(output)"""
