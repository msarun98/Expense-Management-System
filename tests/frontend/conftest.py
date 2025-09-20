import os
import sys

root=os.path.join(os.path.dirname(__file__),'..')
print(root)
sys.path.insert(0,root)
print(sys.path)