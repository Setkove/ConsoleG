from ConsoleG import *
def circle ():
    my_circle = main.CGDrawCircle(x=1300,y=500,radius=50,fill='Black')
main = CGCreateContext(width=3000,height=3000,title='ConsoleG')
Button_show_circle = main.CGUIButton(x=1300,y=1310,width=15,height=2,outline=0,fill='black',foreground='white',text='Show Circle',function=circle)
main.СGStartContext()