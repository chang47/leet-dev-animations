from manim import *

class AlgorithmIntroduction(Scene):
    def construct(self):
        #1 show logo
        self.wait(2)
        title = TextMobject("LeetDev.io", tex_to_color_map={"LeetDev": RED_C, ".io": WHITE}).scale(2)
        self.play(GrowFromCenter(title), run_time=1)
        self.wait(5)

        #2 show 2 pointer problem
        algorithm_text = TextMobject("2 Pointer Algorithm").scale(2)
        self.play(ReplacementTransform(title, algorithm_text))

        self.wait(1)

        #3 show array
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

        # Do a better animation
        self.play(FadeOut(algorithm_text), FadeIn(array_object))

        self.wait(1)

        #4 show forward and back pointer move
        front_arrow = Arrow(DOWN, UP)
        front_arrow.scale(0.5)
        front_arrow.next_to(arr[0]['group'], DOWN)

        back_arrow = Arrow(DOWN, UP)
        back_arrow.scale(0.5)
        back_arrow.next_to(arr[5]['group'], DOWN)
        arrow_runtime = 0.75
        self.play(FadeIn(front_arrow), FadeIn(back_arrow))

        self.wait(1)

        self.play(ApplyMethod(front_arrow.next_to, arr[1]['group'], DOWN, run_time=arrow_runtime))
        self.play(ApplyMethod(back_arrow.next_to, arr[4]['group'], DOWN), run_time=arrow_runtime)
        self.play(ApplyMethod(front_arrow.next_to, arr[2]['group'], DOWN), run_time=arrow_runtime)
        self.play(ApplyMethod(back_arrow.next_to, arr[3]['group'], DOWN), run_time=arrow_runtime)

        self.wait(1)

        #5 slow pointer and faster pointer move
        self.play(ApplyMethod(front_arrow.next_to, arr[0]['group'], DOWN, run_time=arrow_runtime), ApplyMethod(back_arrow.next_to, arr[0]['group'], DOWN, run_time=arrow_runtime))

        self.play(ApplyMethod(front_arrow.next_to, arr[1]['group'], DOWN, run_time=arrow_runtime))
        self.play(ApplyMethod(front_arrow.next_to, arr[2]['group'], DOWN, run_time=arrow_runtime))
        self.play(ApplyMethod(front_arrow.next_to, arr[3]['group'], DOWN, run_time=arrow_runtime))
        self.play(ApplyMethod(back_arrow.next_to, arr[1]['group'], DOWN, run_time=arrow_runtime))
        self.play(ApplyMethod(front_arrow.next_to, arr[4]['group'], DOWN, run_time=arrow_runtime))
        self.play(ApplyMethod(back_arrow.next_to, arr[2]['group'], DOWN, run_time=arrow_runtime))
        self.play(ApplyMethod(back_arrow.next_to, arr[3]['group'], DOWN, run_time=arrow_runtime))
        self.play(ApplyMethod(back_arrow.next_to, arr[4]['group'], DOWN, run_time=arrow_runtime))

        self.play(FadeOut(array_object), FadeOut(front_arrow), FadeOut(back_arrow))

class Six(Scene):
    def construct(self):
        problem = Text("Problem Introduction", color=WHITE)

        self.add(problem)
        self.wait(2)

class Seven(Scene):
    def construct(self):
        first = Text("Given an array of sorted integers, find two numbers", color=WHITE)
        second = Text("such that they add up to a target number.", color=WHITE)
        second.next_to(first, DOWN)

        self.play(Write(first, run_time=2))
        self.play(Write(second, run_time=2))
        
