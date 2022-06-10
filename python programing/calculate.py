#using simple module
from sympy import div
import module;
module.add(20,10)
module.sub(20,10)
module.mult(20,10)
module.div(20,10)

#using as object
import module as add;
add.add(20,10)
add.sub(20,10)
add.mult(20,10)
add.div(20,10)

#using from two function ni module
from module import add , sub;
add(20,10)
sub(20,10)

# print all math function
import math
count = dir(math)
print (count)