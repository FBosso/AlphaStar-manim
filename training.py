from manim import *
from manim_slides import Slide
import numpy as np

class Training(Slide):

    def construct(self):

        #title setup
        title = Tex(r"AlphaStar", font_size=50).to_edge(UP)
        self.play(FadeIn(title))

        self.next_slide()

        #main sections: Supervised and Reinforcement Learning
        supervised_learning_title = Tex(r"Supervised Learning", font_size=40).shift(UP)
        reinforcement_learning_title = Tex(r"Reinforcement Learning", font_size=40).shift(DOWN)

        self.play(FadeIn(supervised_learning_title), FadeIn(reinforcement_learning_title))

        ###supervised learning section
        self.next_slide()

        self.play(FadeOut(reinforcement_learning_title), supervised_learning_title.animate.next_to(title, DOWN))

        #supervised learning bullet points
        supervised_item_1 = Tex(r"$\bullet$ Games are sampled from human replays", font_size=30)
        supervised_item_2 = Tex(r"$\bullet$ Policy trained to predict action $a_t$ given", font_size=30)
        supervised_item_3 = Tex(r"$\bullet$ state $s_t$", font_size=28)
        supervised_item_4 = Tex(r"$\bullet$ statistic $z$", font_size=28)

        supervised_subitems = VGroup(supervised_item_3, supervised_item_4).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        supervised_items_group = VGroup(supervised_item_1, supervised_item_2, supervised_subitems).arrange(DOWN, aligned_edge=LEFT)
        supervised_subitems.shift(RIGHT)

        self.next_slide()
        self.play(FadeIn(supervised_item_1))
        self.next_slide()

        self.play(FadeIn(supervised_item_2))
        self.next_slide()

        self.play(FadeIn(supervised_item_3))
        self.next_slide()

        self.play(FadeIn(supervised_item_4))
        self.next_slide()

        self.play(FadeOut(supervised_items_group))
        self.play(FadeIn(reinforcement_learning_title), supervised_learning_title.animate.move_to(ORIGIN + UP))
        ###reinforcement learning section
        self.next_slide()

        self.play(FadeOut(supervised_learning_title), reinforcement_learning_title.animate.next_to(title, DOWN))

        self.next_slide()

        #reinforcement learning bullet points
        rl_item_1 = Tex(r"$\bullet$ Weights obtained from \textbf{Supervised Learning} used to \textbf{initialize RL agent}", font_size=30)
        rl_item_2 = Tex(r"$\bullet$ RL algorithm is designed to", font_size=30)
        rl_item_3 = Tex(r"$\bullet$ Maximize the win rate", font_size=28)
        rl_item_4 = Tex(r"$\bullet$ Play against a mixture of opponents", font_size=28)

        rl_subitems = VGroup(rl_item_3, rl_item_4).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        rl_items_group = VGroup(rl_item_1, rl_item_2, rl_subitems).arrange(DOWN, aligned_edge=LEFT)
        rl_subitems.shift(RIGHT)

        self.next_slide()
        self.play(FadeIn(rl_item_1))
        self.next_slide()

        self.play(FadeIn(rl_item_2))
        self.next_slide()

        self.play(FadeIn(rl_item_3))
        self.next_slide()

        self.play(FadeIn(rl_item_4))
        self.next_slide()

        #questions about maximizing win rate and opponent selection
        win_rate_arrow = Arrow(
            start=rl_item_3.get_right(),
            end=rl_item_3.get_right() + RIGHT
        )
        opponent_mixture_arrow = Arrow(
            start=rl_item_4.get_right(),
            end=rl_item_4.get_right() + RIGHT
        )

        win_rate_question = Tex(r"How is it maximizing the win rate?", font_size=24).next_to(win_rate_arrow, RIGHT)
        opponent_question = Tex(r"How are opponents selected during training?", font_size=24).next_to(opponent_mixture_arrow, RIGHT)
        
        self.play(DrawBorderThenFill(win_rate_arrow), DrawBorderThenFill(opponent_mixture_arrow), Write(win_rate_question), Write(opponent_question))

        self.next_slide()

        self.play(Indicate(win_rate_question))

        self.next_slide()

        self.play(FadeOut(rl_items_group), FadeOut(win_rate_arrow), FadeOut(opponent_mixture_arrow), FadeOut(opponent_question), win_rate_question.animate.next_to(reinforcement_learning_title, DOWN))

        self.next_slide()

        #actor-critic algorithm explanation
        actor_critic_title = Tex(r"$\bullet$ The learning algorithm used by AlphaStar is \textbf{Actor-Critic}", font_size=30)

        techniques_intro = Tex(r"$\bullet$ It brings together 3 different techniques", font_size=30)
        td_lambda_item = Tex(r"$\bullet$ TD($\lambda$)", font_size=28, substrings_to_isolate=[r"TD($\lambda$)"])
        v_trace_item = Tex(r"$\bullet$ V-trace", font_size=28, substrings_to_isolate=[r"V-trace"])
        upgo_item = Tex(r"$\bullet$ Upgoing Policy Update, UPGO", font_size=28, substrings_to_isolate=[r"UPGO"])

        rewards_intro = Tex(r"$\bullet$ Two different types of reward", font_size=30)
        terminal_reward = Tex(r"$\bullet$ \textbf{Terminal Reward}: match outcome (-1 Loss, 0 Draw, 1 Win)", font_size=28)
        pseudo_reward = Tex(r"$\bullet$ \textbf{Pseudo-reward}: Edit/Hamming distance w.r.t $z$ statistic", font_size=28)

        techniques_subitems = VGroup(td_lambda_item, v_trace_item, upgo_item).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        rewards_subitems = VGroup(terminal_reward, pseudo_reward).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        actor_critic_items = VGroup(actor_critic_title, techniques_intro, techniques_subitems, rewards_intro, rewards_subitems).arrange(DOWN, aligned_edge=LEFT).shift(0.5 * DOWN)
        techniques_subitems.shift(RIGHT)
        rewards_subitems.shift(RIGHT)

        self.next_slide()
        self.play(FadeIn(actor_critic_title))
        self.next_slide()

        #actor-critic diagram
        state_node = Tex(r"$s$")
        policy_node = Tex(r"$\pi_{\theta}$")
        value_node = Tex(r"$V_{w}(s')$")
        td_error_node = Tex(r"TD Error", font_size=30)

        #arrange them in a row with spacing
        actor_critic_nodes = VGroup(state_node, policy_node, value_node, td_error_node)
        actor_critic_nodes.arrange(RIGHT, buff=1.5)

        #create arrows between each pair
        state_to_policy_arrow = Arrow(start=state_node.get_right(), end=policy_node.get_left(), buff=0.1)
        policy_to_value_arrow = Arrow(start=policy_node.get_right(), end=value_node.get_left(), buff=0.1)
        value_to_td_arrow = Arrow(start=value_node.get_right(), end=td_error_node.get_left(), buff=0.1)

        #labels on top of arrows
        transition_label = Tex(r"transition", font_size=35).scale(0.6).next_to(policy_to_value_arrow, UP, buff=0.15)
        value_label = Tex(r"value of \\ new state", font_size=35).scale(0.6).next_to(value_to_td_arrow, UP, buff=0.15)

        #labels on top of nodes
        actor_label = Tex(r"actor").scale(0.6).set_color(YELLOW).next_to(policy_node, DOWN, buff=0.3)
        critic_label = Tex(r"critic").scale(0.6).set_color(YELLOW).next_to(value_node, DOWN, buff=0.3)

        #curved feedback arrows from TD Error back to V_w and pi_theta
        update_value_arrow = CurvedArrow(
            start_point=td_error_node.get_bottom() + DOWN * 0.1,
            end_point=value_node.get_bottom() + DOWN * 0.1,
            angle=-PI / 3,
        ).set_color(RED)

        update_policy_arrow = CurvedArrow(
            start_point=td_error_node.get_bottom() + DOWN * 0.1,
            end_point=policy_node.get_bottom() + DOWN * 0.1,
            angle=-PI / 4,
        ).set_color(RED)

        #update labels below the curved arrows
        update_label = Tex(r"update").scale(0.55).set_color(RED)
        update_label.next_to(update_value_arrow, 2 * DOWN, buff=0.1)

        actor_critic_diagram = VGroup(
            state_node, state_to_policy_arrow, policy_node, transition_label, actor_label,
            policy_to_value_arrow, value_node, value_label, critic_label, value_to_td_arrow,
            td_error_node, update_value_arrow, update_policy_arrow, update_label
        )

        #animate the diagram
        self.play(FadeIn(state_node))
        self.next_slide()
        self.play(DrawBorderThenFill(state_to_policy_arrow), FadeIn(policy_node))
        self.next_slide()
        self.play(FadeIn(actor_label))
        self.next_slide()
        self.play(DrawBorderThenFill(policy_to_value_arrow), FadeIn(value_node), FadeIn(transition_label))
        self.next_slide()
        self.play(FadeIn(critic_label))
        self.next_slide()
        self.play(DrawBorderThenFill(value_to_td_arrow), FadeIn(td_error_node), FadeIn(value_label))
        self.next_slide()
        self.play(
            DrawBorderThenFill(update_value_arrow), DrawBorderThenFill(update_policy_arrow), FadeIn(update_label)
        )
        self.next_slide()

        self.play(FadeOut(actor_critic_diagram))

        self.play(FadeIn(techniques_intro))
        self.next_slide()

        self.play(FadeIn(td_lambda_item, v_trace_item, upgo_item))
        self.next_slide()

        self.play(FadeIn(rewards_intro))
        self.next_slide()

        self.play(FadeIn(terminal_reward, pseudo_reward))
        self.next_slide()

        #extract the term parts for highlighting
        td_lambda_part = td_lambda_item.get_part_by_tex("TD($\\lambda$)")
        v_trace_part = v_trace_item.get_part_by_tex("V-trace")
        upgo_part = upgo_item.get_part_by_tex("UPGO")

        #remove terms from their parents so FadeOut on parents won't affect them
        td_lambda_item.remove(td_lambda_part)
        v_trace_item.remove(v_trace_part)
        upgo_item.remove(upgo_part)

        #add them directly to the scene
        self.add(td_lambda_part, v_trace_part, upgo_part)

        #now fade out everything else (terms are no longer children of these)
        other_items = VGroup(actor_critic_title, techniques_intro, td_lambda_item, v_trace_item, upgo_item, rewards_intro, terminal_reward, pseudo_reward)
        #move the three terms to the left
        technique_terms = VGroup(td_lambda_part.copy(), v_trace_part.copy(), upgo_part.copy())
        technique_terms.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        technique_terms.to_edge(LEFT, buff=1.0)

        self.play(
            ReplacementTransform(td_lambda_part, technique_terms[0]),
            ReplacementTransform(v_trace_part, technique_terms[1]),
            ReplacementTransform(upgo_part, technique_terms[2]),
        )
        self.play(FadeOut(other_items))

        self.next_slide()

        #td(lambda) section
        self.play(technique_terms[1].animate.set_color("#363636"), technique_terms[2].animate.set_color("#363636"))

        monte_carlo_image = ImageMobject("assets/monte_carlo.png").shift(2 * LEFT + DOWN)
        monte_carlo_image.scale(0.35)

        td_zero_image = ImageMobject("assets/TD(0).png").shift(3 * RIGHT + DOWN)
        td_zero_image.scale(0.35)

        monte_carlo_label = Tex(r"Monte Carlo").next_to(monte_carlo_image, UP)
        td_zero_label = Tex(r"TD(0)").next_to(td_zero_image, UP)

        self.play(FadeIn(monte_carlo_image), FadeIn(td_zero_image), FadeIn(monte_carlo_label), FadeIn(td_zero_label))
        self.next_slide()
        self.play(FadeOut(monte_carlo_image), FadeOut(td_zero_image), FadeOut(monte_carlo_label), FadeOut(td_zero_label))

        n_steps_image = ImageMobject("assets/n_steps.png").shift(DOWN)
        n_steps_image.scale(0.5)

        bias_label = Tex(r"Bias", font_size=30).shift(2 * DOWN + 2 * LEFT)
        left_arrow = Arrow(start=RIGHT, end=LEFT).next_to(bias_label, DOWN)

        variance_label = Tex(r"Variance", font_size=30).shift(2 * DOWN + 2 * LEFT)
        right_arrow = Arrow(start=LEFT, end=RIGHT).next_to(variance_label, DOWN)

        self.play(FadeIn(n_steps_image))
        self.play(FadeIn(bias_label), DrawBorderThenFill(left_arrow))
        self.next_slide()
        self.play(FadeOut(bias_label), FadeOut(left_arrow))
        self.play(FadeIn(variance_label), DrawBorderThenFill(right_arrow))

        self.next_slide()
        self.play(FadeOut(variance_label), FadeOut(right_arrow), FadeOut(n_steps_image))

        #v-trace section
        self.play(technique_terms[0].animate.set_color("#363636"), technique_terms[2].animate.set_color("#363636"), technique_terms[1].animate.set_color(WHITE))
        v_trace_question = Tex(r"Why is it used?", font_size=30).next_to(win_rate_question, 2 * DOWN)
        on_policy_actor_critic = Tex(r"$\bullet$ Naive Actor-Critic implementations are on-policy", font_size=30)
        importance_sampling_intro = Tex(r"$\bullet$ We make Naive Actor-Critic off-policy with Importance Sampling", font_size=30, substrings_to_isolate=[r"Importance Sampling"])
        importance_sampling_part = importance_sampling_intro.get_part_by_tex("Importance Sampling")
        importance_sampling_explanation = Tex(r"Estimate the expectation of a \textbf{different} \\ \textbf{distribution} with respect to the distribution \\ used to \textbf{draw samples}", font_size=30).next_to(importance_sampling_part, 5 * DOWN)
        importance_sampling_arrow = Arrow(
            start=importance_sampling_part.get_bottom() + 0.2 * DOWN,
            end=importance_sampling_explanation.get_top())

        importance_sampling_items = VGroup(on_policy_actor_critic, importance_sampling_intro).arrange(DOWN, aligned_edge=LEFT)

        self.play(FadeIn(v_trace_question))
        self.next_slide()

        self.play(FadeIn(on_policy_actor_critic))
        self.next_slide()
        
        
        ####################
        #create all text objects
        state = Tex(r"$s$", font_size=35)
        pi_1 = Tex(r"$\pi_{1}(a|s)$", font_size=35)
        v_p1 = Tex(r"$V_{\pi_{1}}(s')$", font_size=35)
        td_error = Tex(r"$r+\gamma V_{\pi_{1}}(s^{\prime})-V_{\pi_{1}}(s)$", font_size=30)

        #arrange main row first
        all_labels = VGroup(state, pi_1, v_p1, td_error)
        all_labels.arrange(RIGHT, buff=1.2)

        #now position pi_2 and v_p2 relative to already-placed pi_1 and v_p1
        pi_2 = Tex(r"$\pi_{2}(a|s)$", font_size=35).next_to(pi_1, DOWN, buff=0.6)
        v_p2 = Tex(r"$V_{\pi_{2}}(s')$", font_size=35).next_to(v_p1, DOWN, buff=0.6)

        #create arrows after positions are set, no .scale()
        sp = Arrow(start=state.get_right(), end=pi_1.get_left(), buff=0.1, tip_length=0.2)
        pv = Arrow(start=pi_1.get_right(), end=v_p1.get_left(), buff=0.1, tip_length=0.2)
        vt = Arrow(start=v_p1.get_right(), end=td_error.get_left(), buff=0.1, tip_length=0.2)

        down_arrow_pi1 = Arrow(start=pi_1.get_bottom(), end=pi_2.get_top(), buff=0.1, tip_length=0.2)
        down_arrow_v_p1 = Arrow(start=v_p1.get_bottom(), end=v_p2.get_top(), buff=0.1, tip_length=0.2)

        #labels on top of arrows
        transition_label = Tex(r"transition", font_size=22).next_to(pv, UP, buff=0.1)
        value_label = Tex(r"value of \\ new state", font_size=22).next_to(vt, UP, buff=0.1)

        #labels on top of nodes
        actor_label = Tex(r"actor", font_size=22).set_color(YELLOW).next_to(pi_1, UP, buff=0.2)
        critic_label = Tex(r"critic", font_size=22).set_color(YELLOW).next_to(v_p1, UP, buff=0.2)

        #curved feedback arrows from TD Error back
        update_v = CurvedArrow(
            start_point=td_error.get_top() + UP * 0.1,
            end_point=v_p1.get_top() + UP * 0.1,
            angle=PI / 3,
        ).set_color(RED)

        update_pi = CurvedArrow(
            start_point=td_error.get_top() + UP * 0.1,
            end_point=pi_1.get_top() + UP * 0.1,
            angle=PI / 4,
        ).set_color(RED)

        #shift everything together
        everything = VGroup(
            state, pi_1, v_p1, td_error, pi_2, v_p2,
            sp, pv, vt, down_arrow_pi1, down_arrow_v_p1,
            transition_label, value_label, actor_label, critic_label,
            update_v, update_pi
            
        ).shift(1.3*DOWN)

        #animate
        self.play(FadeIn(state))
        self.next_slide()
        self.play(DrawBorderThenFill(sp), FadeIn(pi_1))
        self.next_slide()
        self.play(FadeIn(actor_label))
        self.next_slide()
        self.play(DrawBorderThenFill(pv), FadeIn(v_p1), FadeIn(transition_label))
        self.next_slide()
        self.play(FadeIn(critic_label))
        self.next_slide()
        self.play(DrawBorderThenFill(vt), Write(td_error), FadeIn(value_label))
        self.next_slide()
        self.play(DrawBorderThenFill(update_v), DrawBorderThenFill(update_pi))
        self.next_slide()
        self.play(DrawBorderThenFill(down_arrow_pi1), DrawBorderThenFill(down_arrow_v_p1), FadeIn(pi_2), FadeIn(v_p2))
        self.next_slide()
        
        self.play(FadeOut(everything))
        
        ###################        
        
        
        
        self.play(FadeIn(importance_sampling_intro))
        self.next_slide()

        self.play(Indicate(importance_sampling_part), DrawBorderThenFill(importance_sampling_arrow), FadeIn(importance_sampling_explanation))
        self.next_slide()

        self.play(FadeOut(importance_sampling_arrow), FadeOut(importance_sampling_explanation), FadeOut(importance_sampling_items), FadeOut(v_trace_question))

        #importance sampling proof section
        importance_sampling_line1 = MathTex(
            r"\mathbb{E}_{a \sim \pi_1(\cdot|s)}[f(a)]",
            r"= \sum_a \pi_1(a|s)\, f(a)",
            font_size=35
        )

        importance_sampling_line2 = MathTex(
            r"= \sum_a \pi_2(a|s)\, \frac{\pi_1(a|s)}{\pi_2(a|s)}\, f(a)",
            font_size=35
        )

        importance_sampling_line3 = MathTex(
            r"= \mathbb{E}_{a \sim \pi_2(\cdot|s)}\!\left[",
            r"\frac{\pi_1(a|s)}{\pi_2(a|s)}",
            r"\, f(a)\right]",
            font_size=35
        )

        #align lines
        importance_sampling_line2.next_to(importance_sampling_line1, DOWN, buff=0.4)
        importance_sampling_line3.next_to(importance_sampling_line2, DOWN, buff=0.4)
        importance_sampling_line2.align_to(importance_sampling_line1[1], LEFT)
        importance_sampling_line3.align_to(importance_sampling_line1[1], LEFT)

        importance_sampling_proof = VGroup(importance_sampling_line1, importance_sampling_line2, importance_sampling_line3).move_to(ORIGIN)

        #reveal proof line by line
        self.play(Write(importance_sampling_line1))
        self.next_slide()
        self.play(Write(importance_sampling_line2))
        self.next_slide()
        self.play(Write(importance_sampling_line3))
        self.next_slide()

        #transition: move proof up to make room
        ratio_copy = importance_sampling_line3[1].copy()
        self.add(ratio_copy)
        self.play(FadeOut(importance_sampling_line3[0]), FadeOut(importance_sampling_line3[1]), FadeOut(importance_sampling_line3[2]),
                FadeOut(importance_sampling_line1), FadeOut(importance_sampling_line2))
        self.next_slide()

        #initial equation
        static_left = MathTex(
            r"V^{\pi}(s_t) = \mathbb{E}_{\pi} \left[ V(s_t) + \sum_{k=0}^{K-1} \gamma^k \,",
            font_size=35
        )
        static_right = MathTex(
            r"\delta_{t+k} \right]",
            font_size=35
        )
        static_left.move_to(ORIGIN)
        static_right.next_to(static_left, RIGHT, buff=0.15)

        self.play(Write(static_left))
        self.play(Write(static_right))
        self.next_slide()

        #step 2: ratio flies in from line3, static parts don't move
        ratio_simple = MathTex(
            r"\frac{\pi_1(a|s)}{\pi_2(a|s)}",
            font_size=35
        )
        ratio_simple.next_to(static_left, RIGHT, buff=0.15)

        self.play(
            static_right.animate.next_to(ratio_simple, RIGHT, buff=0.15),
            ratio_copy.animate.move_to(ratio_simple.get_center()),
        )
        self.play(FadeIn(ratio_simple), FadeOut(ratio_copy))
        self.remove(ratio_copy)
        self.next_slide()

        #step 3: only the ratio morphs into product — static parts frozen
        prod_left = MathTex(r"\left( \prod_{i=0}^{k}", font_size=35)
        ratio_indexed = MathTex(
            r"\frac{\pi_1(a_{t+i}|s_{t+i})}{\pi_2(a_{t+i}|s_{t+i})}",
            font_size=35
        )
        prod_right = MathTex(r"\right)", font_size=35)

        product_group = VGroup(prod_left, ratio_indexed, prod_right)
        product_group.arrange(RIGHT, buff=0.1)
        product_group.move_to(ratio_simple.get_center())

        self.play(
            ReplacementTransform(ratio_simple, ratio_indexed),
            static_right.animate.next_to(product_group, RIGHT, buff=0.15),
            static_left.animate.next_to(product_group, LEFT, buff=0.15),
            FadeIn(prod_left),
            FadeIn(prod_right)
        )

        value_function = VGroup(static_right, static_left, product_group)
        where_label = Tex(r"where", font_size=30).next_to(value_function, DOWN)
        delta_definition = MathTex(r"\delta_t^V = r_t + \gamma V(s_{t+1}) - V(s_t)", font_size=35).next_to(where_label, DOWN)

        self.next_slide()

        #highlight product term only
        product_term = VGroup(prod_left, ratio_indexed, prod_right)
        self.play(product_term.animate.set_color(YELLOW), FadeIn(where_label), FadeIn(delta_definition))
        self.next_slide()

        self.play(FadeOut(where_label), FadeOut(delta_definition), FadeOut(value_function))
        
        
        line_1 = MathTex(r"V^{\pi_2}(s_t) = \mathbb{E}_{\pi_1}\Big[\; V(s_t)", font_size=30)

        line_2 = MathTex(
            r"+ ",
            r"\frac{\pi_2(a_t \mid s_t)}{\pi_1(a_t \mid s_t)}",
            r"\, \delta_t^V",
            font_size=30
        )

        line_3 = MathTex(
            r"+ \gamma",
            r"\frac{\pi_2(a_t \mid s_t)}{\pi_1(a_t \mid s_t)}",
            r"\frac{\pi_2(a_{t+1} \mid s_{t+1})}{\pi_1(a_{t+1} \mid s_{t+1})}",
            r"\, \delta_{t+1}^V",
            font_size=30
        )

        line_4 = MathTex(
            r"+ \gamma^2",
            r"\frac{\pi_2(a_t \mid s_t)}{\pi_1(a_t \mid s_t)}",
            r"\frac{\pi_2(a_{t+1} \mid s_{t+1})}{\pi_1(a_{t+1} \mid s_{t+1})}",
            r"\frac{\pi_2(a_{t+2} \mid s_{t+2})}{\pi_1(a_{t+2} \mid s_{t+2})}",
            r"\, \delta_{t+2}^V",
            font_size=30
        )

        line_5 = MathTex(r"+ \dots \Big]", font_size=30)

        #stack lines and left-align them
        unrolled_is = VGroup(line_1, line_2, line_3, line_4, line_5)
        unrolled_is.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        unrolled_is.move_to(ORIGIN)
        unrolled_is.shift(DOWN)
        line_2.shift(RIGHT)
        line_3.shift(RIGHT)
        line_4.shift(RIGHT)
        line_5.next_to(line_4,RIGHT)

        #named ratio references
        ratio_t_line2  = line_2[1]
        ratio_t_line3  = line_3[1]
        ratio_t1_line3 = line_3[2]
        ratio_t_line4  = line_4[1]
        ratio_t1_line4 = line_4[2]
        ratio_t2_line4 = line_4[3]

        self.play(FadeIn(unrolled_is))
        self.next_slide()
        
        high_variance = Tex(r"\textbf{High Variance}").set_color(RED).next_to(line_4,DOWN)

        # ── Example: highlight all t-step ratios in yellow ───────────────────────────
        self.play(
            ratio_t_line2.animate.set_color(RED),
            ratio_t_line3.animate.set_color(RED),
            ratio_t1_line3.animate.set_color(RED),
            ratio_t1_line4.animate.set_color(RED),
            ratio_t_line4.animate.set_color(RED),
            ratio_t2_line4.animate.set_color(RED),
            FadeIn(high_variance)
        )
        
        self.next_slide()
        
        
        self.play(
            ratio_t_line2.animate.set_color("#FABF7F"),
            ratio_t_line3.animate.set_color("#FABF7F"),
            ratio_t1_line3.animate.set_color("#C17FFA"),
            ratio_t1_line4.animate.set_color("#C17FFA"),
            ratio_t_line4.animate.set_color("#FABF7F"),
            ratio_t2_line4.animate.set_color("#C17FFA"),
            FadeOut(high_variance)
        )
        
        
        # ── Define rho and c equations ────────────────────────────────────────────────
        c = MathTex(r"\min \left(\bar{c},\frac{\pi_{2}(a_i|s_i)}{\pi_{1}(a_i|s_i)} \right)", font_size=32)
        rho = MathTex(r"\min \left(\bar{\rho},\frac{\pi_{2}(a_t|s_t)}{\pi_{1}(a_t|s_t)} \right)", font_size=32)

        #position them to the right of unrolled_is
        rho.to_edge(RIGHT, buff=1.0).shift(UP * 1.5)
        c.to_edge(RIGHT, buff=1.0).shift(DOWN * 0.5)

        self.play(FadeIn(rho), FadeIn(c))
        self.next_slide()
        
        self.play(rho.animate.set_color("#FABF7F"), c.animate.set_color("#C17FFA"))

        # ── Arrows from ratio_t_* → rho ───────────────────────────────────────────────
        arrow_rho_1 = Arrow(
            start=ratio_t_line2.get_right(),
            end=rho.get_left(),
            buff=0.1, tip_length=0.15, stroke_width=2
        ).set_color("#FABF7F")

        arrow_rho_2 = Arrow(
            start=ratio_t_line3.get_right(),
            end=rho.get_left(),
            buff=0.1, tip_length=0.15, stroke_width=2
        ).set_color("#FABF7F")

        arrow_rho_3 = Arrow(
            start=ratio_t_line4.get_right(),
            end=rho.get_left(),
            buff=0.1, tip_length=0.15, stroke_width=2
        ).set_color("#FABF7F")

        # ── Arrows from ratio_t1/t2_* → c ────────────────────────────────────────────
        arrow_c_1 = Arrow(
            start=ratio_t1_line3.get_right(),
            end=c.get_left(),
            buff=0.1, tip_length=0.15, stroke_width=2
        ).set_color("#C17FFA")

        arrow_c_2 = Arrow(
            start=ratio_t1_line4.get_right(),
            end=c.get_left(),
            buff=0.1, tip_length=0.15, stroke_width=2
        ).set_color("#C17FFA")

        arrow_c_3 = Arrow(
            start=ratio_t2_line4.get_right(),
            end=c.get_left(),
            buff=0.1, tip_length=0.15, stroke_width=2
        ).set_color("#C17FFA")

        # ── Animate arrows and highlight ratios simultaneously ────────────────────────
        self.play(
            #draw rho arrows
            DrawBorderThenFill(arrow_rho_1),
            DrawBorderThenFill(arrow_rho_2),
            DrawBorderThenFill(arrow_rho_3),
        )
        self.play(
            DrawBorderThenFill(arrow_c_1),
            DrawBorderThenFill(arrow_c_2),
            DrawBorderThenFill(arrow_c_3),
        )
        low_variance_and_bias = high_variance = Tex(r"\textbf{Low Variance + some Bias}").set_color(GREEN).next_to(line_4,DOWN).set_x(0)
        self.play(FadeIn(low_variance_and_bias))
        

        self.next_slide()

        self.play(FadeOut(low_variance_and_bias,arrow_c_3,arrow_c_2,arrow_c_1,arrow_rho_3,arrow_rho_2,arrow_rho_1,rho,c,unrolled_is))        
        
        #UPGO
        self.play(technique_terms[0].animate.set_color("#363636"), technique_terms[1].animate.set_color("#363636"),technique_terms[2].animate.set_color(WHITE))

        what_upgo = Tex(r"It moves the \textbf{policy} towards trajectories with \textbf{better than} \\ \textbf{expected rewards} by updating in the direction of", font_size=30).next_to(win_rate_question, 2*DOWN)
        
        upgo_update = MathTex(
                r"\left(",
                r"G_{t}^U",                                    # [1] — easily accessible
                r"- V_{w}(s_t,z)",
                r"\right)",
                r"\nabla_{\theta} \log \pi_{\theta}(a_t|s_t,z)",
                font_size=32
            ).next_to(what_upgo, 2*DOWN)
        
        G_t_U = upgo_update[1]  # named reference for easy access
        
        where = Tex(r"where", font_size = 30).next_to(upgo_update, 1.5*DOWN)
        
        upgo_logic = MathTex(r"""G_t^U = 
            \begin{cases}
            r_t + G_{t+1}^U & \text{if } r_t + V_{w}(s_{t+1},z) \ge V_{w}(s_{t+1}, z)\\
            r_t + V_{w}(s_{t+1}, z) & \text{otherwise}
            \end{cases}""", font_size = 32).next_to(where, 1.5*DOWN)

        
        self.play(FadeIn(what_upgo))
        self.next_slide()
        self.play(FadeIn(upgo_update),FadeIn(where),FadeIn(upgo_logic))
        self.next_slide()
        self.play(Indicate(G_t_U))
        self.next_slide()
        
        
        
        ####### UNROLL UPGO
        
        self.play(FadeOut(what_upgo,upgo_update,where,upgo_logic))
        lets_unroll = Tex(r"Let's unroll this \\ (3 better than expected steps + 1 worse than expected)", font_size=30).next_to(win_rate_question, 2*DOWN)
        self.play(FadeIn(lets_unroll))
        self.next_slide()
        
        
        
        # ── Define each line separately for individual control ────────────────────────
        gtu_line1 = MathTex(
            r"G_t^U",
            r"= r_t +",
            r"G_{t+1}^U",
            font_size=32
        )

        gtu_line2 = MathTex(
            r"= r_t + (",
            r"r_{t+1} +",
            r"G_{t+2}^U",
            r")",
            font_size=32
        )

        gtu_line3 = MathTex(
            r"= r_t + r_{t+1} + (",
            r"r_{t+2} +",
            r"G_{t+3}^U",
            r")",
            font_size=32
        )

        gtu_line4 = MathTex(
            r"= r_t + r_{t+1} + r_{t+2} + (",
            r"r_{t+3} +",
            r"V(s_{t+4}, z)",
            r")",
            font_size=32
        )

        gtu_line5 = MathTex(
            r"= r_t + r_{t+1} + r_{t+2} + r_{t+3} +",
            r"V(s_{t+4}, z)",
            font_size=32
        )

        # ── Stack and left-align ──────────────────────────────────────────────────────
        gtu_proof = VGroup(gtu_line1, gtu_line2, gtu_line3, gtu_line4, gtu_line5)
        gtu_proof.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        gtu_proof.move_to(ORIGIN)
        gtu_proof.shift(1.5*DOWN)
        gtu_line2.shift(0.6*RIGHT)
        gtu_line3.shift(0.6*RIGHT)
        gtu_line4.shift(0.6*RIGHT)
        gtu_line5.shift(0.6*RIGHT)
        

        #named G references (the recurring term at the end of each line)
        G_line1 = gtu_line1[2]   # G_{t+1}^U
        G_line2 = gtu_line2[2]   # G_{t+2}^U
        G_line3 = gtu_line3[2]   # G_{t+3}^U

        # ── Line 1 appears ────────────────────────────────────────────────────────────
        self.play(Write(gtu_line1))
        self.next_slide()
        self.play(Indicate(gtu_line1,color=GREEN))

        # ── Line 2 appears, G of line 1 highlighted ───────────────────────────────────
        self.play(
            G_line1.animate.set_color(YELLOW),
        )
        self.play(
            FadeIn(gtu_line2),
            G_line1.animate.set_color(WHITE),
        )
        self.next_slide()
        self.play(Indicate(gtu_line2,color=GREEN))
        # ── Line 3 appears, G of line 2 highlighted ───────────────────────────────────
        self.play(
            G_line2.animate.set_color(YELLOW),
        )
        self.play(
            FadeIn(gtu_line3),
            G_line2.animate.set_color(WHITE),
        )
        self.next_slide()
        self.play(Indicate(gtu_line3,color=GREEN))
        # ── Line 4 appears, G of line 3 highlighted ───────────────────────────────────
        self.play(
            G_line3.animate.set_color(YELLOW),
        )
        self.play(
            FadeIn(gtu_line4),
            G_line3.animate.set_color(WHITE),
        )
        self.next_slide()
        self.play(Indicate(gtu_line4,color=RED))
        # ── Line 5 appears (no more G to highlight, V replaces it) ───────────────────
        self.play(
            gtu_line4[2].animate.set_color(YELLOW),  #highlight V(s_{t+4}, z)
        )
        self.play(
            FadeIn(gtu_line5),
            gtu_line4[2].animate.set_color(WHITE),
        )
        self.next_slide()
        
        
        td_text = Tex(r"Allows for n-step returns",font_size=30)
        v_trace_text = Tex(r"Allows for re-using experience and keeping variance low",font_size=30)
        upgo_text = Tex(r"Allows for reinforcing better than expected n-step trajectories",font_size=30)
        
        texts = VGroup(td_text,v_trace_text,upgo_text)
        texts.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        texts.move_to(ORIGIN)
        
        
        self.play(FadeOut(gtu_proof,win_rate_question, lets_unroll),
                  technique_terms[0].animate.set_color(WHITE), technique_terms[1].animate.set_color(WHITE))
        self.play(FadeIn(texts))

        self.next_slide()

        self.play(FadeOut(texts, technique_terms[0],technique_terms[1],technique_terms[2]))

        win_rate_question.next_to(win_rate_arrow, RIGHT)
        self.play(FadeIn(rl_items_group), FadeIn(win_rate_arrow), FadeIn(opponent_mixture_arrow), FadeIn(opponent_question), FadeIn(win_rate_question))

        self.next_slide()

        self.play(Indicate(opponent_question))

        self.next_slide()

        self.play(FadeOut(rl_items_group),
                  FadeOut(win_rate_arrow),
                  FadeOut(opponent_mixture_arrow),
                  FadeOut(win_rate_question),
                  opponent_question.animate.next_to(reinforcement_learning_title, DOWN))


        league_training = Tex(r"\textbf{League Training}: consists of \textbf{3 different types of agents} differing primarily in their mechanism for \textbf{selecting the opponent mixture}", font_size =30).next_to(opponent_question,DOWN)
        
        rect_ma = Tex(r"Main Agents", font_size=32)
        rect_me = Tex(r"Main Exploiters", font_size=32)
        rect_le = Tex(r"League Exploiters", font_size=32)

        #find the largest dimensions across all labels
        max_width  = max(rect_ma.width, rect_me.width, rect_le.width) + 0.6
        max_height = max(rect_ma.height, rect_me.height, rect_le.height) + 0.4

        def make_box(text_mob, color=RED):
            box = RoundedRectangle(
                corner_radius=0.2,
                width=max_width,
                height=max_height,
                color=color,
                fill_color=color,
                fill_opacity=0.3
            )
            box.move_to(text_mob.get_center())
            return VGroup(box, text_mob)

        box_ma_group = make_box(rect_ma)
        box_me_group = make_box(rect_me)
        box_le_group = make_box(rect_le)

        #arrange all three in a row
        all_boxes = VGroup(box_ma_group, box_me_group, box_le_group)
        all_boxes.arrange(RIGHT, buff=0.5)
        all_boxes.move_to(ORIGIN)

        self.play(FadeIn(box_ma_group, box_me_group, box_le_group,league_training))
        
        self.next_slide()
        
        self.play(box_ma_group.animate.to_edge(LEFT), FadeOut(box_me_group, box_le_group), FadeOut(league_training))
        ma_box_description = Tex(r"The output of \\ the training", font_size = 30).next_to(box_ma_group, DOWN)
        self.play(FadeIn(ma_box_description))
        item1_ma = Tex(r"$\bullet$ Play against all league members with \textbf{PFSP}", font_size=30)
        item2_ma = Tex(r"$\bullet$ Every $2\times 10^{9}$ steps, a frozen copy of the agent is added to the league", font_size=30)
        ma_text = VGroup(item1_ma, item2_ma).arrange(DOWN, aligned_edge=LEFT).next_to(box_ma_group, 2*RIGHT)
        
        self.play(FadeIn(ma_text))
        
        self.next_slide()
        
        box_me_group.to_edge(LEFT)
        self.play(FadeOut(ma_text, box_ma_group), FadeIn(box_me_group), FadeOut(ma_box_description))
        
        item1_me = Tex(r"$\bullet$ Play just against Main Agents", font_size=30)
        item2_me = Tex(r"$\bullet$ May use \textbf{PFSP} over saved copies of the Main Agents", font_size=30)
        item3_me = Tex(r"$\bullet$ Frozen copies are regularly added to the league", font_size=30)
        item4_me = Tex(r"$\bullet$ After saving the copy: reset to supervised parameters", font_size=30)
        me_text = VGroup(item1_me, item2_me, item3_me, item4_me).arrange(DOWN, aligned_edge=LEFT).next_to(box_me_group, 2*RIGHT)
        me_box_description = Tex(r"Identify \\ weaknesses in \\ the Main Agent", font_size = 30).next_to(box_me_group, DOWN)
        self.play(FadeIn(me_box_description))
        self.play(FadeIn(me_text))
        
        self.next_slide()
        box_le_group.to_edge(LEFT)
        self.play(FadeOut(me_text, box_me_group), FadeIn(box_le_group), FadeOut(me_box_description))
        
        item1_le = Tex(r"$\bullet$ Play against all league members with \textbf{PFSP}", font_size=30)
        item2_le = Tex(r"$\bullet$ Frozen copies are regularly added to the league", font_size=30)
        item3_le = Tex(r"$\bullet$ After saving the copy: $25\%$ chance of reset to supervised parameters", font_size=30)
        le_text = VGroup(item1_le, item2_le, item3_le).arrange(DOWN, aligned_edge=LEFT).next_to(box_le_group, 2*RIGHT)
        le_box_description = Tex(r"Identify \\ weaknesses in \\ the League", font_size = 30).next_to(box_le_group, DOWN)
        self.play(FadeIn(le_box_description))
        self.play(FadeIn(le_text))
        
        self.next_slide()
        self.play(FadeOut(le_text,le_box_description,box_le_group))
        
        psfp_text = Tex(r"Prioritized Fictitious Self-Play (PFSP) is a matchmaking mechanism studied to provide a good learning signal to agents during training", font_size = 30).next_to(opponent_question, 2*DOWN)
        pfsp_theorem = Tex(r"Given a learning agent $\textbf{A}$, we sample the frozen opponent $\textbf{B}$ from a candidate set $\mathcal{C}$ with probability", font_size = 30).next_to(psfp_text,2*DOWN)
        
        psfp_prob = MathTex(r"\frac{f(\mathbb{P}(A \text{ beats } B))}{\sum_{c \in C} f(\mathbb{P}(A \text{ beats } c))}", font_size = 35).next_to(pfsp_theorem, 2*DOWN)
        
        pfsp = VGroup(psfp_text,pfsp_theorem,psfp_prob)
        
        self.play(FadeIn(pfsp))
        
        
        self.next_slide()
        self.play(FadeOut(psfp_text,pfsp_theorem), psfp_prob.animate.to_edge(LEFT).set_y(0))
        
        # ── Axes (shifted right to avoid pfsp_prob) ───────────────────────────────────
        axes = Axes(
            x_range=[0, 1, 0.25],
            y_range=[0, 1, 0.25],
            x_length=4.5,
            y_length=3.5,
            axis_config={"include_numbers": True, "font_size": 20},
        ).shift(0.2* RIGHT + DOWN * 0.3)

        axes_labels = axes.get_axis_labels(
            x_label=Tex("x", font_size=24),
            y_label=Tex("", font_size=24)
        )

        self.play(Create(axes), Write(axes_labels))
        self.next_slide()

        # ── Step 1: Hardness function ─────────────────────────────────────────────────
        graph_hard = axes.plot(
            lambda x: (1 - x) ** 2.5,
            x_range=[0, 1],
            color=GREEN
        )

        eq_hard = MathTex(
            r"f_{\text{hard}}(x) = (1-x)^{2.5}",
            font_size=35,
            color=GREEN
        ).to_edge(RIGHT, buff=0.4).shift(0.5 * UP + 0.5 * LEFT)

        self.play(Create(graph_hard), Write(eq_hard))
        self.next_slide()

        # ── Step 2: Variance function ─────────────────────────────────────────────────
        graph_var = axes.plot(
            lambda x: x * (1 - x),
            x_range=[0, 1],
            color="#ADD8E6"
        )

        eq_var = MathTex(
            r"f_{\text{var}}(x) = x(1-x)",
            font_size=35,
            color="#ADD8E6"
        ).to_edge(RIGHT, buff=0.4).shift(0.5 * DOWN + 0.8 * LEFT)

        self.play(Create(graph_var), Write(eq_var))
        self.next_slide()
        
        self.play(FadeOut(axes,axes_labels,graph_hard,eq_hard,graph_var,eq_var,opponent_question,reinforcement_learning_title,psfp_prob))
        
        
        ####ARCHITECTURE
        arch_img = ImageMobject("assets/architecture.png")
        arch_img.scale(0.7)
        self.play(FadeIn(arch_img))
        
        
        
        ######RESULTS
        self.next_slide()
        
        self.play(FadeOut(arch_img))
        
        results = Tex(r"Results").next_to(title,DOWN)
        test_results1 = Tex(r"\textbf{AlphaStar Final} (after RL training): $> 99.8\%$ of ranked human players", font_size=30).next_to(results,1.5*DOWN)
        test_results2 = Tex(r"\textbf{AlphaStar Supervised} (after SL training): $> 84\%$ of ranked human players", font_size=30).next_to(test_results1, DOWN)
        res_img = ImageMobject("assets/results.png")
        res_img.scale(0.6)
        res_img.next_to(test_results2, DOWN, buff=0.2)
        
        self.play(FadeIn(results,test_results1,test_results2,res_img))
        