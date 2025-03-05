from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:

    def __init__(self):
        self.root=None
        
    def addCar(self, car):
        if self.root == None:
            self.root=CarInventoryNode(car)
        else:
            self._addCar(car,self.root)

    def _addCar(self,car,currentNode):
        if car.make==currentNode.getMake() and car.model==currentNode.getModel():
                currentNode.cars.append(car)
        elif car.__lt__(currentNode.cars[0]):
            if currentNode.getLeft()!=None:
                self._addCar(car,currentNode.getLeft())
            else:
                currentNode.setLeft(CarInventoryNode(car))
                currentNode.getLeft().setParent(currentNode)
        else:
            if currentNode.getRight()!=None:
                self._addCar(car,currentNode.getRight())
            else:
                currentNode.setRight(CarInventoryNode(car))
                currentNode.getRight().setParent(currentNode)

    def doesCarExist(self, car):
        if self.root == None:
            return False
        else:
            return self._doesCarExist(car,self.root)

    def _doesCarExist(self,car,currentNode):
        if currentNode==None:
            return False
        elif car.make==currentNode.getMake() and car.model==currentNode.getModel():
               i=0
               while i < len(currentNode.cars):
                   if car.__eq__(currentNode.cars[i]):
                       return True
                   else:
                       i=i+1
               return False
        else:
            if car.__lt__(currentNode.cars[0]):
                return self._doesCarExist(car,currentNode.getLeft())
            else:
                return self._doesCarExist(car,currentNode.getRight())

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self,tree):
        ret=""
        if tree!=None:
            ret +=self._inOrder(tree.getLeft())
            ret +=str(tree)
            ret +=self._inOrder(tree.getRight())
        return ret

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self,tree):
        ret =""
        if tree!=None:
            ret += str(tree)
            ret += self._preOrder(tree.getLeft())
            ret += self._preOrder(tree.getRight())
        return ret

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self,tree):
        ret = ""
        if tree!=None:
            ret += self._postOrder(tree.getLeft())
            ret += self._postOrder(tree.getRight())
            ret += str(tree)
        return ret

    def getBestCar(self, make, model):
        if self.root== None:
            return None
        else:
            return self._getBestCar(make,model,self.root)

    def _getBestCar(self,make,model,currentNode):
        if currentNode==None:
            return None
        elif make.upper()==currentNode.getMake() and model.upper()==currentNode.getModel():
                    if len(currentNode.cars)==1:
                        return currentNode.cars[0]
                    else:
                        biggest=currentNode.cars[0]
                        for car in currentNode.cars:
                            if car.__gt__(biggest):
                                biggest=car
                        return biggest
                
        else:
            if make.upper()<currentNode.getMake():
                return self._getBestCar(make,model,currentNode.getLeft())
            elif make.upper()==currentNode.getMake() and model.upper()<currentNode.getModel():
                return self._getBestCar(make,model,currentNode.getLeft())
            else:
                return self._getBestCar(make,model,currentNode.getRight())

    def getWorstCar(self, make, model):
        if self.root== None:
            return None
        else:
            return self._getWorstCar(make,model,self.root)

    def _getWorstCar(self,make,model,currentNode):
        if currentNode==None:
            return None
        elif make.upper()==currentNode.getMake() and model.upper()==currentNode.getModel():
                    if len(currentNode.cars)==1:
                        return currentNode.cars[0]
                    else:
                        smallest=currentNode.cars[0]
                        for car in currentNode.cars:
                            if car.__lt__(smallest):
                                smallest=car
                        return smallest
                
        else:
            if make.upper()<currentNode.getMake():
                return self._getWorstCar(make,model,currentNode.getLeft())
            elif make.upper()==currentNode.getMake() and model.upper()<currentNode.getModel():
                return self._getWorstCar(make,model,currentNode.getLeft())
            else:
                return self._getWorstCar(make,model,currentNode.getRight())


    def getTotalInventoryPrice(self):
        m=0
        if self.root==None:
            return m
        else:
            m+=self._getTotal(self.root)
        return m

    def _getTotal(self,currentNode):
        if currentNode==None:
            return 0
        else:
            s1=self._getTotal(currentNode.getLeft())
            s2=0
            for x in currentNode.cars:
                s2+=x.price
            s3=self._getTotal(currentNode.getRight())
            return s1+s2+s3

        
    def getSuccessor(self, make, model):
        if self._get2(make,model,self.root)!=None:
            Succ=self._get2(make,model,self.root)
            return Succ.findSuccessor()
        else:
            return None
         
            
    def _get2(self,make,model,currentNode):
        if not currentNode:
            return None
        elif make.upper()==currentNode.getMake() and model.upper()==currentNode.getModel():
                    return currentNode
        else:
            if make.upper()<currentNode.getMake():
                return self._get2(make,model,currentNode.getLeft())
            elif make.upper()==currentNode.getMake() and model.upper()<currentNode.getModel():
                return self._get2(make,model,currentNode.getLeft())
            else:
                return self._get2(make,model,currentNode.getRight())

    def _get(self,make,model,year,price,currentNode):
        if not currentNode:
            return None
        elif make.upper()==currentNode.getMake() and model.upper()==currentNode.getModel():
            for car in currentNode.cars:
                if car.year==year and car.price==price:
                    return currentNode
        else:
            if make.upper()<currentNode.getMake():
                return self._get(make,model,year,price,currentNode.getLeft())
            elif make.upper()==currentNode.getMake() and model.upper()<currentNode.getModel():
                return self._get(make,model,year,price,currentNode.getLeft())
            else:
                return self._get(make,model,year,price,currentNode.getRight())
    
    def removeCar(self, make, model, year, price):
        if self.root != None:
            nodeToRemove =self._get(make,model,year,price,self.root)
            
            if nodeToRemove:
                self._removeCar(nodeToRemove,year,price)
                return True
            else:
                return False
        
    def _removeCar(self,currentNode,year,price):
        if len(currentNode.cars)>1:
            for car in currentNode.cars:
                if price==car.price and year==car.year:
                    currentNode.cars.remove(car)

        elif currentNode==self.root and currentNode.getLeft()==None and currentNode.getRight()==None:
             self.root=None
                    
        elif currentNode.getLeft()==None and currentNode.getRight()==None:
            if currentNode == currentNode.getParent().getLeft():
                 currentNode.parent.setLeft(None)
            else:
                 currentNode.parent.setRight(None)
                 
        elif currentNode.getLeft()!=None and currentNode.getRight()!=None:
                succ= currentNode.findSuccessor()
                succ.spliceOut()
                currentNode.make=succ.getMake()
                currentNode.model=succ.getModel()
                currentNode.cars=succ.cars

        else:
            if currentNode.getLeft()!=None:
                if currentNode.getParent().getLeft()==currentNode:
                    
                    currentNode.getLeft().setParent(currentNode.parent)
                    currentNode.parent.setLeft(currentNode.getLeft())
                elif currentNode.getParent().getRight()==currentNode:
                    currentNode.getLeft().setParent(currentNode.parent)
                    currentNode.parent.setRight(currentNode.getLeft())
                else:
                    currentNode.replaceNodeData(currentNode.getLeft().getMake(),currentNode.getLeft().getModel(),currentNode.getLeft().cars,currentNode.getLeft().getLeft(),currentNode.getLeft().getRight())

            else:
                if currentNode.getParent().getLeft()==currentNode:
                    currentNode.getRight().setParent(currentNode.parent)
                    currentNode.parent.setLeft(currentNode.getRight())
                elif currentNode.getParent().getRight()==currentNode:
                    currentNode.getRight().setParent(currentNode.parent)
                    currentNode.parent.setRight(currentNode.getRight())
                else:
                    currentNode.replaceNodeData(currentNode.getRight().getMake(),currentNode.getRight().getModel(),currentNode.getRight().cars,currentNode.getRight().getLeft(),currentNode.getRight().getRight()) 




