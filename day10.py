import itertools
import re


number = int(input())

converter = format(number,'b')

Cantidad=max(len(i) for i in re.findall(r'1+',converter))


print(Cantidad)
