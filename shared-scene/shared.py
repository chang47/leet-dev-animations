from manim import *

class ShowLogo(Scene):
    def construct(self):
        img = ImageMobject('../images/logo2.png').scale(1)
        # img.center()

        self.play(GrowFromCenter(img))  # Display the image

class LikeAndSubscribe(Scene):
    def construct(self):
        like = ImageMobject('../images/like.png')
        subscribe = ImageMobject('../images/subscribe.png').scale(0.75)
        plus = ImageMobject('../images/plus.png').scale(0.75)
        
        like.next_to(like, LEFT)
        subscribe.next_to(plus, RIGHT*4)

        self.play(FadeIn(like))
        self.play(FadeIn(plus))
        self.play(FadeIn(subscribe))

