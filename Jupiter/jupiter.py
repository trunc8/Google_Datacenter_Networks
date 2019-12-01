'''To see visible plots, please first run singleSpineBlock and
singleAggregationBlock programs
This is the complete Jupiter topology with 256 spine blocks 
connected across 64 aggregation+ToR blocks
'''
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

'''This variable helps to keep track of the spline block 
we're currently working in '''
CurrentSB = 0
'''This variable helps to keep track of the aggregation+ToR block 
we're currently working in '''
CurrentAB = 0

N_in_SB = 24 #Stores total number of switches in each spine block
N_in_AB = 256 #Stores total number of switches in each aggregation+ToR block
N_of_AB = 64 #Stores the number of aggregation blocks

'''We first assign node IDs to all switches across all Aggregation+ToR blocks
Thus node IDs of Spine Blocks begin with SB_Origin+1 '''
SB_Origin = N_of_AB*N_in_AB 

for CurrentSB in range(0,256):
	
	for SB_Stage1_Switch in range(0,16): #For each of the 16 stage 1 switches in a spine block
		
		for SB_Stage2_Switch in range(0,8): #For each of the 8 stage 2 switches in a spine block
			#Finding IDs
			SB_S1_ID = SB_Origin + N_in_SB*CurrentSB + SB_Stage1_Switch+1
			SB_S2_ID = SB_Origin + N_in_SB*CurrentSB + 16 + SB_Stage2_Switch+1
			G.add_edge(SB_S1_ID, SB_S2_ID, weight=1, capacity=40, color='black') #1*40G links

for CurrentAB in range(0,64):
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


'''The next loop makes connections between the SB_Stage1 switches(16) of all the Spine Blocks(256)
to the Stage 2 Main Block switches of all the Aggregation Blocks'''
for CurrentSB in range(0, 256):
	for SB_Stage1_Switch in range(0,16):
		CurrentAB = int(CurrentSB/4) #Mapping 256 SBs to 64 ABs
		for x in range(0,4): #Each switch in SB_S1 connects to 4 MB_S2 switches
			#24 total switches in one spine block
			SB_S1_ID = SB_Origin +24*CurrentSB+ SB_Stage1_Switch +1
			#128 ToRs + 8*8 MB_S1 switches = 192 in a block
			MB_S2_ID = 256*(4*SB_Stage1_Switch +x)+ 193 + CurrentAB
			'''Same switch in SB will connect to MB_S2 switches from 4 different Aggregation Blocks'''

			G.add_edge(SB_S1_ID, MB_S2_ID, weight=2, capacity=40, color='blue') #2*40G links, Dual Redundancy

colors = [G[u][v]['color'] for u,v in G.edges()]
nx.draw(G,with_labels=True, edge_color=colors)
plt.show()