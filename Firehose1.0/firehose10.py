import matplotlib.pyplot as plt
import networkx as nx
import numpy
G = nx.Graph()

NumberInBlock = 32 

#This is the Number of nodes in one aggregation block, including the ToRs
#There are 16 ToRs for one aggregation block, and 16 4x4 switches in the aggregation block. Hence, NumberInBlock = 16+16 = 32

NumberOfBlock = 32

#Since there are 32 Aggregation blocks, NumberOfBlock = 32

f = open("ConstructedNodes.txt","w") #This writes the nodes that are constructed in a file, ConstructedNodes.txt


# Code for Firehose1.0 - Other topologies may be implemented by changing NumberInBlock and NumberOfBlock

for i in range(0,NumberOfBlock):

    #Connecting edges for all the Aggregation blocks
    
    #In each aggregation block, the 1st - 16th nodes are the ToRs. The 17th - 24th nodes are the 1st 8 switches in the Aggregation Block
    #The 25th - 32nd nodes are the 2nd level 8 switches in each aggregation block.

    for j in range(i*NumberInBlock+1,i*NumberInBlock+17):

        #This loop connects the ToR switches to the 1st level of aggregation block

        G.add_edge(j,i*NumberInBlock+17+(int)((j-i*NumberInBlock-1)/4))
        f.write(str(j)+" "+str(i*NumberInBlock+17+(int)((j-i*NumberInBlock-1)/4)))
        f.write("\n")
        G.add_edge(j,i*NumberInBlock+21+(int)((j-i*NumberInBlock-1)/4))
        f.write(str(j)+" "+str(i*NumberInBlock+21+(int)((j-i*NumberInBlock-1)/4)))
        f.write("\n")

    for j in range(i*NumberInBlock+17,i*NumberInBlock+21):

        # This loop connects the 1st level of aggregation block to 2nd level of aggregation block, for switches number 17-20

        for k in range(i*NumberInBlock+25,i*NumberInBlock+29):
            G.add_edge(j,k)
            f.write(str(j)+" "+str(k))
            f.write("\n")

    for j in range(i*NumberInBlock+21,i*NumberInBlock+25):

        # This loop connects the 1st level of aggregation block to 2nd level of aggregation block, for switches number 21-24

        for k in range(i*NumberInBlock+29,i*NumberInBlock+33):
            G.add_edge(j,k)
            f.write(str(j)+" "+str(k))
            f.write("\n")

    for j in range(i*NumberInBlock+25,i*NumberInBlock+33):

        # This loop connects the top 8 switches of the aggregation block to the correct ports of the switches in the spine block
        # Note that the indexes of the spine block switches start from 32*32+1, as 32*32 nodes were present in the aggregation block and ToRs

        for k in range(0,4):
            G.add_edge(j,NumberInBlock*NumberOfBlock+((j-i*NumberOfBlock-25)*4+k)*12+(int)(i/4)+1)
            f.write(str(j)+" "+str(NumberInBlock*NumberOfBlock+((j-i*NumberOfBlock-25)*4+k)*12+(int)(i/4)+1))
            f.write("\n")

    for j in range(0,8):

        # This loop connects the lower switches in spine block with the upper switches in spine block

        for k in range(9,13):
            G.add_edge(NumberInBlock*NumberOfBlock+i*12+j+1,NumberInBlock*NumberOfBlock+i*12+k) 
            f.write(str(32*32+i*12+j+1)+" "+str(32*32+i*12+k))
            f.write("\n")
  


f.close()

#On Uncommenting the following lines the plot will be obtained

nx.draw(G,with_labels=True)
plt.show()