class HighLevel(Scene):
    def construct(self):
        # 8 Show the High Level Algorithm Text
        problem = Text("High Level Algorithm", color=WHITE).scale(2)

        self.play(FadeIn(problem, run_time=3))
        self.play(FadeOut(problem))

        self.wait(2)
        
        # 9 Show questions to ask
        first = TextMobject("Questions to ask:").scale(2)
        rec = VGroup(first)
        rec.move_to(UP*2 + LEFT*2)

        third = TextMobject("* What does my input look like?").scale(1.25)
        four = TextMobject("* Will the sum cause integer overflow?").scale(1.25)
        # five = TextMobject("* Is there guaranteed to be an answer?").scale(1.25) # script forgot to say it

        # https://www.reddit.com/r/manim/comments/iupbe8/how_to_left_align_textmobject/
        self.play(Write(rec, run_time=2))
        self.wait(2)
        rec.add(third)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(third, run_time=2))
        rec.add(four)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(four, run_time=3))
        
        # Forgot to include it in the script
        # rec.add(five)
        # rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        # self.play(Write(five, run_time=2))
        # self.wait(1)

        # Fade out the rectangle holding all the text 
        self.wait(2)
        self.play(FadeOut(rec))

        # #10 N^2 array
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
        
        arrow1 = Arrow(DOWN, UP)
        arrow1.scale(0.5)
        arrow1.next_to(arr[0]['group'], DOWN)
        
        arrow2 = Arrow(DOWN, UP)
        arrow2.scale(0.5)
        arrow2.next_to(arr[0]['group'], DOWN)
        
        self.play(FadeIn(arrow1), FadeIn(arrow2))
        arrow_runtime=0.8
        for i in range(6):
            # Move both indexes together
            self.play(ApplyMethod(arrow1.next_to, arr[i]['group'], DOWN, run_time=arrow_runtime), ApplyMethod(arrow2.next_to, arr[i]['group'], DOWN, run_time=arrow_runtime))
            for j in range(i, 6):
                self.play(ApplyMethod(arrow2.next_to, arr[j]['group'], DOWN, run_time=arrow_runtime))

        self.play(FadeOut(array_object), FadeOut(arrow1), FadeOut(arrow2))

class FindBetterAnswer(Scene):
    def construct(self):
        first = TextMobject("How to find better solutions:").scale(1.5)
        rec = VGroup(first)
        rec.move_to(UP*2 + LEFT*2)

        third = TextMobject("* Find insights from simple solution or problem statement").scale(1)
        four = TextMobject("* Ask for a hint").scale(1)
        five = TextMobject("* Find algorithms based off of runtimes").scale(1)

        # https://www.reddit.com/r/manim/comments/iupbe8/how_to_left_align_textmobject/
        self.play(Write(rec, run_time=3))
        rec.add(third)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(third, run_time=2))
        self.wait(6)
        rec.add(four)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(four, run_time=2))
        self.wait(8)
        rec.add(five)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(five, run_time=2))
        self.wait(7)
        self.play(FadeOut(rec))

class NLogNText(Scene):
    def construct(self):
        problem = Text("O(N Log N) > O(N²)",).scale(1.3)

        self.play(FadeIn(problem))
        self.wait(7)
        self.play(FadeOut(problem))

        first = TextMobject("O(N Log N) Algo:").scale(1.5)
        rec = VGroup(first)
        rec.move_to(UP*2 + LEFT*2)

        third = TextMobject("* Sort and scan").scale(1)
        four = TextMobject("* Scan through array and use binary search").scale(1)

        # https://www.reddit.com/r/manim/comments/iupbe8/how_to_left_align_textmobject/
        self.play(Write(rec, run_time=2))
        rec.add(third)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(third, run_time=2))
        self.wait(5)
        rec.add(four)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(four, run_time=2))
        self.wait(20)
        self.play(FadeOut(rec))
        # Finsh around the 3:28 mark
    
