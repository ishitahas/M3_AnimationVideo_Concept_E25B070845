from manim import *
from theme import *

class Intuition(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            include_background_plane=True,
            include_foreground_plane=True,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
        self.chrome = chrome(3, "Visual intuition")
        self.add_foreground_mobject(self.chrome)
        A = [[2, 1], [1, 2]]

        title = Text("Matrix A = [[2, 1], [1, 2]]", font_size=30).to_edge(UP)
        self.add_foreground_mobject(title)

        v1 = self.add_vector([1, 1], color=BLUE)
        v2 = self.add_vector([1, -1], color=ORANGE)
        self.wait(1)

        self.apply_matrix(A)
        self.wait(2)
