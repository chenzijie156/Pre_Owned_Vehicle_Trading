from Car import Car

class CarInventoryNode:

    def __init__(self, car):
        self.make=car.make
        self.model=car.model
        self.cars=[]
        self.cars.append(car)
        self.left= None
        self.right= None
        self.parent= None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent=parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left=left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right=right

    def __str__(self):
        st1=""
        for car in self.cars:
            st1+=str(car)+"\n"
        return st1

    def findSuccessor(self):
        succ= None
        if self.getRight()!=None:
            succ=self.getRight().findMin()
        else:
            if self.parent:
                if self.getParent().getLeft()==self:
                    succ=self.parent
                else:
                    self.parent.setRight(None)
                    succ=self.parent.findSuccessor()
                    self.parent.setRight(self)
                    
        return succ

    def findMin(self):
        current=self
        while current.getLeft()!=None:
            current=current.getLeft()
        return current

    def spliceOut(self):
        if self.getRight()==None and self.getLeft()==None:
            if self.getParent().getLeft()==self:
                self.getParent().setLeft(None)
            else:
                self.getParent().setRight(None)
        elif self.getRight!=None or self.getLeft()!=None:
            if self.getRight()!=None:
                if self.getParent().getLeft()==self:
                    self.getParent().setLeft(self.getRight())
                else:
                    self.getParent().setRight(self.getRight())
                self.getRight().setParent(self.getParent())
            else:
                if self.getParent().getLeft()==self:
                    self.parent.setLeft(self.getRight())
                else:
                    self.getParent().setRight(self.getRight())
                self.getRight().setParent(self.parent)

    def replaceNodeData(self,make,model,cars,lc,rc):
        self.make=make
        self.model=model
        self.cars=cars
        self.left=lc
        self.right=rc
        if self.getLeft()!=None:
            self.getLeft().setParent(self)
        if self.getRight()!=None:
            self.getRight().setParent(self)
        
                
            
            
        
