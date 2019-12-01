'''This code shows connections within a single Aggregation+ToR Block of Jupiter topology
There are 64 of these Blocks in the Jupiter architecture
In one block, there are 128 ToR switches connected by 2*10G links to AB
Aggregation Block(AB) consists of 8 Main Blocks(MB)
Each MB consists of two stages of switches- MB_S1, MB_S2
consisting of 8 switches each connected by 1*40G links'''
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

'''This variable helps to keep track of the aggregation+ToR block 
we're currently working in '''
CurrentAB = 0

N_in_AB = 256 #Stores total number of switches in each aggregation+ToR block

for CurrentAB in range(0,1): #In this demo we show a single aggregation+ToR block
	for MB_Stage1_Switch in range(0,8): #For each of the 8 stage 1 switches in a main block
		
		for CurrentMB in range(0,8): #For each of the 8 MBs in the aggregation block
			
			for tor_group in range(0,16): #Each switch in MB_S1 connects to 16 ToR switches
			#So 8 MB_S1 switches connect to 8*16=128 all ToR switches in the block
				#Finding IDs
				#128 ToRs in a block
				MB_S1_ID = N_in_AB*CurrentAB + 129 + 8*CurrentMB + MB_Stage1_Switch
				tor_ID = N_in_AB*CurrentAB + MB_Stage1_Switch+1+tor_group
				G.add_edge(MB_S1_ID, tor_ID, weight=2, capacity=10, color='indigo') #2*10G links, Dual Redundancy
			
			for MB_Stage2_Switch in range(0,8): #For each of the 8 stage 2 switches in a main block
				#Finding IDs
				#128 ToRs in a block
				MB_S1_ID = N_in_AB*CurrentAB + 129 + 8*CurrentMB + MB_Stage1_Switch
				#128 ToRs + 8*8 MB_S1 switches = 192 in a block
				MB_S2_ID = N_in_AB*CurrentAB + 193 + 8*CurrentMB + MB_Stage2_Switch
				G.add_edge(MB_S1_ID, MB_S2_ID, weight=1, capacity=40, color='black') #1*40G links


colors = [G[u][v]['color'] for u,v in G.edges()]
nx.draw(G,with_labels=True, edge_color=colors)
plt.show()


