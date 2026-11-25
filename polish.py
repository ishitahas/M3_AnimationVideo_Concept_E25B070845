import pathlib

scenes = {
    "scene1_opening.py": (1, "Hook", True),
    "scene2_definition.py": (2, "Definition", False),
    "scene3_intuition.py": (3, "Visual intuition", True),
    "scene4_example.py": (4, "Worked example", False),
    "scene5_interpretation.py": (5, "Interpretation", False),
    "scene6_summary.py": (6, "Summary", False),
}

for f, (n, name, linear) in scenes.items():
    p = pathlib.Path(f)
    s = p.read_text()
    if "from theme import" in s:
        continue
    s = s.replace("from manim import *", "from manim import *\nfrom theme import *", 1)
    add = "self.add_foreground_mobject(self.chrome)" if linear else "self.add(self.chrome)"
    s = s.replace(
        "    def construct(self):\n",
        f'    def construct(self):\n        self.chrome = chrome({n}, "{name}")\n        {add}\n',
        1,
    )
    s = s.replace("fill_color=BLACK", "fill_color=BG")
    s = s.replace("m is not title]", "m is not title and m is not self.chrome]")
    s = s.replace("self.add(plane)", "self.add(plane)\n        self.add(self.chrome)")
    p.write_text(s)
    print("patched", f)
