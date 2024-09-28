from manim import *
from math import *

class PPText(Scene):
    def show_text(self):
        textPP = Text("PPv2").scale(3).next_to(Point((0, 0, 0)), UP)
        textStrain = Text("Strain").scale(3).next_to(Point((0, 0, 0)), UP)
        text = Text(" System").scale(3).next_to(textPP, DOWN)
        self.add(textPP, text)
        self.play(Transform(textPP, textStrain))

        self.wait()
    def total_strain(x):
        strain = 0
        DELTA_TIME = 150
        for i in range(int(x)):
            strain += 1
            strain *= pow(0.15, DELTA_TIME / 1000.0)
        return strain
    def strain_visual(self):
        OBJECTS=11
        axes = Axes(
            x_range=[0, OBJECTS, 1],
            y_range=[0, 5],
            x_length=7,
            y_length=4
        )
        axes.move_to(Point((3, 0, 0)))
        labels = axes.get_axis_labels(x_label="note count", y_label="strain")
        vt = ValueTracker(0)
        x_vals = []
        y_vals = []
        for i in range(OBJECTS):
            x_vals.append(i)
            y_vals.append(PPText.total_strain(i))
        self.add(axes, labels)

        hitCircle1 = Circle(color=WHITE)
        hitCircle1.move_to(Point((-5.5, -2.5, 0)))
        hitCircle2 = Circle(color=WHITE)
        hitCircle2.move_to(Point((-3.0, 2.5, 0)))
        self.add(hitCircle1)
        self.add(hitCircle2)

        cursor = Circle(color=YELLOW, radius=0.3)
        cursor.set_fill(YELLOW, opacity=1)
        cursor.move_to(hitCircle1.get_center())
        self.add(cursor)

        self.play(*[FadeIn(mob) for mob in self.mobjects])
        self.add(Dot(axes.c2p(0, 0)))

        for i in range(1, ceil(OBJECTS/2)):
            dot1 = Dot(axes.c2p(x_vals[i*2-1], y_vals[i*2-1]), color=RED, z_index=1)
            if (i > 0):
                line1 = Line(start=axes.c2p(x_vals[i*2-2], y_vals[i*2-2]), end=dot1.get_center())
            if (i == 0):
                self.play(cursor.animate.move_to(hitCircle2.get_center()))
            else:
                self.play(AnimationGroup(cursor.animate.move_to(hitCircle2.get_center()), Create(line1)))
            self.add(dot1)
            dot2 = Dot(axes.c2p(x_vals[i*2], y_vals[i*2]), color=RED, z_index=1)
            line2 = Line(start=dot1.get_center(), end=dot2.get_center())
            self.play(AnimationGroup(cursor.animate.move_to(hitCircle1.get_center()), Create(line2)))
            self.add(dot2)
        end_i = len(x_vals)-1
        line = Line(start=axes.c2p(x_vals[end_i-1], y_vals[end_i-1]), end=axes.c2p(x_vals[end_i], y_vals[end_i]))
        self.play(Create(line))
    def change_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
    


    def construct(self):
        self.show_text()
        self.change_scene()
        self.strain_visual()
        self.change_scene()
