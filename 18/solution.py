import copy

with open('input.txt') as f:
    data = f.read()

class Node:
    def __init__(self):
        self.up = None
        self.left = None
        self.right = None
        self.value = None

def parse_num(line, depth=0):
    if line[0].isdigit():
        return int(line)

    num = []
    for pos in range(len(line)):
        if line[pos] == '[':
            depth += 1
        if line[pos] == ']':
            depth -= 1

        if depth == 1 and line[pos] == ',':
            num.append(parse_num(line[1:pos]))
            num.append(parse_num(line[pos+1:-1]))

    return num

def make_tree(num, parent):
    this = Node()
    this.up = parent
    if type(num) == int:
        this.value = num
        return this
    
    this.left = make_tree(num[0], this)
    this.right = make_tree(num[1], this)

    return this

nums = [parse_num(line) for line in data.splitlines()]
trees_1 = []
for num in nums:
    trees_1.append(make_tree(num, None))
trees_2 = copy.deepcopy(trees_1)


def add(tree1, tree2):
    new_root = Node()
    tree1.up = new_root
    tree2.up = new_root
    new_root.left = tree1
    new_root.right = tree2
    return new_root

def find_exploding_node(node, depth):
    if depth == 5:
        return node.up
    if node.value is not None:
        return None
    return (
        find_exploding_node(node.left, depth + 1)
        or find_exploding_node(node.right, depth + 1)
    )

def find_splitting_node(node):
    if not node.value is None:
        if node.value > 9:
            return node
        else:
            return None
    return (
        find_splitting_node(node.left)
        or find_splitting_node(node.right)
    )

def find_left_ancestor(node, child):
    if node is None:
        return None
    if node.left is not child:
        return node.left
    return find_left_ancestor(node.up, node)

def find_right_ancestor(node, child):
    if node is None:
        return None
    if node.right is not child:
        return node.right
    return find_right_ancestor(node.up, node)

def bottom_right_node(node):
    while node.right:
        node = node.right
    return node
    
def bottom_left_node(node):
    while node.left:
        node = node.left
    return node

def reduce(tree):
    while 1:
        exploding_node = find_exploding_node(tree, 0)
        if exploding_node:
            left_ancestor = find_left_ancestor(exploding_node.up, exploding_node)
            if left_ancestor:
                left_node = bottom_right_node(left_ancestor)
                left_node.value += exploding_node.left.value

            right_ancestor = find_right_ancestor(exploding_node.up, exploding_node)
            if right_ancestor:
                right_node = bottom_left_node(right_ancestor)
                right_node.value += exploding_node.right.value

            exploding_node.left = None
            exploding_node.right = None
            exploding_node.value = 0

            continue

        splitting_node = find_splitting_node(tree)
        if splitting_node:
            left = Node()
            right = Node()

            left.up = splitting_node
            right.up = splitting_node

            left.value = int(splitting_node.value / 2)
            right.value = int(0.5 + splitting_node.value / 2)

            splitting_node.value = None
            splitting_node.left = left
            splitting_node.right = right

            continue
        
        break
          
    return tree

def get_magnitude(node):
    if node.value is not None:
        return node.value
    return 3 * get_magnitude(node.left) + 2 * get_magnitude(node.right)


tree_1 = trees_1[0]
for t in trees_1[1:]:
    tree_1 = add(tree_1, t)
    tree_1 = reduce(tree_1)
print("Part 1:", get_magnitude(tree_1))


largest_magnitude = 0
for i in range(len(trees_2)):
    for j in range(len(trees_2)):
        if i == j:
            continue
        t1 = copy.deepcopy(trees_2[i])
        t2 = copy.deepcopy(trees_2[j])

        mag = get_magnitude(reduce(add(t1, t2)))
        largest_magnitude = max(largest_magnitude, mag)
print("Part 2:", largest_magnitude)
