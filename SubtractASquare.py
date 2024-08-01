import GameAnalyzer as GA

# Set up the GameNodes
starting_value = 26
remove_values = [1, 4, 9, 16, 25]

nodes = {
    value: GA.GameNode() for value in range(starting_value + 1)
    }

# Create out_node linkages
for node in nodes:
    out_nodes = []
    for remove in remove_values:
        if node - remove >= 0:
            out_nodes.append(node - remove)

    nodes[node].out_nodes = out_nodes
            
# Analyze the game
GA.analyze(nodes, 'SubtractASquare.txt')