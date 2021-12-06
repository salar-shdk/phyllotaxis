import sys

from . import Phyllotaxis
from . import Blender
from . import Plot
 
def main(args):
    try:
        action = args[0]
        node_number = int(args[1])
    except:
        print('2 positional arguments is needed, action and number of nodes. (ex: render 600)')
        return
    
    phy = Phyllotaxis(node_number)
    
    if action == 'plot':
        plot = Plot(phy)
        plot.render()
    elif action == 'render':
        blender = Blender(phy)
        blender.render()
    else:
        print('action is not valid. (choices: plot, render)')

if __name__ == '__main__':
    main(sys.argv[1:])
