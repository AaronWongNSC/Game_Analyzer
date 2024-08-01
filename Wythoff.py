import GameAnalyzer as GA

# Naming Functions
def list2name(game_state):
    return '{}{}'.format(*game_state)

def name2list(name):
    return [int(name[0]), int(name[1])]

# Set up the GameNodes
starting_heaps = [9, 7]

# Create nodes
nodes = {
    list2name([a, b]): GA.GameNode()
        for a in range(0, starting_heaps[0] + 1)
        for b in range(0, starting_heaps[1] + 1)
}

# Create out_node linkages
links = []

for node in nodes:
    out_node_heaps = []
    
    current_heaps = name2list(node)
    
    for remaining in range(current_heaps[0]):
        out_node_heaps.append(list2name([remaining, current_heaps[1]]))
    for remaining in range(current_heaps[1]):
        out_node_heaps.append(list2name([current_heaps[0], remaining]))
    for taking in range(min(current_heaps[0], current_heaps[1])):
        out_node_heaps.append(list2name([current_heaps[0] - taking - 1, current_heaps[1] - taking - 1]))
    
    for potential_out_node in out_node_heaps:
        if name2list(potential_out_node) not in nodes[node].out_nodes:
            nodes[node].out_nodes.append(potential_out_node)

GA.analyze(nodes, 'Wythoff.txt')