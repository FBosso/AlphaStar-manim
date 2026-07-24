from manim import *
from manim_slides import Slide
import numpy as np

class AlphaStar(Slide):
    
    def construct(self):
        
        title = Tex(r"AlphaStar", font_size=50).to_edge(UP)
        self.play(FadeIn(title))
        
        self.next_slide()
        
        policy = MathTex("\pi(a_{t}|s_{t},","z",")")
        self.play(Write(policy))
        
        self.next_slide()
        
        observation = MathTex(r"o_{t}")
        o2p = MathTex(r"\rightarrow")
        p2a = MathTex(r"\rightarrow")
        action = MathTex(r"a_{t}")
        
        
        o2p.next_to(policy, LEFT)
        observation.next_to(o2p, LEFT)

        p2a.next_to(policy, RIGHT)
        action.next_to(p2a, RIGHT)
        
        self.play(FadeIn(observation),FadeIn(o2p),FadeIn(p2a),FadeIn(action))
        
        opa = VGroup(observation,o2p,policy,p2a,action)
        self.play(opa.animate.shift(2*UP))
        
        self.next_slide()
        
        self.play(Indicate(observation))
        observation_list = Tex(r"""
                                Baseline Features \\
                                Scalar Features \\
                                Entities \\
                                Minimap""", font_size=30).next_to(observation, 3*DOWN)
        self.play(FadeIn(observation_list))
        
        self.next_slide()
        
        self.play(Indicate(action))
        action_list = Tex(r"""
                                Action Type \\
                                Delay \\
                                Queued \\
                                Target Unit \\
                                Target Point""", font_size=30).next_to(action, 3*DOWN)
        self.play(FadeIn(action_list))
        
        self.next_slide()
        
        arrow = Arrow(
            start=observation_list.get_bottom(),
            end=observation_list.get_bottom() + DOWN
            )
        self.play(DrawBorderThenFill(arrow))
        
        train_and_inference = Tex(r"\textbf{Train}: Player and Opponent \\ \textbf{Inference}: Just Player", font_size=30).next_to(arrow, DOWN)
        
        self.play(FadeIn(train_and_inference))
        
        self.next_slide()
        
        # Don't FadeOut policy here — animate it shifting down instead
        self.play(FadeOut(observation),
                  FadeOut(o2p),
                  FadeOut(p2a),
                  FadeOut(action),
                  FadeOut(observation_list),
                  FadeOut(arrow),
                  FadeOut(train_and_inference),
                  FadeOut(action_list),
                  policy.animate.shift(2*DOWN))
        
        self.next_slide()
        
        self.play(Indicate(policy[1]))
        
        arrow = Arrow(
            start=policy[1].get_bottom(),
            end=policy[1].get_bottom() + DOWN
            )
        self.play(DrawBorderThenFill(arrow))
        
        z_stat_description = Tex(r"Randomly sampled player's statistic", font_size=30).next_to(arrow,DOWN)
        
        self.play(FadeIn(z_stat_description))
        
        self.next_slide()
        
        how_is = Tex(r"How is").next_to(policy, LEFT)
        trained = Tex(r"trained?").next_to(policy, RIGHT)
        
        self.play(FadeIn(how_is), FadeIn(trained), FadeOut(arrow), FadeOut(z_stat_description))