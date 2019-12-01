import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

NumberInBlock = 32

#This is the Number of nodes in one aggregation block, including the ToRs
#There are 16 ToRs for one aggregation block, and 16 4x4 switches in the aggregation block. Hence, NumberInBlock = 16+16 = 32

NumberOfBlock = 32

#Since there are 32 Aggregation blocks, NumberOfBlock = 32

f = open("ConstructedNodes.txt","w") #This writes the nodes that are constructed in a file, ConstructedNodes.txt

# Code for Firehose1.1 - Other topologies may be implemented by changing NumberInBlock and NumberOfBlock

for i in range(0,NumberOfBlock):

    #Connecting edges for all the Aggregation blocks
    
    #In each aggregation block, the 1st - 16th nodes are the ToRs. The 17th - 24th nodes are the 1st 8 switches in the Aggregation Block
    #The 25th - 32nd nodes are the 2nd level 8 switches in each aggregation block.

    # Differences from Firehose1.0 - The TORs have been connected to the aggregation block in a different way.
    # Also, the intra-aggregation block connections have also changed.
    
    for j in range(i*NumberInBlock+1,i*NumberInBlock+16):

        if j%2 == 1:
            G.add_edge(j,j+1)
            G.add_edge(j,j+1)
            f.write(str(j)+" "+str(j+1))
            f.write("\n")
            f.write(str(j)+" "+str(j+1))
            f.write("\n")

            # The concept of buddy ToRs has been used here

    for j in range(i*NumberInBlock+1,i*NumberInBlock+9):


        #This loop connects the ToR switches to the 1st level of aggregation block

        if j%2 == 1:

            G.add_edge(j,i*NumberInBlock+17)
            G.add_edge(j,i*NumberInBlock+18)
            f.write(str(j)+" "+str(i*NumberInBlock+17))
            f.write("\n")
            f.write(str(j)+" "+str(i*NumberInBlock+18))
            f.write("\n")
        
        else:
        
            G.add_edge(j,i*NumberInBlock+19)
            G.add_edge(j,i*NumberInBlock+20)
            f.write(str(j)+" "+str(i*NumberInBlock+19))
            f.write("\n")
            f.write(str(j)+" "+str(i*NumberInBlock+20))
            f.write("\n")

    for j in range(i*NumberInBlock+9,i*NumberInBlock+17):

        #This loop connects the ToR switches to the 1st level of aggregation block

        if j%2 == 1:

            G.add_edge(j,i*NumberInBlock+21)
            G.add_edge(j,i*NumberInBlock+22)
            f.write(str(j)+" "+str(i*NumberInBlock+21))
            f.write("\n")
            f.write(str(j)+" "+str(i*NumberInBlock+22))
            f.write("\n")

        else:

            G.add_edge(j,i*NumberInBlock+23)
            G.add_edge(j,i*NumberInBlock+24)
            f.write(str(j)+" "+str(i*NumberInBlock+23))
            f.write("\n")
            f.write(str(j)+" "+str(i*NumberInBlock+24))
            f.write("\n")

    for j in range(i*NumberInBlock+17,i*NumberInBlock+25):

        # This loop connects the 1st level of aggregation block to 2nd level of aggregation block

        if j%2 == 1:
            G.add_edge(j,i*NumberInBlock+25)
            G.add_edge(j,i*NumberInBlock+27)
            G.add_edge(j,i*NumberInBlock+29)
            G.add_edge(j,i*NumberInBlock+31)
            f.write(str(j)+" "+str(i*NumberInBlock+25))
            f.write("\n")
            f.write(str(j)+" "+str(i*NumberInBlock+27))
            f.write("\n")
            f.write(str(j)+" "+str(i*NumberInBlock+29))
            f.write("\n")
            f.write(str(j)+" "+str(i*NumberInBlock+31))
            f.write("\n")
        else:
            G.add_edge(j,i*NumberInBlock+26)
            G.add_edge(j,i*NumberInBlock+28)
            G.add_edge(j,i*NumberInBlock+30)
            G.add_edge(j,i*NumberInBlock+32)
            f.write(str(j)+" "+str(i*NumberInBlock+26))
            f.write("\n")
            f.write(str(j)+" "+str(i*NumberInBlock+28))
            f.write("\n")
            f.write(str(j)+" "+str(i*NumberInBlock+30))
            f.write("\n")
            f.write(str(j)+" "+str(i*NumberInBlock+32))
            f.write("\n")


    for j in range(i*NumberInBlock+25,i*NumberInBlock+33):

        # This loop connects the top 8 switches of the aggregation block to the correct ports of the switches in the spine block

        for k in range(0,4):

            G.add_edge(j,NumberInBlock*NumberOfBlock+((j-i*NumberOfBlock-25)*4+k)*12+(int)(i/4)+1)
            f.write(str(j)+" "+str(NumberInBlock*NumberOfBlock+((j-i*NumberOfBlock-25)*4+k)*12+(int)(i/4)+1))
            f.write("\n")

    for j in range(0,8):

        # This loop connects the lower switches in spine block with the upper switches in spine block

        for k in range(9,13):

            G.add_edge(NumberInBlock*NumberOfBlock+i*12+j+1,NumberInBlock*NumberOfBlock+i*12+k) 
            f.write(str(NumberInBlock*NumberOfBlock+i*12+j+1)+" "+str(NumberInBlock*NumberOfBlock+i*12+k))
            f.write("\n")
  


f.close()

#On Uncommenting the following lines the plot will be obtained

nx.draw(G,with_labels=True)
plt.savefig('Firehose11.png')
plt.show()

