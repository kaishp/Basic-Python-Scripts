"""
------------------------------------------------------------------------
[Remove Lines from File]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2020-02-18"
------------------------------------------------------------------------
"""
filepath = "hello.py"

print(filepath)

fh = open(filepath,'r')

line_list = fh.readlines()
fh.close
print(line_list)

fh = open(filepath,'w')
fh.writelines(line_list[2:])
print("Done")

fh.close