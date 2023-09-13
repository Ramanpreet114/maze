# A class for a min heap
class MinHeap:
    
    def __init__(self, arr=[]):
        self.heap = [0 for i in range(len(arr))]
        self.n0_of_elements = 0
        for element in arr:
            self.heap[self.n0_of_elements] = element
            parent_position = (self.n0_of_elements - 1)//2
            new_node_position = self.n0_of_elements
            self.n0_of_elements += 1
            while new_node_position > 0:
                if self.heap[new_node_position] < self.heap[parent_position]:
                    self.heap[new_node_position], self.heap[parent_position] = self.heap[parent_position], self.heap[new_node_position]
                else:
                    break
                new_node_position = parent_position
                parent_position = (parent_position - 1)//2
        
    def insert(self, element):
        #adding new element to list
        self.heap.append(element)
    
        #heapifing
        parent_position = (self.n0_of_elements - 1)//2
        new_node_position = self.n0_of_elements
        self.n0_of_elements += 1
        while new_node_position > 0:
            if self.heap[new_node_position] < self.heap[parent_position]:
                self.heap[new_node_position], self.heap[parent_position] = self.heap[parent_position], self.heap[new_node_position]
            else:
                break
            new_node_position = parent_position
            parent_position = (parent_position - 1)//2
        

    def get_min(self):
        if self.n0_of_elements:
             return self.heap[0]

    def extract_min(self):
        # validate the list is not empty
        if self.n0_of_elements:
            #removing lowest value
            removed = self.heap[0] 
            self.heap[0] = None
            #removing rightmost-bottom element also
            last_element = self.heap[self.n0_of_elements - 1] 
            self.heap[self.n0_of_elements - 1] = None 
            # reducing no. of elements by one
            self.n0_of_elements -= 1        
            #sorting the remaing heap
            # setting position
            parent_position = 0
            left_child = (2 * parent_position) + 1
            right_child = (2 * parent_position) + 2
            #looping through heap
            while left_child < self.n0_of_elements :
                # trying to fit last element
                if self.heap[left_child] is not None and self.heap[right_child] is not None and last_element < self.heap[left_child] and last_element < self.heap[right_child]:
                    self.heap[parent_position] = last_element
                    break
                # validating right vhild is not out heap i.e. parent having 
                # only one child, secondly comparing childrens to swap with parent space 
                if  right_child >= self.n0_of_elements or self.heap[left_child] < self.heap[right_child]:
                    self.heap[parent_position] , self.heap[left_child] = self.heap[left_child], self.heap[parent_position]
                    parent_position = left_child
                else:
                    self.heap[parent_position] , self.heap[right_child] = self.heap[right_child], self.heap[parent_position]
                    parent_position = right_child
                #fetching new children positions
                left_child = (2 * parent_position) + 1
                right_child = (2 * parent_position) + 2
                
            if self.heap[parent_position] is None:
                self.heap[parent_position]  = last_element
                #heapifing
                new_node_position = parent_position
                parent_position = (parent_position - 1)//2
                while new_node_position > 0:
                  if self.heap[new_node_position] < self.heap[parent_position]:
                    self.heap[new_node_position], self.heap[parent_position] = self.heap[parent_position], self.heap[new_node_position]
                  else:
                     break
                new_node_position = parent_position
                parent_position = (parent_position - 1)//2
              
            return removed

    def is_empty(self):
        if self.n0_of_elements:
            return False
        return True

    def __len__(self):
        return self.n0_of_elements
