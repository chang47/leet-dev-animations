from manim import *

class BruteForce(Scene):
    def construct(self):
        title = TextMobject("O(N²): Brute Force")
        title.align_on_border(UP)
        self.play(FadeIn(title))

        arr = []
        array_object = Group()
        text_arr = []
        arr_index = 0
        prices = [1,2,3,2]
        for val in prices:
            value = Tex(str(val))
            text_arr.append(value)
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * arr_index)
            arr.append(group)
            array_object.add(group)
            arr_index+=1

        array_object.scale(0.75)
        array_object.center()

        i_g1 = Group()
        arrow1 = Arrow(DOWN, UP)
        arrow1.scale(0.5)
        text1 = Tex("i")
        text1.next_to(arrow1, DOWN)
        i_g1.add(arrow1)
        i_g1.add(text1)

        i_g2 = Group()
        arrow2 = Arrow(DOWN, UP)
        arrow2.scale(0.5)
        text2 = Tex("j")
        text2.next_to(arrow2, DOWN)
        i_g2.add(arrow2)
        i_g2.add(text2)

        self.play(FadeIn(array_object))
        values = self.createText(title)

        for i in range(len(prices)):
            i_g1.next_to(arr[i], DOWN)
            self.play(ApplyMethod(i_g1.next_to, arr[i], DOWN))
            self.transformText(values["i"], "i: " + str(i), title, 2)
            for j in range(i+1, len(prices)):
                i_g2.next_to(arr[j], DOWN)
                self.play(ApplyMethod(i_g2.next_to, arr[j], DOWN))
                self.transformText(values["j"], "j: " + str(j), values["i"])
                if prices[i] == prices[j]:
                    self.wait(1)
                    c1 = Circle()
                    c2 = Circle()
                    c1.surround(text_arr[i])
                    c2.surround(text_arr[j])
                    self.play(ShowCreation(c1), ShowCreation(c2))
                    self.wait(1)
                    # Animation ends here
                    return
            if i != len(prices)-1:
                self.play(FadeOut(i_g2))

    def createText(self, top):
        text_obj = {}
        text_obj["i"] = Tex("i: 0").scale(0.75).next_to(top, DOWN*2)
        text_obj["j"] = Tex("j: 0").scale(0.75).next_to(text_obj["i"], DOWN)
        self.play(FadeIn(text_obj["i"]))
        self.play(FadeIn(text_obj["j"]))

        return text_obj

    def transformText(self, text, value, location, multiple=1):
        text.target = Tex(value).scale(0.75).next_to(location, DOWN*multiple)
        self.play(MoveToTarget(text))

