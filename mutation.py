import random

class Mutation:
    def __init__(self,string):
        self.original = string
        self.string = string
        self.random_position1 = random.randint(0,len(string)//2)
        self.random_position2 = random.randint(self.random_position1+1,len(string)-1)

    def scramble_mutation(self):
        
        subset = self.string[self.random_position1:self.random_position2]            
        before = self.string[:self.random_position1]
        after = self.string[self.random_position2:]
        scrambled_subset = ''.join(random.sample(subset,len(subset)))
        self.string = before + scrambled_subset + after
        print("Scramble Mutation: ")
        print(f"Mutation points -> {self.random_position1} and {self.random_position2}")
        print(f"Mutation performed on ->  {self.original}")
        print(f"Result of mutation -> {self.string}")
    
    def inversion_mutation(self):
        subset = self.string[self.random_position1:self.random_position2]
        before = self.string[:self.random_position1]
        after = self.string[self.random_position2:]
        inverted_subset = subset[::-1]
        self.string = before + inverted_subset + after
        print("Inversion Mutation:")
        print(f"Mutation points -> {self.random_position1} and {self.random_position2}")
        print(f"Mutation performed on ->  {self.original}")
        print(f"Result of mutation -> {self.string}")
    
    def swap_mutation(self):
        first = self.string[self.random_position1]
        second = self.string[self.random_position2]
        self.string = self.string.replace(first,'_').replace(second,first).replace('_',second)
        print("Swap Mutation:")
        print(f"Mutation points -> {self.random_position1} and {self.random_position2}")
        print(f"Mutation performed on ->  {self.original}")
        print(f"Result of mutation -> {self.string}")

    def insert_mutation(self):
        mlisst = list(self.string)
        mlisst.insert(self.random_position1,mlisst[self.random_position2])
        mlisst.pop(self.random_position2+1)
        self.string = ''.join(mlisst)
        print("Insert Mutation:")
        print(f"Mutation points -> {self.random_position1} and {self.random_position2}")
        print(f"Mutation performed on ->  {self.original}")
        print(f"Result of mutation -> {self.string}")



#Examples
mutator = Mutation("123456789")
mutator.scramble_mutation()
print()
mutator = Mutation("123456789")
mutator.inversion_mutation()
print()
mutator = Mutation("123456789")
mutator.swap_mutation()
print()
mutator = Mutation("123456789")
mutator.insert_mutation()
print()

