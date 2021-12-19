with open('input.txt') as f:
    data = f.read()

class Node:
    def __init__(self):
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

def make_tree(num):
    this = Node()
    if type(num) == int:
        this.value = num
        return this

    this.left = make_tree(num[0])
    this.right = make_tree(num[1])
    return this

def add(tree1, tree2):
    new_root = Node()
    new_root.left = tree1
    new_root.right = tree2
    return new_root

def find_exploding_node(node):
    left = None
    target = None
    right = None
    horizon = [(node, 0)]
    while horizon:
        node, depth = horizon.pop()

        if depth == 4 and not target and node.value is None:
            target = node
            continue

        if not target and node.value is not None:
            left = node
        
        if target and node.value is not None:
            right = node
            return left, target, right
        
        if node.left and node.right:
            horizon += [(node.right, depth + 1), (node.left, depth + 1)]
    
    return left, target, right

def find_splitting_node(node):
    if node.value is not None:
        if node.value > 9:
            return node
        else:
            return None
    return (
        find_splitting_node(node.left)
        or find_splitting_node(node.right)
    )

def reduce(tree):
    while 1:
        left, exploding_node, right = find_exploding_node(tree)
        if exploding_node:
            if left:
                left.value += exploding_node.left.value
            if right:
                right.value += exploding_node.right.value
            exploding_node.left = None
            exploding_node.right = None
            exploding_node.value = 0
            continue

        splitting_node = find_splitting_node(tree)
        if splitting_node:
            left = Node()
            right = Node()

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


nums = [parse_num(line) for line in data.splitlines()] # snailfish numbers as lists
trees = [make_tree(num) for num in nums] # snailfish numbers as trees


full_tree = trees[0]
for tree in trees[1:]:
    full_tree = add(full_tree, tree)
    full_tree = reduce(full_tree)
print("Part 1:", get_magnitude(full_tree)) # 3305


largest_magnitude = 0
for num1 in nums:
    for num2 in nums:
        if num1 is num2:
            continue
        t1 = make_tree(num1)
        t2 = make_tree(num2)
        magnitude = get_magnitude(reduce(add(t1, t2)))
        largest_magnitude = max(largest_magnitude, magnitude)
print("Part 2:", largest_magnitude) # 4563
