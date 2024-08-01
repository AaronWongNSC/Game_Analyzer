import GameAnalyzer as GA

# Naming Functions
def list2name(game_state):
    return '/'.join([ str(value) for value in game_state ])

def name2list(name):
    heaps = []
    heaps_strings = name.split('/')
    for heap in heaps_strings:
        heaps.append(int(heap))
    
    return heaps

def prunelist(node_list):
    for node in node_list:
        node.sort()

    result = []
    [ result.append(node) for node in node_list if node not in result]

    return result
    


# Set up the GameNodes
starting_heaps = [3, 5, 7, 9]

# Create nodes
heaps = [ [] ]
for starting_heap in starting_heaps:
    heaps = [ heap + [value]
             for heap in heaps
             for value in range(starting_heap + 1) ]

heaps = prunelist(heaps)

nodes = {
    list2name(heap): GA.GameNode() for heap in heaps
}

# Create out_node linkages
for node in nodes:
    out_node_heaps = []
    
    current_heaps = name2list(node)

    for position in range(len(current_heaps)):
        for remaining in range(current_heaps[position]):
            out_node_heaps.append(current_heaps[:position] + [ remaining ] + current_heaps[position + 1:])
    
    out_node_heaps = prunelist(out_node_heaps)
    out_node_heaps = [ list2name(heap) for heap in out_node_heaps]
    
    nodes[node].out_nodes = out_node_heaps

GA.analyze(nodes, 'GeneralizedNim.txt', display = False)