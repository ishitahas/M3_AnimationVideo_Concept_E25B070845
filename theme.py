from manim import *

BG = "#0B1220"
PANEL = "#16213A"
C_V1 = "#38BDF8"
C_V2 = "#FB923C"
C_ACC = "#FACC15"
TXT = "#E2E8F0"

config.background_color = BG

def chrome(n, name, total=6):
    w = config.frame_width
    strip = Rectangle(width=w, height=0.4, fill_color=PANEL,
                      fill_opacity=1, stroke_width=0).to_edge(UP, buff=0)
    left = Text("Eigenvalues & Eigenvectors  |  M3", font_size=16,
                color=TXT).move_to(strip).align_to(strip, LEFT).shift(RIGHT * 0.3)
    right = Text(f"{n}. {name}", font_size=16,
                 color=C_ACC).move_to(strip).align_to(strip, RIGHT).shift(LEFT * 0.3)
    track = Rectangle(width=w, height=0.07, fill_color=PANEL,
                      fill_opacity=1, stroke_width=0).to_edge(DOWN, buff=0)
    fill = Rectangle(width=w * n / total, height=0.07, fill_color=C_V1,
                     fill_opacity=1, stroke_width=0)
    fill.align_to(track, DOWN).align_to(track, LEFT)
    return VGroup(strip, left, right, track, fill)

Text.set_default(font="Avenir Next", color=TXT)
