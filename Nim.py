import GameAnalyzer as GA

# Naming Functions
def list2name(game_state):
    return '{}{}{}'.format(*game_state)

def name2list(name):
    return [int(name[0]), int(name[1]), int(name[2])]

# Set up the GameNodes
starting_heaps = [3, 5, 7]


# Create nodes
nodes = {
    list2name([a, b, c]): GA.GameNode()
        for a in range(0, starting_heaps[0] + 1)
        for b in range(0, starting_heaps[1] + 1)
        for c in range(0, starting_heaps[2] + 1)
}

# Create out_node linkages
for node in nodes:
    out_node_heaps = []
    
    current_heaps = name2list(node)
    
    for remaining in range(current_heaps[0]):
        out_node_heaps.append(list2name([remaining, current_heaps[1], current_heaps[2]]))
    for remaining in range(current_heaps[1]):
        out_node_heaps.append(list2name([current_heaps[0], remaining, current_heaps[2]]))
    for remaining in range(current_heaps[2]):
        out_node_heaps.append(list2name([current_heaps[0], current_heaps[1], remaining]))
    
    nodes[node].out_nodes = out_node_heaps

GA.analyze(nodes, 'Nim.txt')