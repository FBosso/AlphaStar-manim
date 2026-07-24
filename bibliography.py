from manim import *
from manim_slides import Slide

class Bibliography(Slide):
    
    def construct(self):
        
        title = Tex(r"Bibliography", font_size=50).to_edge(UP)
        self.play(FadeIn(title))

        # ── Bibliography entries ───────────────────────────────────────────────
        entry1 = Tex(
            r"Sutton, R. S., and Barto, A. G. \textit{Reinforcement Learning: An Introduction}. 2nd ed., MIT Press, 2018.",
            font_size=30
        )

        entry2 = Tex(
            r"Degris, T., White, M., and Sutton, R. S. ``Off-policy actor-critic.'' \textit{arXiv preprint arXiv:1205.4839} (2012).",
            font_size=30
        )

        entry3 = Tex(
            r"Schmitt, S., Hessel, M., and Simonyan, K. ``Off-policy actor-critic with shared experience replay.'' \textit{ICML}. PMLR, 2020.",
            font_size=30
        )

        entry4 = Tex(
            r"Vinyals, O., Babuschkin, I., Czarnecki, W.M. et al. ``Grandmaster level in StarCraft II using multi-agent reinforcement learning.'' \textit{Nature} 575, 350--354 (2019).",
            font_size=30
        )

        entry5 = Tex(
            r"Espeholt, L., et al. ``IMPALA: Scalable distributed deep-RL with importance weighted actor-learner architectures.'' \textit{ICML}. PMLR, 2018.",
            font_size=30
        )

        # ── Stack and left-align all entries ──────────────────────────────────
        bib = VGroup(entry1, entry2, entry3, entry4, entry5)
        bib.arrange(DOWN, buff=0.35)
        bib.next_to(title, DOWN, buff=0.5)
        

        self.play(FadeIn(bib))
        self.next_slide()