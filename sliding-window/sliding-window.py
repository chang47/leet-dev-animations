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

class ArrayPermutation(Scene):
    def construct(self):
        pointer = CurvedArrow(start_point=2 * RIGHT, end_point=5 * RIGHT)
        # self.play(FadeIn(pointer))
        # path = VMobject()
        # path.set_points_as_corners([np.array([1,1,0]), np.array([1,3,0]), np.array([2,2,0])])
        # self.play(FadeIn(path))

        arr = []
        array_object = Group()
        prev = None
        for i in range(6):
            obj = {}
            value = TextMobject(str(i))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * i)
            obj['value'] = value
            obj['square'] = square
            obj['group'] = group
            arr.append(obj)
            array_object.add(group)

        array_object.center()
        self.play(FadeIn(array_object))

        # print(array_object[0]['group'].get_y())
        for i in range(1, len(arr)):
            g = Group()
            for j in range(i, len(arr)):
                pointer = CurvedArrow(start_point=arr[i-1]['group'].get_center(), end_point=arr[j]['group'].get_center()).shift(DOWN*(0.5+(i-1)*0.5))
                self.play(FadeIn(pointer))
                g.add(pointer)
            # self.play(FadeOut(g))
        self.wait(1)
        
class ArrayWindowOptimization(Scene):
    def construct(self):
        pointer = CurvedArrow(start_point=2 * RIGHT, end_point=5 * RIGHT)
        
        arr = []
        array_object = Group()
        prev = None
        for i in range(6):
            obj = {}
            value = TextMobject(str(i))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * i)
            obj['value'] = value
            obj['square'] = square
            obj['group'] = group
            arr.append(obj)
            array_object.add(group)

        array_object.center()
        self.play(FadeIn(array_object))

        pointer = CurvedArrow(start_point=arr[0]['group'].get_center(), end_point=arr[1]['group'].get_center()).shift(DOWN*0.5)
        self.play(FadeIn(pointer))
        pointer.target = CurvedArrow(start_point=arr[0]['group'].get_center(), end_point=arr[2]['group'].get_center()).shift(DOWN*0.5)
        self.play(MoveToTarget(pointer))
        pointer.target = CurvedArrow(start_point=arr[0]['group'].get_center(), end_point=arr[3]['group'].get_center()).shift(DOWN*0.5)
        self.play(MoveToTarget(pointer))
        pointer.target = CurvedArrow(start_point=arr[1]['group'].get_center(), end_point=arr[3]['group'].get_center()).shift(DOWN*0.5)
        self.play(MoveToTarget(pointer))
        pointer.target = CurvedArrow(start_point=arr[2]['group'].get_center(), end_point=arr[3]['group'].get_center()).shift(DOWN*0.5)
        self.play(MoveToTarget(pointer))
        pointer.target = CurvedArrow(start_point=arr[2]['group'].get_center(), end_point=arr[4]['group'].get_center()).shift(DOWN*0.5)
        self.play(MoveToTarget(pointer))
        pointer.target = CurvedArrow(start_point=arr[3]['group'].get_center(), end_point=arr[4]['group'].get_center()).shift(DOWN*0.5)
        self.play(MoveToTarget(pointer))
        pointer.target = CurvedArrow(start_point=arr[3]['group'].get_center(), end_point=arr[5]['group'].get_center()).shift(DOWN*0.5)
        self.play(MoveToTarget(pointer))

class ThreeStep(Scene):
    def construct(self):
        first = TextMobject("3 Step implementation:").scale(1.5)
        rec = VGroup(first)
        rec.move_to(UP*2 + LEFT*2)

        third = TextMobject("1) Define a condition to keep increasing your window").scale(0.75)
        four = TextMobject("2) Move forward pointer until condition is false.").scale(0.75)
        five = TextMobject("3) Move back pointer until condition is true.").scale(0.75)

        # https://www.reddit.com/r/manim/comments/iupbe8/how_to_left_align_textmobject/
        self.play(Write(rec, run_time=2))
        rec.add(third)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(third, run_time=1.5))
        self.wait(1)
        rec.add(four)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(four, run_time=1.5))
        self.wait(1)
        rec.add(five)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(five, run_time=1.5))
        self.wait(1)

