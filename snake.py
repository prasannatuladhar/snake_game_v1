from turtle import Turtle

SEGMENT_LOCATION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for seg in SEGMENT_LOCATION:
            segment = Turtle(shape="square")
            segment.fillcolor("white")
            segment.penup()
            segment.setpos(seg) 
            self.segments.append(segment) 
            # self.add_snake(seg)
            

    # def add_snake(self,position):
           

    def move_snake(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            xdistance = self.segments[seg_num-1].xcor()
            ydistance = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(xdistance,ydistance)

        self.head.forward(MOVE_DISTANCE)    
        
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  
    
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


