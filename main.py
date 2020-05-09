
class Backpack:
    def __init__(self):
     self.content = []
        # Add to our Backpack
    def add(self,item):
     self.content.append(item)
     print(u" Put in : ", item)
        # Let's see what we got!
    def inspect (self):
       print (u"What is in our backpack:")
       for item in self.content:
        print(" ",item)



    #def __str__(self):
     # return "Backpack : "+",".join (self.content)
   # print (str(my_backpack))
            # if is backpack is true
    def __bool__(self):
        return self.content !=[]
        # len of items
    def __len__(self):
     return len (self.content)
 #if my_backpack :
          #print ("The backpack in not empty!")
          #print ("U can find in, len(my_backpack),items ")
    #else:
          #print("Empty!")
my_backpack = Backpack()
my_backpack.add(item ="Book")
my_backpack.add(item ="pen")
my_backpack.inspect()
print(len(my_backpack))
