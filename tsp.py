#A python implementation of the famous TSP problem 
#You will provide a graph with nodes and a distance from each node to each node 
#You also need to add cost for each node which denotes a penalty for starting your journey from this node 

#python library dependency 
import numpy as np 

#class to import  
class TSP:
	def __init__(self,numberOfNodes):
		#total number of nodes in the graph 
		#node number will be 1 to (numberOfNodes)
		self.numberOfNodes=numberOfNodes 

		#each node starting cost 
		self.startCost={} 
		for i in range(1,self.numberOfNodes+1):
			#initially all the starting cost for each node will be zero 
			self.startCost[i]=0

		#each node ending cost 
		self.endCost={}
		for i in range(1,self.numberOfNodes+1):
			#initially all the ending cost for each node will be zero 
			self.endCost[i]=0

		#graph which saves the cost between nodes 
		self.graph={}  

		#path cost bitmask 
		self.costBitMask={}
		#path find bitmask 
		self.nextStateBitMask={}

	def AddEdge(self,node1,node2,cost):
		#function to add graph edges  
		#uni directional edges are constructed node1->node2, edge weight = cost  
		#node1, node2 will be integer and cost can be float/integer 
		if(node1 not in self.graph):
			self.graph[node1]={}
		if(node2 not in self.graph[node1]):
			self.graph[node1][node2]=cost 

	def AddStartCost(self,node,cost):
		#function to add start cost to each node 
		#node needs to be integer 
		self.startCost[node]=cost 

	def AddEndCost(self,node,cost):
		#function to add end cost to each node
		#nodes need to be integer
		self.endCost[node]=cost 

	def TspSolutionFinder(self):
		#function which will calculate the TSP path and cost 
		#starting no node visited 
		self.costBitMask[0]={}
		#supposing this value is the best value 
		self.BestValue = 10000000000000000 

		#performing recursion to calculate the value 
		minDistancePathSolution = self.DynamicProgramming(0,-1,0)
		print(minDistancePathSolution)
		
	def SetBit(self,value,bit):
		return (value | (1<<bit))
	def OffBit(self,value,bit):
		return (value & ~(1<<bit))
	def CheckBit(self,value,bit):
		if((value & (1<<bit))>0):
			return True
		return False 

	def DynamicProgramming(self,visitedNodesBitMask,lastNodeVisited,costUptoNow):

		if(self.BestValue<costUptoNow):
			#already best value calculated in some path
			#no need to traverse more 
			return 100000000000000

		if(visitedNodesBitMask>=((1<<self.numberOfNodes)-1)):
			#all nodes been visited 
			if(self.BestValue>costUptoNow):
				self.BestValue=costUptoNow+self.endCost[lastNodeVisited] 
			return costUptoNow

		if(visitedNodesBitMask in self.costBitMask and lastNodeVisited in self.costBitMask[visitedNodesBitMask]):
			return self.costBitMask[visitedNodesBitMask][lastNodeVisited] 
		
		if(lastNodeVisited == -1):
			#first movement 
			ret = 10000000000000000
			for i in range(1,self.numberOfNodes+1):
				value = self.DynamicProgramming(self.SetBit(0,i-1),i,self.startCost[i])
				if(value<ret):
					self.costBitMask[0][-1]=value
					ret=value 
			return ret 
		else:
			#other movements 
			ret = 10000000000000000
			for i in range(1,self.numberOfNodes+1):
				if(self.CheckBit(visitedNodesBitMask,i-1) == False and (lastNodeVisited in self.graph) and (i in self.graph[lastNodeVisited])):
					#this node not been visited and an edge between node (i, self.graph[lastNodeVisited])
					value = self.DynamicProgramming(self.SetBit(visitedNodesBitMask,i-1),i,costUptoNow+self.graph[lastNodeVisited][i])
					if(value<ret):
						ret=value 
			if(visitedNodesBitMask not in self.costBitMask):
				self.costBitMask[visitedNodesBitMask]={}
			self.costBitMask[visitedNodesBitMask][lastNodeVisited]=ret 
			return ret 


"""
obj=TSP(4)
obj.AddEdge(1,2,10)
obj.AddEdge(2,1,10)
obj.AddEdge(1,4,20)
obj.AddEdge(4,1,20)
obj.AddEdge(1,3,15)
obj.AddEdge(3,1,15)
obj.AddEdge(2,4,25)
obj.AddEdge(4,2,25)
obj.AddEdge(3,4,30)
obj.AddEdge(4,3,30)
obj.AddEdge(2,3,35)
obj.AddEdge(3,2,35)

obj.AddStartCost(1,0)
obj.AddStartCost(2,0)
obj.AddStartCost(3,0)
obj.AddStartCost(4,0)

obj.AddEndCost(1,0)
obj.AddEndCost(2,0)
obj.AddEndCost(3,0)
obj.AddEndCost(4,0)
"""

obj=TSP(4)
obj.AddEdge(1,2,10)
obj.AddEdge(2,1,10)
obj.AddEdge(1,3,1)
obj.AddEdge(3,1,1)
obj.AddEdge(2,3,2)
obj.AddEdge(3,2,2)
obj.AddEdge(2,4,3)
obj.AddEdge(4,2,3)
obj.AddEdge(3,4,30)
obj.AddEdge(4,3,30)


obj.TspSolutionFinder()
