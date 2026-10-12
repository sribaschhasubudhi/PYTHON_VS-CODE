# Let's make a class of laptops.
# We will define brand, model, RAM, CPU as attributes.

## All the methods had been commented. if you want to run of the methods, 
## you need to remove the comments from the methods and the respective method calling statements.

class Laptop:
    # Constructor
    def __init__(self,brand,model,ram,cpu):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.cpu=cpu

    '''def old_chip(self,cpu):
        print(f"Older version had {cpu} chips")'''

# Using multiple constructors (@classmethod):-

    # @classmethod-1
    '''@classmethod
    def laptop_2(cls,brand,model,cpu):
        default_ram=16

        print(f"{brand} {model} with Intel core {cpu}")
        return  cls(brand,model,default_ram,cpu)'''

    # @classmethod-2
    '''@classmethod
    def laptop_str(cls,lap_str):
        default_cpu="Celeron"
        brand,model,ram=lap_str.split(",")
        print(f"this is {brand} {model} with {default_cpu} processor")
        return cls(brand,model,ram,default_cpu)'''
    ''' ~You can call the default-CPU value only inside this classmethod'''

    # @classmethod-3
    '''@classmethod
    def laptop_dict(cls,laptop_dict):
        return cls(
            brand=laptop_dict["brand"],
            model=laptop_dict["model"],
            ram=laptop_dict["ram"],
            cpu=laptop_dict["cpu"]
        )'''

    # @classmethod-4
    '''@classmethod
    def laptop_dict2(cls,laptop_dict):
        default_cpu="Rygen 7"
        print(f"Best gaming laptop: {laptop_dict['brand']} {laptop_dict['model']}")
        return cls(
            brand=laptop_dict["brand"],
            model=laptop_dict["model"],
            ram=laptop_dict["ram"],
            cpu=default_cpu
        )'''

laptop1=Laptop("Apple","Macbook Air",16,"m5")       # for constructor

# ~for @classmethod-1
'''laptop2=Laptop.laptop_2("HP","Omnibook","i5")'''
''' ~You need to call the class and the classmethod name in the 2nd object
    to make it accesible for @classmethod'''     

# ~for @classmethod-2
'''data="Acer,Aspire,12"           # 3 attributes provided instead of 4(cpu not given)
laptop3=Laptop.laptop_str(data)
print(f"The 3rd laptop is {laptop3.brand} {laptop3.model} with {laptop3.ram}GB RAM")'''
''' ~You can't call the default-CPU value here'''

# ~for @classmethod-3
'''dict_data={"brand":"Asus","model":"Vivobook","ram":8,"cpu":"i3"}
laptop4=Laptop.laptop_dict(dict_data)
print(f"Best laptop:- {laptop4.brand} {laptop4.model}")'''

# ~for @classmethod-4
'''dict2_data={"brand":"HP","model":"Victus","ram":16}
laptop5=Laptop.laptop_dict2(dict2_data)'''

#laptop1.old_chip("m4")

'''print(f"1st laptop is {laptop1.brand} {laptop1.model}")
print(f"It has {laptop1.ram} GB and {laptop1.cpu} processor")'''