class ThreeStepExample(Scene):
    def construct(self):
        first = TextMobject("Example problem 3 Step implementation:").scale(1.5)
        rec = VGroup(first)
        rec.move_to(UP*2 + LEFT*2)

        third = TextMobject("1) Condition: sum is less than the given number").scale(0.75)
        four = TextMobject("2) Move front if sum < x.").scale(0.75)
        five = TextMobject("3) Move back if sum > x.").scale(0.75)

        # https://www.reddit.com/r/manim/comments/iupbe8/how_to_left_align_textmobject/
        self.play(Write(rec, run_time=2))
        rec.add(third)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(third, run_time=1.5))
        self.wait(1)
        rec.add(four)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(four, run_time=1.5))
        self.wait(1)
        rec.add(five)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(five, run_time=1.5))
        self.wait(1)

class SlidingWindowExample(Scene):
    def construct(self):
        title = TextMobject("Sliding Window Example")
        title.align_on_border(UP)
        self.play(FadeIn(title))

        arr = []
        array_object = Group()
        i = 0
        nums = [2,3,1,2,4,3]
        for n in nums:
            value = TextMobject(str(n))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * i)
            arr.append(group)
            array_object.add(group)
            i += 1

        array_object.center().shift(DOWN)

        target_s = TextMobject("Target Sum: 7").scale(0.75).next_to(title, DOWN*2)
        current_s = TextMobject("Current Sum: 0").scale(0.75).next_to(target_s, DOWN)
        length_text = TextMobject("Length: 9999999").scale(0.75).next_to(current_s, DOWN)
        f_index = TextMobject("Front: 0").scale(0.75).next_to(length_text, DOWN)
        b_index = TextMobject("Back: 0").scale(0.75).next_to(f_index, DOWN)

        self.play(Write(target_s))
        self.play(Write(current_s))
        self.play(Write(length_text))
        self.play(Write(f_index))
        self.play(Write(b_index))

        self.play(ShowCreation(array_object))

        fa = Arrow(DOWN, UP).scale(0.5).next_to(arr[0], DOWN)
        ba = Arrow(DOWN, UP).scale(0.5).next_to(arr[0], DOWN)
        self.play(ShowCreation(fa), ShowCreation(ba))

        s = 7
        front = 0
        back = 0
        windowSum = 0
        length = 99999999
        while (front < len(nums)):
            windowSum += nums[front]
            self.transformText(current_s, "Current Sum: " + str(windowSum), target_s)
            self.wait(1)

            while (windowSum >= s and back < front):
                length = min(front+1-back, length)
                self.transformText(length_text, "Length: (" + str(front) + " + 1) - " + str(back) + " = " + str(length), current_s)
                self.wait(1)
                windowSum -= nums[back]
                self.transformText(current_s, "Current Sum: " + str(windowSum), target_s)
                self.wait(1)
                back += 1
                self.play(ApplyMethod(ba.next_to, arr[back], DOWN))
                self.transformText(b_index, "Back: " + str(back), f_index)
                self.wait(1)
            
            front += 1
            if (front == len(arr)):
                self.play(ApplyMethod(fa.shift, RIGHT))
            else:
                self.play(ApplyMethod(fa.next_to, arr[front], DOWN))
            self.transformText(f_index, "Front: " + str(front), length_text)
            self.wait(1)
                

    def transformText(self, text, value, location):
        text.target = Tex(value).scale(0.75).next_to(location, DOWN)
        self.play(MoveToTarget(text))

class Conclusion(Scene):
    def construct(self):
        first = Tex("Conclusion").scale(1.5)
        rec = VGroup(first)
        rec.move_to(LEFT*4)
        self.play(Write(rec, run_time=1))
        self.wait(1)