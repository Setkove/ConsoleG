Hello My Name is Maga

im Dev and programmer

I created this graphical library because 
I wanted to show how to work with graphics using the tkinter library. 
I've created many projects with this library, 
and it's not difficult to use.

read these instructions and you will understand :::

"from ConsoleG import *

Name_it = CGCreateContext(width=yourwidth,height=yourheight,title="your title")"

CGCreateContext  creates a window context where all the graphics will be rendered


" Name_it = CGDrawLine(x1:1100,y1:1200 ,x2:21000, y2:21000, color="your color", width=yourwidth) "

CGDrawLine creates a line drawing on the window on our graph x1 x2 y1 y2 are the positions 
'but you can omit x2 and y2 if you don't create a line color is the color outline is the color of the outline 
and width is the size of the  : outline


CGDrawCircle is basically the same, but instead of drawing a line, 
we're drawing a circle. Why a circle? Because it doesn't have any points. 
The circle remains easy to draw, 
and we can modify the Circle line as desired.
:::

" circle = CGDrawCircle(1250, 50, radius 35, outline="black", fill="your color this is color", width=1) "

That's it
, now we can even run it by clicking on the play button. 
If it doesn't run, 
let's fix it so that it doesn't happen again.
If your project doesn't run, don't search for errors. 
Instead, write the following line at the end: 

Name_it.CGStartContext - this is this launches the program, 
creates our window,
and displays what we've done

Everything Started up and running

We can also create circles or lines ,
as well as ovals and polygons, 
such as rectangles.

triangle_points = [(400, 50), (450, 150), (350, 150)] - this points triangle
Name_it.CGDrawPolygon(triangle_points, outline="your color", fill="your color", width=yourwidth)

in addition to this, 
there is CGUI, 
which is the Console Graphics User Interface. 
It is not a class, but rather an add-on. 
You can add UI text to the beta version, 
but you can only add text.
Code :: 

Name_it = CGUIText(x=your x pos , y=your y pos , text = "your text" , fill = yourcolor , font=("yourfont",size_text))
but you can only add text.
Code :: 

Name_It = CGUIButton(x=your x pos ,y = your pos y , text='your text' ,fill=yourcolor,font=('your font',size_text),outline=your color , width=your width ,height= your height , foreground = your foreground)
Okay, let's make a complete code from everything we've learned.

Сode ::

from ConsoleG import *

graphics = CGCreateContext(3000, 3000, "Graphics")

graphics.CGDrawLine(100, 100, 300, 100, color="black", width=3)

triangle_points = [(1200, 500), (1100, 650), (1300, 650)]
triangle = graphics.CGDrawPolygon(triangle_points, outline="Black", fill="red", width=1)

graphics.CGDrawCircle(500, 100, 35, outline="black", fill="green", width=3)

graphics.CGUIText(x=200,y=50,text='Graphics Library on python',font=('Consolas',12))

graphics.СGStartContext()

So let's talk about the window and what's being drawn in it. 
We've learned how to draw lines, triangles, polygons, circles, and rectangles, 
but the question is how to clear all these drawings on our graph using the function.

CGRenderClear() - this function clears our renders that we've made, 
it clears everything, for example, 
we can make it so that when we press a key, 
our entire render is cleared
code::
import keyboard
def hotkey_pressed():
    graphics.CGRenderClear()
keyboard.add_hotkey('space', hotkey_pressed)

Cube:code:::

Name_it.CGDrawCube(x=your_x,y=your_y,size=number,outline=your_color,color=your_color,width=your_width)