class BinarySearch(Scene):
    def construct(self):
        #13 N Log N binary Search
        arr = []
        array_object = Group()
        prev = None

        # 0 1 2 3 4 5 6 7
        # target = 5 
        for i in range(8):
            obj = {}
            value = TextMobject(str(i))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * i)
            obj['group'] = group
            arr.append(obj)
            array_object.add(group)

        array_object.center()
        self.play(FadeIn(array_object, run_time=2))

        # Setup variable text
        index_text = Text("arr index:")
        index_value = Text("0")
        index_text.to_corner(corner=UP + LEFT)
        index_value.next_to(index_text, RIGHT)

        target_text = Text("target:  ")
        target_value = Text("5")
        target_text.next_to(index_text, DOWN)
        target_value.next_to(target_text, RIGHT)
        
        sum_text = Text("sum:   ")
        sum_value = Text("0")
        sum_text.next_to(target_text, DOWN)
        sum_value.next_to(sum_text, RIGHT)

        arrow = Arrow(DOWN, UP)
        arrow.scale(0.5)
        arrow.next_to(arr[0]['group'], DOWN)

        self.wait(11)
        self.play(FadeIn(arrow), FadeIn(index_text), FadeIn(index_value), FadeIn(target_value), FadeIn(target_text))
        # 3:50
        self.wait(2)

        lo = TextMobject("lo")
        lo.next_to(arr[1]['group'], DOWN)
        mid = TextMobject("mid")
        mid.next_to(arr[4]['group'], DOWN)
        hi = TextMobject("hi")
        hi.next_to(arr[7]['group'], DOWN)

        # show everything
        self.play(FadeIn(lo), FadeIn(hi))
        self.wait(2)
        # 3:55
        self.play(FadeIn(mid))
        self.play(FadeIn(sum_text), FadeIn(sum_value))
        self.wait(5)

        # 4:02
        new_sum_value = self.replace_value_animation(sum_value, "0 + 4 = 4", sum_text)
        self.play(FadeOut(sum_value), FadeIn(new_sum_value))
        sum_value = new_sum_value
        self.wait(4)

        # 4:06

        # move lo to mid+1 (5) because mid + i is too small
        self.play(FadeOut(mid))
        self.play(ApplyMethod(lo.next_to, arr[5]['group'], DOWN))
        
        # show mid at index 6
        mid.next_to(arr[6]['group'], DOWN)
        self.play(FadeIn(mid))
        self.wait(2)

        # 4:11

        new_value = self.replace_value_animation(sum_value, "0 + 6 = 6", sum_text)
        self.play(FadeOut(sum_value), FadeIn(new_value))
        sum_value = new_value
        self.wait(2)

        # 4:14

        # move hi to mid-1 (5) because mid + i is too big
        self.play(FadeOut(mid)) 
        self.play(ApplyMethod(hi.next_to, lo, DOWN)) 
        self.wait(1)

        # 4:17
        
        # show mid at index 5
        new_value = self.replace_value_animation(sum_value, "0 + 5 = 5", sum_text)
        mid.next_to(hi, DOWN)
        self.play(FadeIn(mid))
        self.wait(1)
        self.play(FadeOut(sum_value), FadeIn(new_value))
        sum_value = new_value
        circle = Circle()
        circle.surround(target_value)
        self.wait(1)
        self.play(FadeIn(circle))
        self.wait(12)
        self.play(FadeOut(mid), FadeOut(sum_value), FadeOut(sum_text), FadeOut(target_text), FadeOut(target_value), FadeOut(index_text), 
                    FadeOut(index_value), FadeOut(array_object), FadeOut(arrow), FadeOut(lo), FadeOut(hi), FadeOut(mid), FadeOut(circle))

    # given an old text value object, create a new text object with the new text value
    # plays an animation with the new value appearing and the old value fading, and then
    # returns an instance to the new text object
    def replace_value_animation(self, val_object, val, text_object):
        new_object = Text(val)
        new_object.next_to(text_object, RIGHT)
        # self.play(FadeIn(new_object), FadeOut(text_object))
        return new_object

