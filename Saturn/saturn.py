'''The change from Watchtower to Saturn was the use of 24x10G merchant silicon building blocks
The topology remains nearly the same

'''
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

NumberInBlock = 18 #This is the Number of nodes in one aggregation block, including the ToRs

#There are 12 ToRs for one aggregation block, and 6 switches in the aggregation block. Hence, NumberInBlock = 12+6 = 18

NumberOfBlock = 228 

ToRsInBlock = 12

#No of ToRs for one aggregation block

f = open("ConstructedNodes.txt","w") #This writes the nodes that are constructed in a file, ConstructedNodes.txt

for i in range(0,NumberOfBlock):

    #Connecting edges for all the Aggregation blocks
    
    #In each aggregation block, the 1st - 8thth nodes are the ToRs. The 9thth - 12th nodes are the 4 switches in the Aggregation Block
    # The switches beyond NumberOfBlock*NumberInBlock are the spine block switches

    for j in range(i*NumberInBlock+1,i*NumberInBlock+ToRsInBlock+1):

        # This loop connects the ToR switches to the aggregation block switches

        for k in range(i*NumberInBlock+ToRsInBlock+1,i*NumberInBlock+NumberInBlock+1): 

            G.add_edge(j,k)
            f.write(str(j)+" "+str(k))
            f.write("\n")

    for j in range(i*NumberInBlock+ToRsInBlock+1,i*NumberInBlock+NumberInBlock+1):

        # This loop connects the aggregation block switches to the spine block

        for k in range(NumberOfBlock*NumberInBlock+1,NumberOfBlock*NumberInBlock+NumberOfBlock+1):

            G.add_edge(j,k)
            f.write(str(j)+" "+str(k))
            f.write("\n")
  


f.close()

#On Uncommenting the following lines the plot will be obtained

nx.draw(G,with_labels=True)
plt.savefig('Saturn.png')
plt.show()

