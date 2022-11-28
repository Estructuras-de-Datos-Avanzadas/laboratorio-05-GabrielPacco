# Declaramos las librerias necesarias para graficar un MTree en 3 dimensiones

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib import rc
from matplotlib import rcParams
import matplotlib as mpl
import matplotlib.pyplot as plt

# Declaramos la clase Node, que es la que nos permite crear los nodos del MTree

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

# Declaramos la clase MTree, que es la que nos permite crear el MTree

class MTree:
    def __init__(self, root):
        self.root = root
        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_zlim(-10, 10)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title('MTree')
        self.ax.view_init(30, 60)
        self.ax.dist = 12
        self.ax.plot([0, 0], [0, 0], [-10, 10], 'k-')
        self.ax.plot([0, 0], [-10, 10], [0, 0], 'k-')
        self.ax.plot([-10, 10], [0, 0], [0, 0], 'k-')
        self.root.plot(self.ax, 0, 0, 10, 10)

    def plot(self):
        plt.show()

    # Funcion que nos permite graficar el MTree en 3 dimensiones

    def animate(self, i):
        self.ax.view_init(30, 0.3*i)
        return self.fig,

    def save(self, filename):
        self.ani = animation.FuncAnimation(self.fig, self.animate, frames=1200, interval=20, blit=False)
        self.ani.save(filename, writer='imagemagick', fps=30)

    # Declaramos la funcion main, que es la que nos permite ejecutar el programa

    def main():

        # Definiendo el nodo raiz del MTree

        root = Node(0)

        # Definiendo los nodos del MTree

        root.insert(1)
        root.insert(2)
        root.insert(3)
        root.insert(4)
        root.insert(5)
        root.insert(6)
        root.insert(7)
        root.insert(8)

        # Graficando el MTree
        
        mtree = MTree(root)
        mtree.plot()
        mtree.save('MTree_Visualization.gif')

    if __name__ == '__main__':
        main()

