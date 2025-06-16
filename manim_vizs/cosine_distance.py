from manim import *
import numpy as np


class CosineDistanceScene(Scene):
    def construct(self):
        # Create vectors (using first two components for 2D visualization)
        v1 = [0.3, 0.7]
        v2 = [0.5, 0.2]

        # Start with text in center
        query_text = Text('"Ada is the cutest pair programmer"', font_size=32)
        topic_text = Text(
            '"Ada Lovelace was the world\'s first programmer"', font_size=32
        ).next_to(query_text, DOWN, buff=1)

        self.play(Write(query_text), Write(topic_text))
        self.wait(1)

        # Move both texts to left edge
        self.play(query_text.animate.to_edge(LEFT), topic_text.animate.to_edge(LEFT))
        self.wait(1)

        # Create vectors already positioned at left edge
        query_vec_with_label = MathTex(r"\vec{v1} = " + str(v1), color=BLUE).to_edge(
            LEFT
        )
        topic_vec_with_label = (
            MathTex(r"\vec{v2} = " + str(v2), color=RED)
            .to_edge(LEFT)
            .next_to(query_vec_with_label, DOWN, buff=1)
        )

        # Transform to vectors
        self.play(
            ReplacementTransform(query_text, query_vec_with_label),
            ReplacementTransform(topic_text, topic_vec_with_label),
        )
        self.wait(1)

        # remove labels
        query_vec = MathTex(str(v1), color=BLUE).to_edge(LEFT)
        topic_vec = (
            MathTex(str(v2), color=RED).to_edge(LEFT).next_to(query_vec, DOWN, buff=1)
        )
        self.play(
            ReplacementTransform(query_vec_with_label, query_vec),
            ReplacementTransform(topic_vec_with_label, topic_vec),
        )
        self.wait(1)

        # Create 2D axes in center of screen
        axes = Axes(
            x_range=[0, 0.6, 0.1],
            y_range=[0, 1, 0.1],
        ).scale(0.5)

        # Create 2D arrows for vectors
        vector1 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*v1), color=BLUE, buff=0.1)
        vector2 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*v2), color=RED, buff=0.1)

        # Draw axes and vectors
        self.play(
            Create(axes),
            Create(vector1),
            Create(vector2),
        )
        self.wait(1)

        # Move the vector labels to the ends of the arrows
        self.play(
            query_vec.animate.next_to(vector1.get_end(), RIGHT).scale(0.7),
            topic_vec.animate.next_to(vector2.get_end(), RIGHT).scale(0.7),
        )
        self.wait(1)

        # Move entire graph to left
        graph_group = VGroup(axes, vector1, vector2, query_vec, topic_vec)
        self.play(graph_group.animate.to_edge(LEFT, buff=1))
        self.wait(1)

        # Draw arc
        theta_label = MathTex(r"\theta").move_to(vector1.get_end() + DOWN)
        self.play(Write(theta_label))
        self.wait(1)

        # cosine distance formula center
        cosine_distance_formula_1 = MathTex(r"1 - \cos(\theta)").to_edge(RIGHT, buff=1)
        self.play(Write(cosine_distance_formula_1))
        self.wait(2)

        # transform into full cosine similarity formula
        cosine_distance_formula_2 = MathTex(
            r"\cos(\theta) = \frac{\vec{v1} \cdot \vec{v2}}{||\vec{v1}|| \cdot ||\vec{v2}||}"
        ).to_edge(RIGHT, buff=1)
        self.play(
            ReplacementTransform(cosine_distance_formula_1, cosine_distance_formula_2)
        )
        self.wait(1)

        # Replace transform into single number
        cosine_similarity = 0.707107
        cosim_text = MathTex(str(cosine_similarity)).to_edge(RIGHT, buff=1)
        cosim_label = Text("Cosine Similarity", font_size=24).next_to(
            cosim_text,
            UP,
            buff=0.1,
        )
        cosim_text_group = VGroup(cosim_text, cosim_label)
        self.play(
            ReplacementTransform(cosine_distance_formula_2, cosim_text_group),
        )
        self.wait(1)

        cos_dist_text = MathTex(r"1 - ").shift(cosim_text_group.get_left() + LEFT)
        self.play(Write(cos_dist_text))
        self.wait(1)

        cos_dist_value = round(1 - cosine_similarity, 2)
        cos_dist_label = Text("Cosine Distance", font_size=28).next_to(
            cos_dist_value, UP, buff=0.1
        )
        cos_dist_value_text = VGroup(
            MathTex(str(cos_dist_value), font_size=36),
            cos_dist_label,
        ).shift(cos_dist_text.get_center(), LEFT)

        self.play(
            ReplacementTransform(
                cosim_text_group,
                cos_dist_value_text,
            ),
            ReplacementTransform(cos_dist_text, cos_dist_value_text),
        )
        self.wait(1)
