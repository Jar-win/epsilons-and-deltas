from manimlib.imports import *

class Neighbourhood(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max":  10,
        "y_min": -10,
        "y_max":  10,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$X$",
        "y_axis_label": "$Y$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(-10,11,10),
        "y_labeled_nums": range(-10,11,10)
    }
    
    def on_screen_text(self):
        n1 = TextMobject("For every Neighbourhood")
        n2 = TextMobject(r"There exists\\ another\\ Neighbourhood")
        n1.shift(2.5*RIGHT+0.7*DOWN); n2.shift(1.5*UP+1*LEFT)
        n2.rotate(np.pi/2)
        n1.scale(0.5); n2.scale(0.5)
        #n2.shift(2.5*RIGHT+0.5*DOWN)
        return n1, n2

    def construct(self):
        self.setup_axes(animate=True)
        # creation
        rectangle_vertical   = Rectangle(width=1, height=3, color=YELLOW, fill_color=YELLOW, fill_opacity=0.75)
        rectangle_horizontal = Rectangle(width=4, height=1, color=ORANGE, fill_color=ORANGE, fill_opacity=0.75) 
        brace_vertical = Brace(rectangle_vertical) 
        brace_horizontal = Brace(rectangle_vertical)
        text1, text2 = self.on_screen_text()
        
        # shifting and rotating
        brace_vertical.move_to(0.2525*DOWN+2.5*RIGHT)
        brace_horizontal.move_to(1.5*UP+0.3*LEFT)
        brace_horizontal.rotate(3*np.pi/2)
        rectangle_vertical.shift(2.5*RIGHT+1.5*UP)
        rectangle_horizontal.shift(1.5*UP+2*RIGHT)
        
        # show creation / play
        self.play(ShowCreation(rectangle_vertical))
        self.play(ShowCreation(brace_vertical), ShowCreation(text1), run_time=2.5)
        self.play(ShowCreation(rectangle_horizontal))
        self.play(ShowCreation(brace_horizontal), ShowCreation(text2), run_time=2.5)
        self.wait(2)
