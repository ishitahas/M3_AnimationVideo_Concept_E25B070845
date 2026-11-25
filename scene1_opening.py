from manim import *
from theme import *

class Opening(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            include_background_plane=True,
            include_foreground_plane=False,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
        self.chrome = chrome(1, "Hook")
        self.add_foreground_mobject(self.chrome)
        # Opening frame
        card = Rectangle(width=config.frame_width, height=config.frame_height,
                         fill_color=BG, fill_opacity=1, stroke_width=0)
        info = VGroup(
            Text("Eigenvalues and Eigenvectors", font_size=44),
            Text("Linear Algebra and Calculus (M3) - Animation Project", font_size=26),
            Text("Name: Ishita Chaurasiya", font_size=28),
            Text("Student ID: E25B070845", font_size=28),
        ).arrange(DOWN, buff=0.4)
        self.add_foreground_mobject(card)
        self.add_foreground_mobject(info)
        self.wait(4)
        self.play(FadeOut(card), FadeOut(info))
        self.remove_foreground_mobject(card)
        self.remove_foreground_mobject(info)

        # Hook
        A = [[2, 1], [1, 2]]
        for coords in ([1, 0], [0, 1], [1, 2], [-1, 0], [0, -2]):
            self.add_vector(coords, color=GREY_B)
        self.add_vector([1, 1], color=BLUE)
        self.add_vector([1, -1], color=ORANGE)

        q1 = Text("A matrix transforms every vector.", font_size=30).to_edge(UP)
        q1.add_background_rectangle(opacity=0.8)
        self.add_foreground_mobject(q1)
        self.wait(3)

        self.apply_matrix(A)
        self.wait(2)

        self.remove_foreground_mobject(q1)
        self.play(FadeOut(q1))
        q2 = Text("Most vectors turn. Do any keep their direction?", font_size=30).to_edge(UP)
        q2.add_background_rectangle(opacity=0.8)
        self.add_foreground_mobject(q2)
        self.play(FadeIn(q2))
        self.wait(4)
