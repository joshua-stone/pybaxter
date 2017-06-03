from pybaxter import Baxter, LEFT, RIGHT

if __name__ == '__main__':
    node = Baxter()
    node.reset_limb(LEFT)
    node.reset_limb(RIGHT)
    print(node.joints())
 
