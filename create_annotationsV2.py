import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector

clas = '0'

def write_text(image_folder, img, object_list, tl_list, br_list,class_list, savedir):    
    mystr =  img.path
    for i in range(len(tl_list)):
        x, y = tl_list[i]
        xe, ye = br_list[i]
        mystr += " " + str(x)+","+str(y)+","+str(xe)+","+str(ye)+","+class_list[i]+" "

    mystr += '\n'
    with open('train.txt', 'a') as file:
        file.write(mystr)
        file.close()
        



img = None
tl_list = []
br_list = []
class_list = []
object_list = []

# constants
image_folder = 'images'
savedir = 'annotations'
obj = ['CT', 'Terrorist']


def line_select_callback(clk, rls):
    global tl_list
    global br_list
    global object_list
    global class_list
    plt.connect('key_press_event', set_class)
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    class_list.append(clas)
    if clas == '0':
        object_list.append(obj[0])
    else:
        object_list.append(obj[1])



def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    global class_list
    if event.key == 'q':
        write_text(image_folder, img, object_list, tl_list, br_list, class_list,savedir)
        print(object_list)
        tl_list = []
        br_list = []
        class_list = []
        object_list = []
        img = None
        plt.close()


def toggle_selector(event):
    toggle_selector.RS.set_active(True)

def set_class(event):
    global clas
    
    if event.key == '1':
        clas = '0'
        print('class set to 0')
    elif event.key == '2':
        print('class set to 1')
        clas = '1'


if __name__ == '__main__':
    print('Default class set to 0')
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig, ax = plt.subplots(1)
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(ax, line_select_callback,
                                                drawtype='box', useblit=True,
                                                button=[1], minspanx=5, minspany=5,
                                                spancoords='pixels', interactive=True )
        global clas
        clas = '0'
        
        set_clas = plt.connect('key_press_event', set_class)
        bbox = plt.connect('key_press_event', toggle_selector)
        key = plt.connect('key_press_event', onkeypress)
        plt.show()
        
        
