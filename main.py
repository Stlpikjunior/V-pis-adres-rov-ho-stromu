import os
name = input("(napr.C:\\Program Files):")


def tree(path, depth=0):
    for item in os.listdir(path):
        if os.path.isdir(path+"\\"+item) and item[0] not in ".$":
            print("-" * depth, item)
            if os.listdir(path+"\\"+item):
                tree(path+"\\"+item, depth+1)

tree(name)

