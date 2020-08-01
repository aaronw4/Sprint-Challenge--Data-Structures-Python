import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
class BSTNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def insert(self, name):
        curr_node = self

        while curr_node is not None:
            if name < curr_node.name:
                if curr_node.left is None:
                    curr_node.left = BSTNode(name)
                    curr_node = None
                else:
                    curr_node = curr_node.left
            elif name >= curr_node.name:
                if curr_node.right is None:
                    curr_node.right = BSTNode(name)
                    curr_node = None
                else: 
                    curr_node = curr_node.right

    def contains(self, target):
        curr_node = self

        while curr_node is not None:
            if curr_node.name == target:
                return True
            elif target < curr_node.name:
                if curr_node.left is None:
                    return False
                else:
                    curr_node = curr_node.left
            elif target >= curr_node.name:
                if curr_node.right is None:
                    return False
                else: 
                    curr_node = curr_node.right

first_list = BSTNode(names_1[0])

for x in range(1, len(names_1)):
    first_list.insert(names_1[x])

for name_2 in  names_2:
    if first_list.contains(name_2):
        duplicates.append(name_2)


# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
