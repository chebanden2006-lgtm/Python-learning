print("Task a")
with open("bonds.csv", "r") as f:
    content = f.read()
print(content)
print(type(content))
print(len(content))
print("Task b")
with open("bonds.csv", "r") as f:
    list_of_lines = f.readlines()
print(list_of_lines)
print(len(list_of_lines))
print(list_of_lines[-1].strip())
print(list_of_lines[2].strip())
print(list_of_lines[0].strip())
print(list_of_lines[-2].strip())
print("task c")
with open("bonds.csv", "r") as f:
    header = f.readline()
    first_line = f.readline()
    second_line = f.readline()
print(repr(header))
print(repr(first_line))
print(repr(second_line))

print("")
print("task d")
print("without cleaning")
with open("bonds.csv", "r") as f:
    for line in f:
        print(line)
print("with cleaning")
with open("bonds.csv", "r") as f:
    for line in f:
        print(line.strip())
#the differen is that we have removed \n to each line using strip() leaving only natural priny() jump
print("Task e")
with open("bonds.csv", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i} | {line.strip()}")
print("task f1")
with open("bonds.csv", "r") as f:
    contents = f.read()
    contents2 = f.read()
print(repr(contents))
print(repr(contents2)) #wasnt printed only '' because f.read() already extracted everything in first call,
print("task f2")
with open("bonds.csv", "r") as f:
    content = f.read()        # indented = file open
print(content)
#f.read() #ValueError: I/O operation on closed file. - will not work because it is out of indentation block
print("task f3")
#with open("bondss.csv", "r") as f:
    #content1 = f.read()
#FileNotFoundError: [Errno 2] No such file or directory: 'bondss.csv' - wrong name of the file we are reaching