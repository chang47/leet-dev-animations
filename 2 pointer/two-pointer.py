from manim import *

class AlgorithmIntroduction(Scene):
    def construct(self):
        #1 show logo
        title = TextMobject("LeetDev.io", tex_to_color_map={"LeetDev": RED_C, ".io": WHITE}).scale(2)
        self.play(GrowFromCenter(title))
        
        #2 show 2 pointer problem
        algorithm_text = TextMobject("2 Pointer Algorithm").scale(2)
        self.play(ReplacementTransform(title, algorithm_text))

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

        #4 show forward and back pointer move
        front_arrow = Arrow(DOWN, UP)
        front_arrow.scale(0.5)
        front_arrow.next_to(arr[0]['group'], DOWN)

        back_arrow = Arrow(DOWN, UP)
        back_arrow.scale(0.5)
        back_arrow.next_to(arr[5]['group'], DOWN)
        arrow_runtime = 0.75
        self.play(FadeIn(front_arrow), FadeIn(back_arrow))
        self.play(ApplyMethod(front_arrow.next_to, arr[1]['group'], DOWN, run_time=arrow_runtime))
        self.play(ApplyMethod(back_arrow.next_to, arr[4]['group'], DOWN), run_time=arrow_runtime)
        self.play(ApplyMethod(front_arrow.next_to, arr[2]['group'], DOWN), run_time=arrow_runtime)
        self.play(ApplyMethod(back_arrow.next_to, arr[3]['group'], DOWN), run_time=arrow_runtime)

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
        first = Text("Given an array of integers and a target integer", color=WHITE)
        second = Text("return indices of two numbers such that they add up to target.", color=WHITE)
        second.next_to(first, DOWN)

        self.play(Write(first, run_time=1))
        self.play(Write(second, run_time=1))
        
