class Notebook:
    def __init__(self,):
        self.__pages=24
        self.type="Ruled"

    # @property method:-
    @property
    def sheets(self):
        return self.__pages,self.type

    # @name.setter method:-
    @sheets.setter                  # @'name of the @property method'.setter
    def sheets(self,copy):
        new_count,type=copy         # Tuple unpacking. We can't provide 2 values in a setter method
        
        self.__pages=new_count
        self.type=type

classmate=Notebook()
print(classmate.sheets)         # Calling @property method but looks like a attribute
classmate.sheets=(40,"Plain")   # Calling @sheets.setter method
print(classmate.sheets)