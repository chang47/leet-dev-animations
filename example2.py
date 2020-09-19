from manim import *

class GroupExample(Scene):
    def construct(self):
        t1 = TextMobject("0", tex_to_color_map={"Text": YELLOW})
        s1 = Square().surround(t1).set_width(1).set_height(1)
        g1 = Group(s1, t1)
        t2 = TextMobject("1", tex_to_color_map={"Text": YELLOW})
        s2 = Square().surround(t2).set_width(1).set_height(1)
        g2 = Group(s2, t2).shift(RIGHT)
        t3 = TextMobject("2", tex_to_color_map={"Text": YELLOW})
        s3 = Square().surround(t3).set_width(1).set_height(1)
        g3 = Group(s3, t3).shift(RIGHT*2)
        arrow = Arrow(DOWN, UP)
        arrow.scale(0.5)
        arrow.next_to(g1, DOWN)
        
        array = Group(g1, g2, g3)

        # We can run multiple animations at the same time
        self.play(FadeIn(array), FadeIn(arrow))
        s1.set_fill(GOLD_B, 0.5)
        self.wait(0.5)
        s1.set_fill(GOLD_B, 0)
        s2.set_fill(GOLD_B, 0.5)
        self.play(ApplyMethod(arrow.next_to, g2, DOWN, run_time=0.1))
        # arrow.next_to(g2, DOWN)
        self.wait(0.5)
        s2.set_fill(GOLD_B, 0)
        s3.set_fill(GOLD_B, 0.5)
        self.play(ApplyMethod(arrow.next_to, g3, DOWN))
        self.wait()