'''This code shows connections within a single Spine Block of Jupiter topology
There are 256 of these in the architecture
Each link is 1*40G'''

import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

'''This variable helps to keep track of the spline block 
we're currently working in '''
CurrentSB = 0

N_in_SB = 24 #Stores total number of switches in each spine block
N_in_AB = 256 #Stores total number of switches in each aggregation+ToR block
N_of_AB = 64 #Stores the number of aggregation blocks

'''We first assign node IDs to all switches across all Aggregation+ToR blocks
Thus node IDs of Spine Blocks begin with SB_Origin+1 '''
SB_Origin = N_of_AB*N_in_AB 

for CurrentSB in range(0,1): #In this demo we show a single spine block
	
	for SB_Stage1_Switch in range(0,16): #For each of the 16 stage 1 switches in a spine block
		
		for SB_Stage2_Switch in range(0,8): #For each of the 8 stage 2 switches in a spine block
			#Finding IDs
			SB_S1_ID = SB_Origin + N_in_SB*CurrentSB + SB_Stage1_Switch+1
			SB_S2_ID = SB_Origin + N_in_SB*CurrentSB + 16 + SB_Stage2_Switch+1
			G.add_edge(SB_S1_ID, SB_S2_ID, weight=1, capacity=40, color='black') #1*40G links

colors = [G[u][v]['color'] for u,v in G.edges()]
nx.draw(G,with_labels=True, edge_color=colors)
plt.show()


