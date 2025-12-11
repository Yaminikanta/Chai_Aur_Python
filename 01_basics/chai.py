from hello_chai import chai

chai('ginger tea')



"""
first we create hello_chai.py then we create chai.py 

in this we import the hello_chia file after import when we run it, it run but the __pycache__ file got created autometicaly 

"""


"""
when we work in shell means terminal if we impoert file then did some modification then the modified code will not import 
bcz it was written after import so to overcome that we need to import reload module thrn reload the file


import hello_chai

from importlib import reload             (imoport reload module)

reload(hello_chai)                       (reload the file)

hello_chai.chai_one                      (then it will work)           (refer youtube vdo no 4)



"""