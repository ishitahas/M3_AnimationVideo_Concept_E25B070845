from manim import *
from theme import *

class WorkedExample(Scene):
    def construct(self):
        self.chrome = chrome(4, "Worked example")
        self.add(self.chrome)
        title = Text("Finding eigenvalues of A", font_size=36).to_edge(UP)
        self.play(Write(title))

        A = MathTex(r"A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}", font_size=60)
        self.play(Write(A))
        self.wait(2)
        self.play(A.animate.scale(0.6).to_corner(UL).shift(DOWN * 0.8))

        steps = [
            r"A\vec{v} = \lambda \vec{v} \;\Rightarrow\; (A - \lambda I)\vec{v} = \vec{0}",
            r"A - \lambda I = \begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix}",
            r"\det(A - \lambda I) = (2-\lambda)^2 - 1 = 0",
            r"\lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3) = 0",
            r"\lambda_1 = 3, \quad \lambda_2 = 1",
        ]
        prev = None
        for s in steps:
            m = MathTex(s, font_size=44)
            if prev is None:
                m.move_to(UP * 1.5)
                self.play(Write(m))
            else:
                m.next_to(prev, DOWN, buff=0.45)
                self.play(Write(m))
            self.wait(2)
            prev = m
        self.play(prev.animate.set_color(YELLOW))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects if m is not A and m is not title and m is not self.chrome])

        # Eigenvector for lambda = 3
        e3 = VGroup(
            MathTex(r"\lambda = 3:\quad \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}\vec{v} = \vec{0}", font_size=44),
            MathTex(r"-x + y = 0 \;\Rightarrow\; x = y", font_size=44),
            MathTex(r"\vec{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}", font_size=44, color=BLUE),
        ).arrange(DOWN, buff=0.4).move_to(UP * 0.5)
        for m in e3:
            self.play(Write(m))
            self.wait(2)
        self.play(FadeOut(e3))

        # Eigenvector for lambda = 1
        e1 = VGroup(
            MathTex(r"\lambda = 1:\quad \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\vec{v} = \vec{0}", font_size=44),
            MathTex(r"x + y = 0 \;\Rightarrow\; x = -y", font_size=44),
            MathTex(r"\vec{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}", font_size=44, color=ORANGE),
        ).arrange(DOWN, buff=0.4).move_to(UP * 0.5)
        for m in e1:
            self.play(Write(m))
            self.wait(2)
        self.wait(1)
