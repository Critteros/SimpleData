class NaturalBinary:
   

    #Constructor
    def __init__(self, value = 0):

        #Defaults
        self.__Data = []

        # Sanitize the incoming data
        try:
            value = int(value)
        except:
            raise Exception('Provided value cannot be converted to an integer')
        
        #Check to prevent negatives
        if value < 0: value = -value
        #Setup for 0 value
        if value == 0: self.__Data.append(0)
        
        #Setup for other value
        while(value != 0):
            self.__Data.append(value%2)
            value = value//2
        
    #Defining Addition
    def __add__(self, other):

        if not isinstance(other, NaturalBinary): other = NaturalBinary(other) 

        result = NaturalBinary()

        #Setup
        #--------------------------------------------------
        NaturalBinary.__equalize(self.__Data, other.__Data) #This equals number of elements in both tables
        NaturalBinary.__equalize(self.__Data, result.__Data)
        self.__Data.append(0)                                #Overflow protection
        other.__Data.append(0)
        result.__Data.append(0)
        a = self.__Data # a+b=c
        b = other.__Data
        c = result.__Data
        #--------------------------------------------------
        #Addition Code below
        #--------------------------------------------------
        carryOver = 0
        
        for index in range(len(a)):
            sum = a[index] + b[index] + carryOver
            
            if sum == 0:
                c[index] = 0
                carryOver = 0
            elif  sum == 1:
                c[index] = 1
                carryOver = 0
            elif sum == 2:
                c[index] = 0
                carryOver = 1
            elif sum == 3:
                c[index] = 1
                carryOver = 1
        
        try:
            assert carryOver == 0
        except AssertionError:
            raise Exception(f'An error has occuer while adding carryOver = {carryOver}')



        #--------------------------------------------------
        #Cleanup
        #--------------------------------------------------
        NaturalBinary.__normalize(self.__Data)
        NaturalBinary.__normalize(other.__Data)
        NaturalBinary.__normalize(result.__Data)
        #--------------------------------------------------
        #Debug
        #!!!!!!!!!!!!!!!!!!!!!!!

        #!!!!!!!!!!!!!!!!!!!!!!!

        return result


        
       

    #String method Override       
    def __str__(self):
        return {"Raw Data": self.__Data}.__str__()

    #A funtion that adds 0 to eqalize indexes in both lists
    @staticmethod
    def __equalize(ob1, ob2):
        diffrence = len(ob1) - len(ob2)

        if diffrence > 0:
            for _ in range(diffrence+1): ob2.append(0)
      
        elif  diffrence < 0:
            diffrence = -diffrence
            for _ in range(diffrence+1): ob1.append(0)
    
    #A function to remove unnecesary zeros from equalizing
    @staticmethod
    def __normalize(ob):
        ob.reverse()
        while True:
            if ob[0] == 0 :
                ob.pop(0)
            else:
                ob.reverse()
                break




    



        


        

