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

        NaturalBinary.__equalize(self.__Data, other.__Data)

        print(self)
        print(other)
       

    #String method Override       
    def __str__(self):
        return {"Raw Data": self.__Data}.__str__()

    @staticmethod
    def __equalize(ob1, ob2):
        diffrence = len(ob1) - len(ob2)

        if diffrence > 0:
            for _ in range(diffrence+1):
                ob2.append(0)
            ob1.append(0)
        elif  diffrence < 0:
            diffrence = -diffrence
            for _ in range(diffrence+1):
                ob1.append(0)
            ob2.append(0)





    



        


        