class TwoPointer(Scene):
    def construct(self):
        #14 animation of O(N) > O(N Log N)
        problem = Text("O(N) > O(N Log N)",).scale(2)

        self.play(FadeIn(problem))
        self.play(FadeOut(problem))

        #15 regular O(N) scan
        arr = []
        array_object = Group()
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

        arrow = Arrow(DOWN, UP)
        arrow.scale(0.5)
        arrow.next_to(arr[0]['group'], DOWN)

        self.play(FadeIn(arrow))

        self.play(ApplyMethod(arrow.next_to, arr[5]['group'], DOWN, run_time=1))

        self.play(FadeOut(arrow), FadeOut(array_object))

        #16 show 2 pointer array 
        arr = []
        array_object = Group()
        i = 0
        for val in [1,3,5,6,7]:
            obj = {}
            value = TextMobject(str(val))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * i)
            obj['group'] = group
            arr.append(obj)
            array_object.add(group)
            i+=1

        array_object.center()

        left = Text("L")
        left.next_to(arr[0]['group'], DOWN)

        right = Text("R")
        right.next_to(arr[4]['group'], DOWN)
        
        self.play(FadeIn(array_object), FadeIn(left), FadeIn(right))

        #17 Animation
        # 1 3 5 6 7 Target: 9
        target_text = TextMobject("Target:")
        sum_text = TextMobject("Sum:")
        l_text = TextMobject("L:")
        r_text = TextMobject("R:")
        text_group = VGroup()
        text_group.add(target_text)
        text_group.add(sum_text)
        text_group.add(l_text)
        text_group.add(r_text)
        text_group.to_corner(corner=UP+LEFT)
        text_group.arrange(DOWN, center=False, aligned_edge=LEFT)
        
        # Setup variable value
        target_value = TextMobject("9")
        sum_value = TextMobject("8")
        l_value = TextMobject("1")
        r_value = TextMobject("7")
        value_group = VGroup()
        value_group.add(target_value)
        value_group.add(sum_value)
        value_group.add(l_value)
        value_group.add(r_value)
        value_group.arrange(DOWN, center=False, aligned_edge=LEFT)
        value_group.next_to(text_group, RIGHT*2)

        self.play(FadeIn(text_group), FadeIn(value_group))

        l_value = self.moveArrowAndChangeText(l_value, "3", left, arr, 1) # l -> 3
        sum_value = self.changeSum(sum_value, "10")
        r_value = self.moveArrowAndChangeText(r_value, "6", right, arr, 3) # r -> 6
        sum_value = self.changeSum(sum_value, "9")

    def moveArrowAndChangeText(self, text_object, new_value, position_object, arr, new_index):
        new_object = TextMobject(new_value)
        new_object.set_x(text_object.get_x()).set_y(text_object.get_y())
        self.play(ApplyMethod(position_object.next_to, arr[new_index]['group'], DOWN))
        self.play(FadeOut(text_object), FadeIn(new_object))
        return new_object

    def changeSum(self, text_object, new_value):
        new_object = TextMobject(new_value)
        new_object.set_x(text_object.get_x()).set_y(text_object.get_y())
        self.play(FadeOut(text_object), FadeIn(new_object))
        return new_object

