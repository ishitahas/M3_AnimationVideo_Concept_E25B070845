from manim import *
from theme import *

class Summary(Scene):
    def construct(self):
        self.chrome = chrome(6, "Summary")
        self.add(self.chrome)
        title = Text("Three takeaways", font_size=40).to_edge(UP)
        self.play(Write(title))
        pts = VGroup(
            Text("1. An eigenvector keeps its direction under A.", font_size=28),
            Text("2. The eigenvalue λ is the stretch factor: Av = λv.", font_size=28),
            Text("3. Solve det(A − λI) = 0 for λ, then (A − λI)v = 0 for v.", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=0.7)
        for p in pts:
            self.play(FadeIn(p))
            self.wait(2)
        self.wait(1)
        self.play(FadeOut(pts), FadeOut(title))

        credits = VGroup(
            Text("Thank You!", font_size=40),
            Text("Eigenvalues and Eigenvectors", font_size=24),
            Text("Created using Manim Community Edition", font_size=22),
            Text("Narration and presentation by the student", font_size=22),
        ).arrange(DOWN, buff=0.4)
        self.play(FadeIn(credits))
        self.wait(5)
