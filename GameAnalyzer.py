########## GameAnalyzer.py
# Analyzes game trees to label N-positions and P-positions and identify
# winning moves.
#
# Usage --
# -- Create a dictionary of GameNodes corresponding to the game. Nodes will
# be referenced by the dictionary keys.
# -- Analyze it using the analyzer
#
# GameNode class -- GameNodes contain 
# -- A list of out_nodes [built by the user]
# -- A label (N, P, or None) [labeled by the analyzer]
# -- A list of winning moves [built by the analyzer]

class GameNode:
    def __init__(self):
        self.out_nodes = []
        self.label = None
        self.winning_moves = []

def analyze(nodes, filename = None, display = True):
    # Preliminary Setup
    analyzed_nodes = []
    unanalyzed_nodes = [ node for node in nodes ]

    # Display node information 
    if display:
        print('List of all nodes and their out_nodes')
        for node in nodes:
            print('{}: {}'.format(node, nodes[node].out_nodes))
        print('----------------------')


    # Label terminal nodes as P-positions
    for node in nodes:
        if nodes[node].out_nodes == []:
            nodes[node].label = 'P'
            if node in unanalyzed_nodes:
                analyzed_nodes.append(node)
                unanalyzed_nodes.remove(node)

    # Display terminal node information     
    if display:
        print('List of all terminal nodes')
        for node in nodes:
            if nodes[node].out_nodes == []:
                print('{}: {}'.format(node, nodes[node].out_nodes))
        print('----------------------')
    
    # Analyze the remaining nodes
    while unanalyzed_nodes:
        if display:
            print('Unanalyzed_nodes: {}'.format(len(unanalyzed_nodes)))
        for node in unanalyzed_nodes:
            if display:
                print('Examining node {}'.format(node))
            # Determine if the node has all moves analyzed
            out_nodes_analyzed = True
            for out_node in nodes[node].out_nodes:
                if out_node in unanalyzed_nodes:
                    out_nodes_analyzed = False
            
            # If the node has all moves analyzed, determine if it N or P
            if out_nodes_analyzed:
                if display:
                    print('-- All out_nodes labeled')
                winning_move_found = False
                winning_moves = []
                for out_node in nodes[node].out_nodes:
                    if nodes[out_node].label == 'P':
                        winning_move_found = True
                        winning_moves.append(out_node)
            
                if winning_move_found:
                    if display:
                        print('-- Winning moves identified')
                    nodes[node].label = 'N'
                else:
                    if display:
                        print('-- No winning moves identified')
                    nodes[node].label = 'P'
                
                nodes[node].winning_moves = winning_moves
                
                analyzed_nodes.append(node)
                unanalyzed_nodes.remove(node)
                
                if display:
                    print('----------------------')
                
                break

    # Display final node information
    if display:
        print('----------------------')
        print('Node labels and winning moves')
        for node in analyzed_nodes:
            print('{} : {} -> {}'.format(node, nodes[node].label, nodes[node].winning_moves))
    
    with open(filename, 'w') as output_file:
        output_file.write('Node labels and winning moves\n')
        for node in analyzed_nodes:
            output_file.write('{} : {} -> {}\n'.format(node, nodes[node].label, nodes[node].winning_moves))
