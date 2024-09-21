class Operations:

    def perform_add(self,*args):

        
        total=sum([arg for arg in args if isinstance(arg,(int,float))])

        return total
    
    def get_max_number(self,*args):

        return max(args)
    

math=Operations()

print(math.perform_add(10,20))

print(math.perform_add(10,20,30,40,50.3))

print(math.get_max_number(10,20,30,100))

                                                                                                                                                                           








































































