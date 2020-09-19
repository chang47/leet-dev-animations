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


class TwoPointer(Scene):
    def construct(self):
        # 1
        title = TextMobject("LeetDev.io", tex_to_color_map={"LeetDev": RED_C, ".io": WHITE}).scale(2)
        self.play(GrowFromCenter(title))
        
        #2
        algorithm_text = TextMobject("2 Pointer Algorithm").scale(2)
        self.play(ReplacementTransform(title, algorithm_text))

        #3
        arr = []
        array_object = Group()
        prev = None
        for i in range(6):
            obj = {}
            value = TextMobject(str(i))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * i)
            # obj['value'] = value
            # obj['square'] = square
            # obj['group'] = group
            # arr.append(obj)
            array_object.add(group)

        array_object.center()

        # Do a better animation
        self.play(FadeOut(algorithm_text), FadeIn(array_object))

        