class HighLevel(Scene):
    def construct(self):
        # 8 Show the problem introduction Text
        problem = Text("Problem Introduction", color=WHITE).scale(2)

        self.play(FadeIn(problem))
        self.play(FadeOut(problem))
        
        # 9 Show questions to ask
        first = TextMobject("Questions to ask:").scale(2)
        rec = VGroup(first)
        rec.move_to(UP*2 + LEFT*2)

        second = TextMobject("* Is the array sorted?").scale(1.25)
        third = TextMobject("* What does my input look like?").scale(1.25)
        four = TextMobject("* Will the sum cause integer overflow?").scale(1.25)
        five = TextMobject("* Is there guaranteed to be an answer?").scale(1.25)

        # https://www.reddit.com/r/manim/comments/iupbe8/how_to_left_align_textmobject/
        self.play(Write(rec, run_time=0.75))
        rec.add(second)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(second, run_time=0.75))
        rec.add(third)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(third, run_time=0.75))
        rec.add(four)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(four, run_time=0.75))
        rec.add(five)
        rec.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(five, run_time=0.75))

        # Fade out the rectangle holding all the text 
        self.play(FadeOut(rec))

        #10 N^2 array
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
        arrow_runtime=1
        for i in range(6):
            # Move both indexes together
            self.play(ApplyMethod(arrow1.next_to, arr[i]['group'], DOWN, run_time=arrow_runtime), ApplyMethod(arrow2.next_to, arr[i]['group'], DOWN, run_time=arrow_runtime))
            for j in range(i, 6):
                self.play(ApplyMethod(arrow2.next_to, arr[j]['group'], DOWN, run_time=arrow_runtime))
    
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
        self.play(FadeIn(array_object))

        # Setup variable text
        index_text = TextMobject("index:")
        low_text = TextMobject("lo:")
        mid_text = TextMobject("mid:")
        high_text = TextMobject("hi:")
        text_group = VGroup()
        text_group.add(index_text)
        text_group.add(low_text)
        text_group.add(high_text)
        text_group.add(mid_text)
        text_group.to_corner(corner=UP+LEFT)
        text_group.arrange(DOWN, center=False, aligned_edge=LEFT)

        # Setup variable value
        index_value = TextMobject("0")
        low_value = TextMobject("1")
        mid_value = TextMobject("4")
        high_value = TextMobject("7")
        value_group = VGroup()
        value_group.add(index_value)
        value_group.add(low_value)
        value_group.add(high_value)
        value_group.add(mid_value)
        value_group.arrange(DOWN, center=False, aligned_edge=LEFT)
        value_group.next_to(text_group, RIGHT*2)

        arrow = Arrow(DOWN, UP)
        arrow.scale(0.5)
        arrow.next_to(arr[0]['group'], DOWN)

        self.play(FadeIn(arrow), FadeIn(index_text), FadeIn(index_value)) 

        lo = TextMobject("lo")
        lo.next_to(arr[1]['group'], DOWN)
        mid = TextMobject("mid")
        mid.next_to(arr[4]['group'], DOWN)
        hi = TextMobject("hi")
        hi.next_to(arr[7]['group'], DOWN)

        # show lo,hi, and then show mid
        self.play(FadeIn(lo), FadeIn(hi), FadeIn(low_value), FadeIn(low_text), FadeIn(high_value), FadeIn(high_text))
        self.play(FadeIn(mid), FadeIn(mid_text), FadeIn(mid_value))

        # move lo to mid+1 (5) because mid + i is too small
        self.play(FadeOut(mid))

        new_low_value = self.replace_value_animation(low_value, "5")
        self.play(ApplyMethod(lo.next_to, arr[5]['group'], DOWN), FadeOut(low_value), FadeIn(new_low_value))
        low_value = new_low_value
        
        # show mid at index 6
        new_value = self.replace_value_animation(mid_value, "6")
        mid.next_to(arr[6]['group'], DOWN)
        self.play(FadeIn(mid), FadeOut(mid_value), FadeIn(new_value))
        mid_value = new_value

        # move hi to mid-1 (5) because mid + i is too big
        self.play(FadeOut(mid))  
        new_value = self.replace_value_animation(high_value, "5")
        self.play(ApplyMethod(hi.next_to, lo, DOWN), FadeOut(high_value), FadeIn(new_value))
        high_value = new_value

        # show mid at index 5
        new_value = self.replace_value_animation(mid_value, "5")
        mid.next_to(hi, DOWN)
        self.play(FadeIn(mid), FadeOut(mid_value), FadeIn(new_value))
        mid_value = new_value

    # given an old text value object, create a new text object with the new text value
    # plays an animation with the new value appearing and the old value fading, and then
    # returns an instance to the new text object
    def replace_value_animation(self, text_object, val):
        new_object = TextMobject(val)
        new_object.set_x(text_object.get_x()).set_y(text_object.get_y())
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

        left_value = self.moveArrowAndChangeText(l_value, "3", left, arr, 1) # l -> 3
        sum_value = self.changeSum(sum_value, "10")
        right_value = self.moveArrowAndChangeText(r_value, "6", right, arr, 3) # r -> 6
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

        self.play(FadeIn(code))

        arrow = Arrow(RIGHT, LEFT)
        arrow.scale(0.5)
        arrow.next_to(line1)
        self.play(FadeIn(arrow))
        const = 0.35
        self.play(ApplyMethod(arrow.shift, DOWN*const))
        self.play(ApplyMethod(arrow.shift, DOWN*const))
        self.play(ApplyMethod(arrow.shift, DOWN*const))
        self.play(ApplyMethod(arrow.shift, DOWN*const))
        self.play(ApplyMethod(arrow.shift, DOWN*const))
        self.play(ApplyMethod(arrow.shift, DOWN*const))
        self.play(ApplyMethod(arrow.shift, DOWN*const))
        self.play(ApplyMethod(arrow.shift, DOWN*const))
        self.play(ApplyMethod(arrow.shift, DOWN*const))
        self.play(ApplyMethod(arrow.shift, DOWN*const))


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

        nums_group.set_x(-3)
        nums_group.set_y(2)
        self.play(FadeIn(nums_group))

        lo_ptr = Arrow(DOWN, UP).scale(0.5).next_to(nums[0]['group'], DOWN)
        
        for lo in range(3):
            
            self.play(ApplyMethod(lo_ptr.next_to, nums[lo]['group'], DOWN))
            hi_ptr = Arrow(DOWN, UP, color=BLUE).scale(0.5).next_to(nums[lo]['group'], DOWN)

            for hi in range(lo + 1, 4):
                self.play(ApplyMethod(hi_ptr.next_to, nums[hi]['group'], DOWN))
                total = TextMobject(f"sum = {nums[lo]['num'] + nums[hi]['num']}")
                total.next_to(nums_group, UP)
                self.play(Write(total, run_time=.5))
                self.wait(.5)
                self.play(FadeOut(total))

            self.play(FadeOut(hi_ptr))
