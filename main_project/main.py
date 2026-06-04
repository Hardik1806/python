import helpers.math_utils
#importing the whole module
R1=helpers.math_utils.add(1,2)
print(f" using whole module result of addition is: {R1}")

#importing specific names

from helpers.math_utils import subtract,mul

R2=subtract(2,1)
R3=mul(2,3)
print(f"using specific names output of subtraction is: {R2}")
print(f"using specific names output of multiplication is: {R2}")

#importing with alias
import helpers.math_utils as mm

R4=mm.add(2,5)
print(f"using alias output of addition is : {R4}")

#trying to import everything
from helpers.math_utils import*
R5=square(5)
print(f"using imprt* reuslt of square is: {R5}")

