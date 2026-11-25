from manim import *
from theme import *

class Definition(Scene):
    def construct(self):
        self.chrome = chrome(2, "Definition")
        self.add(self.chrome)
        title = Text("Eigenvectors and Eigenvalues", font_size=40).to_edge(UP)
        self.play(Write(title))

        eq = MathTex(r"A", r"\vec{v}", r"=", r"\lambda", r"\vec{v}", font_size=96)
        self.play(Write(eq))
        box = SurroundingRectangle(eq, color=C_ACC, buff=0.5, corner_radius=0.25, stroke_width=3)
        self.play(Create(box))
        self.wait(1)

        eq[0].set_color(YELLOW)
        eq[1].set_color(BLUE)
        eq[3].set_color(GREEN)
        eq[4].set_color(BLUE)

        labelA = Text("matrix (the transformation)", font_size=24, color=YELLOW).next_to(eq[0], DOWN, buff=1.2)
        labelV = Text("eigenvector (a direction)", font_size=24, color=BLUE).next_to(eq[1], UP, buff=1.2)
        labelL = Text("eigenvalue (the stretch factor)", font_size=24, color=GREEN).next_to(eq[3], DOWN, buff=0.4).shift(RIGHT * 1.2)

        arrA = Arrow(labelA.get_top(), eq[0].get_bottom(), buff=0.1, color=YELLOW)
        arrV = Arrow(labelV.get_bottom(), eq[1].get_top(), buff=0.1, color=BLUE)
        arrL = Arrow(labelL.get_top(), eq[3].get_bottom(), buff=0.1, color=GREEN)

        self.play(FadeIn(labelA), GrowArrow(arrA))
        self.wait(1)
        self.play(FadeIn(labelV), GrowArrow(arrV))
        self.wait(1)
        self.play(FadeIn(labelL), GrowArrow(arrL))
        self.wait(1)

        meaning = Text("A only stretches v by λ. It does not turn it.", font_size=30).to_edge(DOWN)
        self.play(Write(meaning))
        self.wait(2)
