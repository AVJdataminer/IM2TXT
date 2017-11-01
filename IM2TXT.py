import pytesseract
import pyautogui
import numpy
#ll=pyautogui.locateOnScreen('findpic.png')
#print(ll)
x1=250
x2=300
y1=464
y2=80
#text box
x=370
y=708
#save button
xs=495
ys=819
#skip button
xk=315
yk=808

#if __name__ == "__main__":
    # part of the screen
im=pyautogui.screenshot(region=(x1,y1,x2,y2)) # X1,Y1,X2,Y2
#im.show()
txt = pytesseract.image_to_string(im)
numpy.savetxt('Output.txt', [txt], fmt='%s')
#print(txt)
    #if len(txt) = 0:#if text length is zero click blank button
    #    pyautogui.click(xk, yk)
    #else:
pyautogui.doubleClick(x,y)
pyautogui.typewrite(txt, interval=2)
