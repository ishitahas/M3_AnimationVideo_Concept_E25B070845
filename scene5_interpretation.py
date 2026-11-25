from manim import *
from theme import *

class Interpretation(Scene):
    def construct(self):
        self.chrome = chrome(5, "Interpretation")
        self.add(self.chrome)
        plane = NumberPlane()
        self.add(plane)
        self.add(self.chrome)

        title = Text("Checking by substitution", font_size=34).to_edge(UP)
        self.play(Write(title))

        o = plane.c2p(0, 0)
        v1 = Arrow(o, plane.c2p(1, 1), buff=0, color=BLUE)
        Av1 = Arrow(o, plane.c2p(3, 3), buff=0, color=TEAL)
        c1 = MathTex(r"A\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}3\\3\end{bmatrix}=3\begin{bmatrix}1\\1\end{bmatrix}",
                     font_size=40, color=BLUE).to_corner(UL).shift(DOWN * 0.8)
        c1.add_background_rectangle(opacity=0.8)

        self.play(GrowArrow(v1))
        self.play(Write(c1))
        self.play(Transform(v1.copy(), Av1), GrowArrow(Av1))
        self.wait(2)
        lab1 = Text("stretched by 3, same direction", font_size=24, color=TEAL).next_to(plane.c2p(3, 3), RIGHT)
        self.play(FadeIn(lab1))
        self.wait(2)

        v2 = Arrow(o, plane.c2p(1, -1), buff=0, color=ORANGE)
        c2 = MathTex(r"A\begin{bmatrix}1\\-1\end{bmatrix}=\begin{bmatrix}1\\-1\end{bmatrix}=1\begin{bmatrix}1\\-1\end{bmatrix}",
                     font_size=40, color=ORANGE).next_to(c1, DOWN, buff=0.4, aligned_edge=LEFT)
        c2.add_background_rectangle(opacity=0.8)
        self.play(GrowArrow(v2))
        self.play(Write(c2))
        lab2 = Text("unchanged (λ = 1)", font_size=24, color=ORANGE).next_to(plane.c2p(1, -1), RIGHT)
        self.play(FadeIn(lab2))
        self.wait(3)
