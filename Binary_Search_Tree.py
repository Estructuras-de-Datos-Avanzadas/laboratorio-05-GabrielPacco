#Implementacion de un BST
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib import rc
from matplotlib import rcParams


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def findval(self, lkpval):
        if lkpval < self.value:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.value:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.value) + ' is found')

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()

    def plot(self, ax, x, y, dx, dy):
        ax.text(x, y, self.value, ha='center', va='center')
        if self.left:
            ax.plot([x, x-dx], [y, y-dy], 'k-')
            self.left.plot(ax, x-dx, y-dy, dx/2, dy)
        if self.right:
            ax.plot([x, x+dx], [y, y-dy], 'k-')
            self.right.plot(ax, x+dx, y-dy, dx/2, dy)

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
#Graficar el arbol
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, aspect='equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
root.plot(ax, 0, 0, 1, 1)
plt.show()

print(root.findval(7))
print(root.findval(14))
