from manim import *
from manim_slides import Slide

class Title(Slide):
    def construct(self):

        icon = ImageMobject("assets/leo-logo.png").scale(0.15).shift(2.3 * UP)

        title = Tex(r"Reinforcement Learning for Real-time strategy games", font_size=50)
        
        subtitle = Tex(r"AlphaStar", font_size=50)
        subtitle.shift(DOWN)
        
        authors = Tex(r"Bosso Francesco", font_size=30)
        authors.shift(2* DOWN)
        
        affilitions = Tex(r"Reinforcement Learning Community - CoE, Leonardo S.p.A.", font_size=25)
        affilitions.shift(3* DOWN)
        
        self.next_slide() 

        self.play(FadeIn(icon), FadeIn(title), FadeIn(subtitle), FadeIn(authors), FadeIn(affilitions))


        self.next_slide() 