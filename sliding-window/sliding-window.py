from manim import *

class Intro(Scene):
    def construct(self):
        slidingWindow = ImageMobject('image/window.png').scale(1.5).shift(LEFT*9)

        self.play(ApplyMethod(slidingWindow.shift, RIGHT * 9))
        self.wait(1)
        text = TextMobject("Sliding Window").scale(1.5)
        algo = TextMobject("Algorithm").scale(1.5)
        algo.next_to(slidingWindow, UP)
        text.next_to(algo, UP)
        self.play(Write(text), Write(algo))
        self.wait(1)

class ProblemIntro(Scene):
    def construct(self):
        first = Text("Given an array of positive integers and a positive integer s,").scale(0.75)
        second = Text("find the minimal length of a continuous subarray of which the sum ≥ s.").scale(0.75)
        group = Group(first)
        group.add(second)
        second.next_to(first, DOWN)
        group.center()

        self.play(Write(first, run_time=2))
        self.play(Write(second, run_time=2))
        self.wait(1)

class AlgorithmIntro(Scene):
    def construct(self):
        first = Text("The sliding window algorithm is a technique that optimizes array").scale(0.75)
        second = Text("problems by reducing a brute force O(N²) solution to be a O(N)").scale(0.75)
        group = Group(first)
        group.add(second)
        second.next_to(first, DOWN)
        group.center()

        self.play(Write(first, run_time=2))
        self.play(Write(second, run_time=2))
        self.wait(1)

class IdentifyAlgorithm(Scene):
    def construct(self):
        # first = Text("How to identfiy:").scale(0.75)
        # second = Text("• Problem asks you to find the longest sequence in an").scale(0.75)
        # third = Text("  array/string that fulfills a condition.").scale(0.75)
        # group = Group(first)
        # group.add(second)
        # group.add(third)
        # second.next_to(first, DOWN)
        # third.next_to(second, DOWN)
        # group.center()

        # self.play(Write(first, run_time=2))
        # self.play(Write(second, run_time=2))
        # self.play(Write(third, run_time=2))
        # self.wait(1)


        first = TextMobject("How to identfiy:").scale(1.5)
        rec = VGroup(first)
        rec.move_to(UP*2 + LEFT*3)

        third = TextMobject("• Problem asks you to find the longest sequence in an").scale(0.75)
        four = TextMobject("array/string that fulfills a condition.").scale(0.75)

        # https://www.reddit.com/r/manim/comments/iupbe8/how_to_left_align_textmobject/
        self.play(Write(rec, run_time=2))
        rec.add(third)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(third, run_time=2))
        rec.add(four)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        four.shift(RIGHT*0.3)
        self.play(Write(four, run_time=2))
        self.wait(1)