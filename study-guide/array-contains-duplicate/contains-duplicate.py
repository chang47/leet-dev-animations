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

        # self.play(FadeIn(array_object))
        # values = self.createText(array_object)



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

        #Brute force solution
        arr = []
        array_object = Group()
        arr_index = 0
        prices = [5, 3, 6, 1, 9] 
        for val in prices:
            value = TextMobject(str(val))
            square = Square().surround(value).set_width(1).set_height(1)
            group = Group(value, square).shift(RIGHT * arr_index)
            arr.append(group)
            array_object.add(group)
            arr_index+=1

        array_object.scale(0.75)
        array_object.center()
        array_object.shift(UP*2)

        arrow1 = Arrow(DOWN, UP)
        arrow1.scale(0.5)
        arrow2 = Arrow(DOWN, UP)
        arrow2.scale(0.5)

        self.play(FadeIn(array_object))
        values = self.createText(array_object)

        ans = 0
        min_num = prices[0]
        for i in range(1, len(prices), 1):
            arrow1.next_to(arr[i], DOWN)
            # move to the next index
            self.play(ApplyMethod(arrow1.next_to, arr[i], DOWN))
            profit = prices[i] - min_num
            
            values["current_value"] = self.changeText(values["current_text"], str(prices[i]) + ' - ' + str(min_num) + ' = ' + str(profit), values["current_value"])
            
            if profit > ans:
                ans = profit
                values["max_value"] = self.changeText(values["max_text"], str(ans), values["max_value"], True)
            elif prices[i] < min_num:
                min_num = prices[i]
                values["min_value"] = self.changeText(values["min_text"], str(prices[i]), values["min_value"], True)
    
    def createText(self, array_container):
        text_obj = {}

        max_text = Text("max profit:  ")
        max_value = Text("0")
        max_text.next_to(array_container, DOWN*5)
        max_text.shift(LEFT)
        max_value.next_to(max_text, RIGHT)
        self.play(FadeIn(max_text), FadeIn(max_value))
        text_obj["max_text"] = max_text
        text_obj["max_value"] = max_value
        
        current_text = Text("current profit:")
        current_value = Text("0")
        current_text.next_to(max_text, DOWN)
        current_value.next_to(current_text, RIGHT)
        self.play(FadeIn(current_text), FadeIn(current_value))
        text_obj["current_text"] = current_text
        text_obj["current_value"] = current_value

        min_text = Text("min:       ")
        min_value = Text("5")
        min_text.next_to(current_text, DOWN)
        min_value.next_to(min_text, RIGHT)
        self.play(FadeIn(min_text), FadeIn(min_value))
        text_obj["min_text"] = min_text
        text_obj["min_value"] = min_value
        return text_obj

    def changeText(self, text_object, new_value, value_object, grow=False):
        new_object = TextMobject(new_value)
        new_object.next_to(text_object, RIGHT)
        if grow:
            self.play(FadeOut(value_object), GrowFromCenter(new_object))
        else:
            self.play(FadeOut(value_object), FadeIn(new_object))
        return new_object

        