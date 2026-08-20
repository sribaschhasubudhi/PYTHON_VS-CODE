def demo1(a,b):
    print(a,b)
    def demo2(c,d):
        print(c,d)
        print(a,b)
    demo2(4,5)
#   print(c,d)      """we can't print this statement because 
#                      c and d are not defined."""
demo1(1,2)