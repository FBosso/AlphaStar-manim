from manim import *
from manim_slides import Slide

class Starcraft(Slide):
    
    def construct(self):
    
        title = Tex(r"StarCraft", font_size=50).to_edge(UP)
        
        self.play(FadeIn(title))
        
        self.next_slide() 
        
        bullets = Tex(r"""
                      \begin{itemize}
                        \item Real-Time Strategy (RTS) game
                        \item Combinatorial action space
                        \item Thousands of real-time decisions
                        \item Imperfect information
                      \end{itemize}
                      """, font_size=30).shift(3*LEFT)
        
        starcraft_img = ImageMobject("assets/starcraft.jpeg").shift(3*RIGHT)
        starcraft_img.scale(0.5)
        
        self.play(FadeIn(bullets), FadeIn(starcraft_img))