class CodeWalkthrough(Scene):
    def construct(self):
        #18 - 21: Note we're still missing the portion of the code where we just walk through the code
        line1 = Text("public boolean twoSum(int[] nums, int target) {")
        line2 = Text("\tint left = 0;")
        line3 = Text("\tint right = nums.length - 1;")
        line4 = Text("\twhile (left < right) {")
        line5 = Text("\t\tint sum = nums[left] + nums[right];")
        line6 = Text("\t\tif (sum == target) {")
        line7 = Text("\t\t\treturn new int[]{left+1,right+1};")
        line8 = Text("\t\t} else if (sum <= target) {")
        line9 = Text("\t\t\tleft++;")
        line10 = Text("\t\t} else {")
        line11 = Text("\t\t\tright--;")
        line12 = Text("\t\t}")
        line13 = Text("\t}")
        line14 = Text("\treturn new int[2];")
        line15 = Text("}")
        
        code = VGroup()
        code.add(line1)
        code.add(line2)
        code.add(line3)
        code.add(line4)
        code.add(line5)
        code.add(line6)
        code.add(line7)
        code.add(line8)
        code.add(line9)
        code.add(line10)
        code.add(line11)
        code.add(line12)
        code.add(line13)
        code.add(line14)
        code.add(line15)
        code.arrange(DOWN, center=False, aligned_edge=LEFT)
        code.scale(0.5)
        code.center()
        code.to_edge(LEFT)
        code.shift(RIGHT)

        # show the code
        self.play(FadeIn(code))

        # Show the array on the top right corner
        arr = []
        array_object = Group()
        i = 0
        for val in [1,3,5,6,7]:
            obj = {}
            value = TextMobject(str(val))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * i)
            obj['group'] = group
            arr.append(obj)
            array_object.add(group)
            i+=1

        array_object.scale(0.75)
        array_object.to_corner(RIGHT+UP)

        self.play(FadeIn(array_object))

        array_variable_text = Text("nums:")
        array_variable_text.next_to(array_object, LEFT)
        self.play(FadeIn(array_variable_text))
        
        target_text = Text("target:")
        target_value = Text("9")
        target_text.next_to(array_variable_text, DOWN*3)
        target_value.next_to(target_text, RIGHT)
        self.play(FadeIn(target_text), FadeIn(target_value))
        
        # show the arrow
        arrow = Arrow(LEFT, RIGHT)
        arrow.scale(0.5)
        arrow.next_to(line1, LEFT)
        self.play(FadeIn(arrow))
        
        self.play(ApplyMethod(arrow.next_to, line2, LEFT))

        left_text = Text("left:  ")
        left_value = Text("0")
        left_text.next_to(target_text, DOWN)
        left_value.next_to(left_text, RIGHT)
        self.play(FadeIn(left_text), FadeIn(left_value))

        self.play(ApplyMethod(arrow.next_to, line3, LEFT))

        right_text = Text("right: ")
        right_value = Text("4")
        right_text.next_to(left_text, DOWN)
        right_value.next_to(right_text, RIGHT)
        self.play(FadeIn(right_text), FadeIn(right_value))

        self.play(ApplyMethod(arrow.next_to, line3, LEFT))

        self.play(ApplyMethod(arrow.next_to, line4, LEFT))
        self.play(ApplyMethod(arrow.next_to, line5, LEFT))

        sum_text = Text("sum: ")
        sum_value = Text("8")
        sum_text.next_to(right_text, DOWN)
        sum_value.next_to(sum_text, RIGHT)
        self.play(FadeIn(sum_text), FadeIn(sum_value))

        self.play(ApplyMethod(arrow.next_to, line6, LEFT))
        self.jumpArrow(arrow, line8)
        self.play(ApplyMethod(arrow.next_to, line9, LEFT))
        left_value = self.changeText(left_text, "1", left_value)
        
        self.jumpArrow(arrow, line4)
        self.play(ApplyMethod(arrow.next_to, line5, LEFT))
        sum_value = self.changeText(sum_text, "10", sum_value)

        self.play(ApplyMethod(arrow.next_to, line6, LEFT))
        self.jumpArrow(arrow, line8)
        self.jumpArrow(arrow, line10)
        self.play(ApplyMethod(arrow.next_to, line11, LEFT))
        right_value = self.changeText(right_text, "3", right_value)

        self.jumpArrow(arrow, line4)
        self.play(ApplyMethod(arrow.next_to, line5, LEFT))
        sum_value = self.changeText(sum_text, "9", sum_value)
        
        self.play(ApplyMethod(arrow.next_to, line6, LEFT))
        self.play(ApplyMethod(arrow.next_to, line7, LEFT))

        # Make everything disapear
        self.play(FadeOut(arrow), FadeOut(code), FadeOut(sum_text), FadeOut(sum_value), FadeOut(right_text),
                  FadeOut(right_value), FadeOut(left_text), FadeOut(left_value), FadeOut(array_variable_text), 
                  FadeOut(array_object), FadeOut(target_text), FadeOut(target_value))
    
    def changeText(self, text_object, new_value, value_object):
        new_object = TextMobject(new_value)
        new_object.next_to(text_object, RIGHT)
        self.play(FadeOut(value_object), FadeIn(new_object))
        return new_object

    def jumpArrow(self, arrow, line):
        self.play(FadeOut(arrow, run_time=.5))
        arrow.next_to(line, LEFT)
        self.play(FadeIn(arrow, run_time=.5))


class EdgeCases(Scene):
    def construct(self):
        # 22 Show aniamtion of list edge cases
        problem = Text("Edge Cases", color=WHITE).scale(2)
        problem.generate_target()
        problem.target.to_corner(UP+LEFT)
        problem.target.scale(0.65)

        # Maybe just move it to the top left corner instead of fading away
        self.play(FadeIn(problem))
        self.wait(1)
        self.play(MoveToTarget(problem, run_time=2))
        
        first = TextMobject("Questions to ask:").scale(1.5)
        rec = VGroup(first)
        rec.move_to(UP*2 + LEFT*2)

        second = TextMobject("* What if there's no solutions?").scale(1.25)
        third = TextMobject("* What if there's negative numbers?").scale(1.25)
        four = TextMobject("* What if there are duplicates?").scale(1.25)
        five = TextMobject("* What if the array wasn't sorted?").scale(1.25)

        # https://www.reddit.com/r/manim/comments/iupbe8/how_to_left_align_textmobject/
        self.play(Write(rec, run_time=0.75))
        self.wait(1.5)
        rec.add(second)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(second, run_time=0.75))
        self.wait(1.5)
        rec.add(third)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(third, run_time=0.75))
        self.wait(1.5)
        rec.add(four)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(four, run_time=0.75))
        self.wait(1.5)
        rec.add(five)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(five, run_time=0.75))
        self.wait(1.5)

        # Fade out the rectangle holding all the text 
        self.play(FadeOut(rec), FadeOut(problem))

