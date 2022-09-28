import time


# classes
class State:
    def __init__(self, seeds, values, snake):
        self.seeds = seeds
        self.values = values
        self.snake = snake
        self.eaten = 0

    def __eq__(self, other):
        if other == None:
            return False
        return self.seeds == other.seeds and self.values == other.values and self.snake == self.snake

    def __hash__(self):
        snake = tuple(self.snake)
        values = tuple(self.values)
        return hash((snake, values))

    def delete_seed(self, index):
        self.seeds.pop(index)
        self.values.pop(index)

    def dec_seed_value(self, index):
        self.values[index] = self.values[index] - 1

    def eat(self, index):
        self.eaten = 1
        if (self.values[index] == 1):
            self.delete_seed(index)
            return
        if (self.values[index] == 2):
            self.dec_seed_value(index)


class Node:
    def __init__(self, state, id, parent, direction):
        self.state = state
        self.parent = parent
        self.id = id
        self.direction = direction


# functions
def snake_move(state, direc, row, col):
    new_snake = []
    seeds = []
    values = []
    for i in range(len(state.snake)):
        new_snake.append(state.snake[i])
    s_head = new_snake[0]
    for i in range(len(state.seeds)):
        seeds.append(state.seeds[i])
        values.append(state.values[i])
    eaten = state.eaten

    if direc == (0, 1) and s_head[1] + 1 >= col:
        direc = (0, 1 - col)
    if direc == (0, -1) and s_head[1] - 1 < 0:
        direc = (0, col - 1)
    if direc == (1, 0) and s_head[0] + 1 >= row:
        direc = (1 - row, 0)
    if direc == (-1, 0) and s_head[0] - 1 < 0:
        direc = (row - 1, 0)

    new_head = (s_head[0] + direc[0], s_head[1] + direc[1])
    if not eaten:
        tail = new_snake.pop()
        if len(new_snake) == 1 and new_head == tail:
            if not (row == 2 and s_head[1] == tail[1]) or (col == 2 and s_head[0] == tail[0]):
                return None

    if new_head in new_snake:
        return None
    new_snake.insert(0, new_head)
    new_state = State(seeds, values, new_snake)
    global total_states
    total_states += 1
    if new_head in seeds:
        seed_index = seeds.index(new_head)
        new_state.eat(seed_index)
    return new_state


def check_duplication(state, states):
    hashed = hash(state)
    if hashed not in states:
        if state != None:
            states.add(hashed)
            return True
    return False


def check_goal(state):
    if (state == None):
        return False
    if (len(state.seeds) == 0):
        return True
    return False


def find_driec(direc):
    if direc == (0, 1):
        return "R"
    if direc == (0, -1):
        return "L"
    if direc == (1, 0):
        return "D"
    if direc == (-1, 0):
        return "U"


def create_node(parent_id, state, states, nodes, direc, row, col):
    new_state = snake_move(state, direc, row, col)
    is_new = check_duplication(new_state, states)
    if not is_new:
        return None
    if state == None:
        return None
    new_node = Node(new_state, len(nodes), parent_id, find_driec(direc))
    return new_node


def add_child(node, queue, nodes):
    if node != None:
        nodes.append(node)
        queue.append(node)
        if check_goal(node.state):
            return True


def find_children(node, states, nodes, queue, row, col):
    state = node.state

    right_child = create_node(node.id, state, states, nodes, (0, 1), row, col)  # right
    if add_child(right_child, queue, nodes):
        return True

    left_child = create_node(node.id, state, states, nodes, (0, -1), row, col)  # left
    if add_child(left_child, queue, nodes):
        return True

    up_child = create_node(node.id, state, states, nodes, (-1, 0), row, col)  # up
    if add_child(up_child, queue, nodes):
        return True

    down_child = create_node(node.id, state, states, nodes, (1, 0), row, col)  # down
    if add_child(down_child, queue, nodes):
        return True

    return False


def bfs(nodes, states, row, col):
    queue = [nodes[0]]
    while queue:
        node = queue.pop(0)
        if find_children(node, states, nodes, queue, row, col):
            return nodes[len(nodes) - 1]


def find_sol(node):
    sol = []
    while node.parent != -1:
        sol.insert(0, node)
        node = nodes[node.parent]
    return sol

def print_sol(solution):
    string = ""
    for i in range(len(solution)):
        string += str(solution[i].direction)
    print(string)
# inputs

inputs = [int(x) for x in input().split(',')]
row = inputs[0]  # row
col = inputs[1]  # col
init_snake = [int(x) for x in input().split(',')]
seeds_num = int(input())
seeds = []
values = []
nodes = []

for i in range(seeds_num):
    inputs = [int(x) for x in input().split(',')]
    values.append(inputs[2])
    seeds.append(tuple(inputs[:2]))

# initial state
snake = [tuple(init_snake)]
init_state = State(seeds, values, snake)
states = {hash(init_state)}
total_states = 1

# initial Node
node = Node(init_state, 0, -1, None)
nodes.append(node)

# bfs
t1 = time.time()
goal_node = bfs(nodes, states, row, col)
t2 = time.time()
print("time:")
print((t2 - t1) * 1000)
solution = find_sol(goal_node)
print(" solution length: ")
print(len(solution))
print(" solution ")
print_sol(solution)
print(" number of the states: ")
print(total_states)
print(" number of the unique states: ")
print(len(nodes))