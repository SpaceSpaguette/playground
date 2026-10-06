class graphs():
    def __init__(self):
        self.matrix = []
        self.size = 0
        self.names = []
    def init (self,count):
        self.size = count
        for x in range(count):
            self.matrix.append([])
            for y in range(count):
                self.matrix[x].append(0)
        for x in range(count):
            self.names.append(x)
    
    def add_edge(self,u,v,m):
        self.matrix[u][v] = m

    def remove_edge(self,u,v):
        self.matrix[u][v] = 0
    def print_graph(self):
        print("--------Matrix---------")
        print("     ",end="")

        for x in range(self.size):
            print(self.names[x],end="   ")
        print()

        print()
        for x in range(self.size):
            print(self.names[x], end="   ") 
            for y in range(self.size):
                print(f"[{self.matrix[x][y]}]", end=" ")
            print("\n")
        print("-----------------------")
    def get_neighbors(self,u):
        pass
    def set_name(self,index,name):
        self.names[index] = name
    def analize(self):
        """
        is valued == Has anything else then 1
        is oriented == if a 1 in 
        is recursive == if matrix[x][x] != 0
        complete === if matrix[x][y] != 0 for all and recursive 
        """
        temp_valued = False
        temp_oriented = False
        temp_recursive = False
        temp_complete = False
        
        for x in range(self.size):
            for y in range(self.size):
                if self.matrix[x][y] != 0 and self.matrix[x][y] != 1:
                    temp_valued = True
                if self.matrix[x][y] != self.matrix[y][x]:
                    temp_oriented = True
                if self.matrix[x][x] != 0:
                    temp_recursive = True
                if self.matrix[x][y] != 0:
                    temp_complete = True
        print(f"is simple: {not(temp_complete)}")
        print(f"is valued: {temp_valued}")
        print(f"is oriented: {temp_oriented}")
        print(f"is recursive: {temp_recursive}")
        print(f"Is Complete: {temp_complete}")

g = graphs()
g.init(5)
g.analize()
g.print_graph()