class IdentifyProblem(Scene):
    def construct(self):
        # 23 Show animation of the new section
        problem = Text("Identifying Problem", color=WHITE).scale(2)
        problem.generate_target()
        problem.target.to_corner(UP+LEFT)
        problem.target.scale(0.65)

        # Maybe just move it to the top left corner instead of fading away
        self.play(FadeIn(problem))
        self.wait(1)
        self.play(MoveToTarget(problem, run_time=2))

        identify = Text("Find a pair of numbers in an array", color=WHITE).scale(1.5)
        self.play(FadeIn(identify))


class Smart(Scene):
    def construct(self):
        nums = []
        nums_group = Group()
        i = 0
        for num in [2,4,5,7,11,15]:
            value = TextMobject(str(num))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square)
            nums_group.add(group.shift(RIGHT * i))
            nums.append({
                'group': group,
                'num': num
            })
            i += 1

        nums_group.set_x(0)
        nums_group.set_y(0)
        self.play(FadeIn(nums_group))

        lo_ptr = Arrow(DOWN, UP).scale(0.5).next_to(nums[0]['group'], DOWN)
        lo_group = Group(TextMobject("front").scale(0.75).next_to(lo_ptr, DOWN), lo_ptr)

        hi_ptr = Arrow(DOWN, UP, color=BLUE).scale(0.5).next_to(nums[5]['group'], DOWN)
        hi_group = Group(TextMobject("back", color=BLUE).scale(0.75).next_to(hi_ptr, DOWN), hi_ptr)

        total = TextMobject(f"sum = {nums[0]['num'] + nums[5]['num']}").next_to(nums_group, UP)
        self.play(FadeIn(lo_group), FadeIn(hi_group), FadeIn(total))

        lo = 0
        hi = 5
        i = 0
        while lo + 1 < hi:
            if i % 2 == 0:
                lo = lo+1
                total_new = TextMobject(f"sum = {nums[lo]['num'] + nums[hi]['num']}").next_to(nums_group, UP)
                self.play(ApplyMethod(lo_group.next_to, nums[lo]['group'], DOWN), Transform(total, total_new))
            else:
                hi = hi-1
                total_new = TextMobject(f"sum = {nums[lo]['num'] + nums[hi]['num']}").next_to(nums_group, UP)
                self.play(ApplyMethod(hi_group.next_to, nums[hi]['group'], DOWN), Transform(total, total_new))

            self.wait(1)
            i += 1

class BruteForce(Scene):
    def construct(self):
        nums = []
        nums_group = Group()
        i = 0
        for num in [2,7,11,15]:
            value = TextMobject(str(num))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square)
            nums_group.add(group.shift(RIGHT * i))
            nums.append({
                'group': group,
                'num': num
            })
            i+=1

        nums_group.set_x(0)
        nums_group.set_y(0)
        self.play(FadeIn(nums_group))

        lo_ptr = Arrow(DOWN, UP).scale(0.5).next_to(nums[0]['group'], DOWN)
        lo_group = Group(TextMobject("slow").scale(0.75).next_to(lo_ptr, DOWN), lo_ptr)

        for lo in range(3):
            self.play(ApplyMethod(lo_group.next_to, nums[lo]['group'], DOWN))

            hi_ptr = Arrow(DOWN, UP, color=BLUE).scale(0.5).next_to(nums[lo]['group'], DOWN)
            hi_group = Group(TextMobject("fast", color=BLUE).scale(0.75).next_to(hi_ptr, DOWN), hi_ptr)

            for hi in range(lo + 1, 4):
                self.play(ApplyMethod(hi_group.next_to, nums[hi]['group'], DOWN))
                total = TextMobject(f"sum = {nums[lo]['num'] + nums[hi]['num']}")
                total.next_to(nums_group, UP)
                self.play(Write(total))
                self.wait(.5)
                self.play(FadeOut(total))

            self.play(FadeOut(hi_group))