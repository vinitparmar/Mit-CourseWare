import sys

class MaxHeap:
    # initialization of heap
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self. size = 0
        self.Heap = [0]*(self.maxsize+1)
        self. Heap[0] = sys.maxsize
        self.FRONT = 1
    
    
    # return the position of
    # the current node 
    # at position pos
    def parent(self,pos):
        return pos//2

    # return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self,pos):
        return 2*pos


    # return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self,pos):
        return (2*pos) + 1

    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self,pos):
        if pos >= (self.size//2) and pos <= self.size :
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self,fpos,spos):
        self.Heap[fpos] , self.Heap[spos] = self.Heap[spos] , self.Heap[fpos]
    
    
    def maxHeapify(self,pos):

        if not self.isLeaf(pos):
            if (self.Heap[pos] <= self.Heap[self.leftChild(pos)]or
                self.Heap[pos] <= self.Heap[self.rightChild(pos)]):
                
                if (self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]):
                    self.swap(pos,self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                else:

                    self.swap(pos,self.rightChild(pos))
                    self.maxHeapify(selfrightChild(pos))

    def insert(self,element):
        if self.size > self.maxsize:
            return
        
        self.size = self.size + 1
        self.Heap[self.size] =  element
        current = self.size

        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current , self.parent(current))
            current =self.parent(current)

    
     # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+str(self.Heap[i])+" LEFT CHILD : "+ 
                               str(self.Heap[2 * i])+" RIGHT CHILD : "+
                               str(self.Heap[2 * i + 1])) 
  

    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] =  self.Heap[self.size]
        self.size = self.size - 1
        self.maxHeapify(self.FRONT)

        return popped

# driver code
print("=============MAX HEAP===================")
minHeap = MaxHeap(15) 
minHeap.insert(5) 
minHeap.insert(3) 
minHeap.insert(17) 
minHeap.insert(10) 
minHeap.insert(84) 
minHeap.insert(19) 
minHeap.insert(6)  
minHeap.insert(22) 
minHeap.insert(9) 

minHeap.Print()
print("================================")
print("The Max val is " + str(minHeap.extractMax()))
print("================================")