class Sorting(Scene):
    def construct(self):
        title = TextMobject("O(N Log N) Sorting")
        title.align_on_border(UP)
        self.play(FadeIn(title))
        
        #Brute force solution
        array_object = Group()
        arr_index = 0
        prices = [1,2,3,2]
        for val in prices:
            value = Tex(str(val))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * arr_index)
            array_object.add(group)
            arr_index+=1

        array_object.scale(0.75)
        array_object.center()

        self.play(FadeIn(array_object))

        arr = []
        array_object2 = Group()
        arr_index = 0
        text_arr = []
        prices2 = [1, 2, 2, 3]
        for val in prices2:
            value = Tex(str(val))
            text_arr.append(value)
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * arr_index)
            arr.append(group)
            array_object2.add(group)
            arr_index+=1
            
        array_object2.scale(0.75)
        array_object2.center()

        self.play(Transform(array_object, array_object2))

        i_g1 = Group()
        arrow1 = Arrow(DOWN, UP)
        arrow1.scale(0.5)
        text1 = Tex("i")
        text1.next_to(arrow1, DOWN)
        i_g1.add(arrow1)
        i_g1.add(text1)

        i_g2 = Group()
        arrow2 = Arrow(DOWN, UP)
        arrow2.scale(0.5)
        text2 = Tex("i-1")
        text2.next_to(arrow2, DOWN)
        i_g2.add(arrow2)
        i_g2.add(text2)

        prices.sort()

        for i in range(1, len(prices)):
            j = i-1
            i_g1.next_to(arr[i], DOWN)
            self.play(ApplyMethod(i_g1.next_to, arr[i], DOWN))

            i_g2.next_to(arr[j], DOWN)
            self.play(ApplyMethod(i_g2.next_to, arr[j], DOWN))
            if prices[i] == prices[j]:
                self.wait(1)
                c1 = Circle()
                c2 = Circle()
                c1.surround(text_arr[i])
                c2.surround(text_arr[j])
                self.play(ShowCreation(c1), ShowCreation(c2))
                self.wait(1)
                # Animation ends here
                return
            if i != len(prices)-1:
                self.play(FadeOut(i_g2))
    
    def createText(self, top):
        text_obj = {}
        text_obj["i"] = Tex("i: 0").scale(0.75).next_to(top, DOWN*2)
        text_obj["j"] = Tex("j: 0").scale(0.75).next_to(text_obj["i"], DOWN)
        self.play(FadeIn(text_obj["i"]))
        self.play(FadeIn(text_obj["j"]))

        return text_obj

    def transformText(self, text, value, location, multiple=1):
        text.target = Tex(value).scale(0.75).next_to(location, DOWN*multiple)
        self.play(MoveToTarget(text))

class Optimal(Scene):
    def construct(self):
        title = TextMobject("O(N): Set")
        title.align_on_border(UP)
        self.play(FadeIn(title))

        arr = []
        array_object = Group()
        arr_index = 0
        text_arr = []
        prices = [1, 2, 3, 2]
        for val in prices:
            value = Tex(str(val))
            text_arr.append(value)
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * arr_index)
            arr.append(group)
            array_object.add(group)
            arr_index+=1
            
        array_object.scale(0.75)
        array_object.center()

        texts = self.createText(title)
        self.play(FadeIn(array_object))

        i_g1 = Group()
        arrow1 = Arrow(DOWN, UP)
        arrow1.scale(0.5)
        i_g1.add(arrow1)
        s = set()
        for i in range(0, len(prices)):
            i_g1.next_to(arr[i], DOWN)
            self.play(ApplyMethod(i_g1.next_to, arr[i], DOWN))
            self.transformText(texts["i"], "i: " + str(i), title, 2)
            if prices[i] in s:
                self.wait(1)
                c1 = Circle()
                c1.surround(text_arr[i])
                c2 = Circle().scale(0.2).shift(UP*1.825 + RIGHT * 0.375)

                self.play(ShowCreation(c1), ShowCreation(c2))
                self.wait(1)
                return
            s.add(prices[i])
            self.transformText(texts["set"], "set: \{" + str(s) +"\}", texts["i"])
            self.wait(1)

    def createText(self, top):
        text_obj = {}
        text_obj["i"] = Tex("i: 0").scale(0.75).next_to(top, DOWN*2)
        text_obj["set"] = Tex("set: \{\}").scale(0.75).next_to(text_obj["i"], DOWN)
        self.play(FadeIn(text_obj["i"]))
        self.play(FadeIn(text_obj["set"]))

        return text_obj

    def transformText(self, text, value, location, multiple=1):
        text.target = Tex(value).scale(0.75).next_to(location, DOWN*multiple)
        self.play(MoveToTarget(text))

class AlgorithmExplaination(Scene):
    def construct(self):
        first = TextMobject("Algorithm and Data Structures used:").scale(1.25)
        rec = VGroup(first)
        rec.move_to(UP + LEFT)

        third = TextMobject("O(N²): Brute force every combination").scale(0.9)
        four = TextMobject("O(N Log N): Sort the array and then scan through it").scale(0.9)
        five = TextMobject("O(N): Use a Set to keep track of previously seen numbers").scale(0.9)

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