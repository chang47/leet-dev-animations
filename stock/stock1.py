from manim import *

class BruteForce(Scene):
    def construct(self):
        #Brute force solution
        arr = []
        array_object = Group()
        arr_index = 0
        prices = [7,1,5,3,6,4] 
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
        for i in range(len(prices)):
            arrow1.next_to(arr[i], DOWN)
            if i == 0:
                # show the arrow if the first time
                self.play(FadeIn(arrow1))
            else:
                self.play(ApplyMethod(arrow1.next_to, arr[i], DOWN))
            for j in range(i+1, len(prices), 1):
                profit = prices[j] - prices[i]
                arrow2.next_to(arr[j], DOWN)
                if i + 1 == j:
                    # if the first index, the arrow is missing so we need to show it
                    arrow2.next_to(arr[j], DOWN)
                    self.play(FadeIn(arrow2))
                else:
                    self.play(ApplyMethod(arrow2.next_to, arr[j], DOWN))
                values["current_value"] = self.changeText(values["current_text"], str(prices[j]) + ' - ' + str(prices[i]) + ' = ' + str(profit), values["current_value"])
                
                if profit > ans:
                    ans = profit
                    values["max_value"] = self.changeText(values["max_text"], str(ans), values["max_value"])
            self.play(FadeOut(arrow2))
    
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
        return text_obj

    def changeText(self, text_object, new_value, value_object):
        new_object = TextMobject(new_value)
        new_object.next_to(text_object, RIGHT)
        self.play(FadeOut(value_object), FadeIn(new_object))
        return new_object

        