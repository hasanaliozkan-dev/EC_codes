import random

class Crossover:
    def __init__(self,parent1,parent2):
        self.original1 = parent1
        self.original2 = parent2
        self.parent1 = parent1
        self.parent2 = parent2
        assert len(parent1) == len(parent2) , "Parents must be of equal length"
        self.random_position1 = random.randint(0,len(parent1)//2)
        self.random_position2 = random.randint(self.random_position1+1,len(parent1)-1)
        self.child1 = ['_' for i in range(len(parent1))]
        self.child2 = ['_' for i in range(len(parent2))]

    def one_point_crossover(self):
        self.child1 = self.parent1[:self.random_position1] + self.parent2[self.random_position1:]
        self.child2 = self.parent2[:self.random_position1] + self.parent1[self.random_position1:]
        print("One Point Crossover:")
        print(f"Cross over point -> {self.random_position1}")
        print(f"Parents : \np1 -> {self.parent1} \np2 -> {self.parent2}")
        print(f"Childrens: \nc1 -> {self.child1} \nc2 ->  {self.child2}")     

    def two_point_crossover(self):
        self.child1 = self.parent1[:self.random_position1] + self.parent2[self.random_position1:self.random_position2] + self.parent1[self.random_position2:]
        self.child2 = self.parent2[:self.random_position1] + self.parent1[self.random_position1:self.random_position2] + self.parent2[self.random_position2:]
        print("Two Point Crossover:")
        print(f"Cross over points -> {self.random_position1} and {self.random_position2}")
        print(f"Parents : \np1 -> {self.parent1} \np2 -> {self.parent2}")
        print(f"Childrens: \nc1 -> {self.child1} \nc2 ->  {self.child2}")

    def n_point_crossover(self,n):
        random_indices = sorted(random.sample(range(0,len(self.parent1)),n))
        self.parent1 = list(self.parent1)
        self.parent2 = list(self.parent2)
        self.child1[:random_indices[0]] = self.parent2[:random_indices[0]]
        self.child2[:random_indices[0]] = self.parent1[:random_indices[0]]
        random_indices.append(len(self.parent1))
        
        for i in range(1,len(random_indices)):
            
            for j in range(random_indices[i-1],random_indices[i]):
                if i %2 == 0:
                    self.child1[j] = self.parent2[j]
                    self.child2[j] = self.parent1[j]
                else:
                    self.child1[j] = self.parent1[j]
                    self.child2[j] = self.parent2[j]

        self.child1 = ''.join(self.child1)
        self.child2 = ''.join(self.child2)
        print(f"{n}(n') Point Crossover:")
        print(f"Cross over points -> {random_indices}")
        print(f"Parents : \np1 -> {self.original1} \np2 -> {self.original2}")
        print(f"Childrens: \nc1 -> {self.child1} \nc2 ->  {self.child2}")
   
    def uniform_crossover(self):
        self.child1 = []
        self.child2 = []
        random_list = [random.randint(0,1) for i in range(len(self.parent1))]
        for i in range(len(self.parent1)):
            if random_list[i] < 0.5:
                self.child1.append(self.parent1[i])
                self.child2.append(self.parent2[i])
            else:
                self.child1.append(self.parent2[i])
                self.child2.append(self.parent1[i])
        self.child1 = ''.join(self.child1)
        self.child2 = ''.join(self.child2)
        print("Uniform Crossover:")
        print(f"Random List -> {random_list}")
        print(f"Parents : \np1 -> {self.parent1} \np2 -> {self.parent2}")
        print(f"Childrens: \nc1 -> {self.child1} \nc2 ->  {self.child2}")
    
    def order_one_crossover(self):
        subset1 = list(self.parent1[self.random_position1:self.random_position2])
        subset2 = list(self.parent2[self.random_position1:self.random_position2])
        before1 = list(self.parent1[:self.random_position1])
        before2 = list(self.parent2[:self.random_position1])
        after1 = list(self.parent1[self.random_position2:])
        after2 = list(self.parent2[self.random_position2:])
        self.parent1 = list(self.parent1)
        self.parent2 = list(self.parent2)

        for i in range(self.random_position1,self.random_position2):
            self.child1[i] = self.parent2[i]
            self.child2[i] = self.parent1[i]
        remain1 = after1 + before1 + subset1
        remain2 = after2 + before2 + subset2

        for i in range(len(remain1)):
            if remain1[i] in self.child1:
                remain1[i] = '_'
            if remain2[i] in self.child2:
                remain2[i] = '_'

        remain1 = list(''.join(remain1).replace('_',''))
        remain2 = list(''.join(remain2).replace('_',''))
        for i in range(self.random_position2,len(self.child1)):
            self.child1[i] = remain1.pop(0)
            self.child2[i] = remain2.pop(0)

        for i in range(0,self.random_position1):
            self.child1[i] = remain1.pop(0)
            self.child2[i] = remain2.pop(0)
        self.child1 = ''.join(self.child1)
        self.child2 = ''.join(self.child2)
        print("Order One Crossover:")
        print(f"Cross over points -> {self.random_position1} and {self.random_position2}")
        print(f"Parents : \np1 -> {self.original1} \np2 -> {self.original2}")
        print(f"Childrens: \nc1 -> {self.child1} \nc2 ->  {self.child2}")
        
    def partially_mapped_crossover(self):
        subset1 = list(self.parent1[self.random_position1:self.random_position2])
        subset2 = list(self.parent2[self.random_position1:self.random_position2])
        before1 = list(self.parent1[:self.random_position1])
        before2 = list(self.parent2[:self.random_position1])
        after1 = list(self.parent1[self.random_position2:])
        after2 = list(self.parent2[self.random_position2:])

        self.parent1 = list(self.parent1)
        self.parent2 = list(self.parent2)
        for i in range(self.random_position1,self.random_position2):
            self.child1[i] = self.parent2[i]
            self.child2[i] = self.parent1[i]

        for i in range(len(before1)):
            if before1[i] not in subset2:
                self.child1[i] = before1[i]
            else: 
                index_temp  = self.child1.index(before1[i]) 
                temp = self.child2[index_temp]
                while temp in subset2:
                    index_temp = self.child1.index(temp)
                    temp = self.child2[index_temp]
                self.child1[i] = temp
            if before2[i] not in subset1:
                self.child2[i] = before2[i]
            else:
                index_temp  = self.child2.index(before2[i]) 
                temp = self.child1[index_temp]
                while temp in subset1:
                    index_temp = self.child2.index(temp)
                    temp = self.child1[index_temp]
                self.child2[i] = temp
        for i in range(len(after1)):
            if after1[i] not in subset2:
                self.child1[i+self.random_position2] = after1[i]

            else:
                index_temp  = self.child1.index(after1[i]) 
                temp = self.child2[index_temp]
                while temp in subset2:
                    index_temp = self.child1.index(temp)
                    temp = self.child2[index_temp]
                self.child1[i+self.random_position2] = temp
            if after2[i] not in subset1:
                self.child2[i+self.random_position2] = after2[i]
            else:
                index_temp  = self.child2.index(after2[i]) 
                temp = self.child1[index_temp]
                while temp in subset1:
                    index_temp = self.child2.index(temp)
                    temp = self.child1[index_temp]
                self.child2[i+self.random_position2] = temp
        self.child1 = ''.join(self.child1)
        self.child2 = ''.join(self.child2)
        print("Partially Mapped Crossover:")
        print(f"Cross over points -> {self.random_position1} and {self.random_position2}")
        print(f"Parents : \np1 -> {self.original1} \np2 -> {self.original2}")
        print(f"Childrens: \nc1 -> {self.child1} \nc2 ->  {self.child2}")

    def cyclic_crossover(self):
        self.parent1 = list(self.parent1)
        self.parent2 = list(self.parent2)
        indices1 = [] 
        indices2 = []
        indices1.append(0)
        index1 = -1
        while index1 != 0:
            index2 = self.parent2.index(self.parent1[indices1[-1]])
            indices2.append(index2)
            indices1.append(index2)
            index1 = indices1[-1]
              
        for elem in indices1:
            self.child1[elem] = self.parent1[elem]
        for elem in indices2:
            self.child2[elem] = self.parent2[elem]
        
        for i in range(len(self.child1)):
            if self.child1[i] == '_':
                self.child1[i] = self.parent2[i]
            if self.child2[i] == '_':
                self.child2[i] = self.parent1[i]
        self.child1 = ''.join(self.child1)
        self.child2 = ''.join(self.child2)
        
        print("Cyclic Crossover:")
        print(f"Parents : \np1 -> {self.original1} \np2 -> {self.original2}")
        print(f"Childrens: \nc1 -> {self.child1} \nc2 ->  {self.child2}")
        

            
#Examples
gene1 = ''.join([str(i) for i in  random.sample(range(0, 10), 10)])
gene2 = ''.join([str(i) for i in random.sample(range(0, 10), 10)])

crossover = Crossover(gene1,gene2)
crossover.one_point_crossover()
print()
crossover = Crossover(gene1,gene2)
crossover.two_point_crossover()
print()
crossover = Crossover(gene1,gene2)
crossover.n_point_crossover(2)
print()
crossover = Crossover(gene1,gene2)
crossover.uniform_crossover()
print()
crossover = Crossover(gene1,gene2)
crossover.order_one_crossover()
print()
crossover = Crossover(gene1,gene2)
crossover.partially_mapped_crossover()
print()
crossover = Crossover(gene1,gene2)
crossover.cyclic_crossover()


