from manim import *
import numpy as np


class CosineDistanceScene(Scene):
    def construct(self):
        # Create vectors (using first two components for 2D visualization)
        v1 = [0.3, 0.7]
        v2 = [0.5, 0.2]

        # Start with text in center
        query_text = Text(
            '"Ada is the cutest pair programmer"', font_size=32, color=BLUE
        )
        topic_text = Text(
            '"Ada Lovelace was the world\'s first programmer"', font_size=32, color=RED
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

        # Create 2D axes in center of screen
        axes = Axes(
            x_range=[0, 0.6, 0.1],
            y_range=[0, 1, 0.1],
        ).scale(0.5)

        # Create 2D arrows for vectors
        vector1 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*v1), color=BLUE, buff=0.1)
        vector2 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*v2), color=RED, buff=0.1)

        # remove labels
        query_vec = MathTex(str(v1), color=BLUE).to_edge(LEFT)
        topic_vec = (
            MathTex(str(v2), color=RED).to_edge(LEFT).next_to(query_vec, DOWN, buff=1)
        )
        self.play(
            ReplacementTransform(query_vec_with_label, query_vec),
            ReplacementTransform(topic_vec_with_label, topic_vec),
            Create(axes),
            Create(vector1),
            Create(vector2),
        )
        self.wait(2)

        # Move the vector labels to the ends of the arrows
        self.play(
            query_vec.animate.next_to(vector1.get_end(), RIGHT).scale(0.7),
            topic_vec.animate.next_to(vector2.get_end(), RIGHT).scale(0.7),
        )
        self.wait(2)

        # Move entire graph to left
        graph_group = VGroup(axes, vector1, vector2, query_vec, topic_vec)
        self.play(graph_group.animate.to_edge(LEFT, buff=1))
        self.wait(1)

        # Go from vector to text
        query_text = (
            Text('"Ada is the cutest pair programmer"', font_size=32, color=BLUE)
            .next_to(vector1.get_end(), RIGHT)
            .scale(0.7)
        )
        topic_text = (
            Text(
                '"Ada Lovelace was the world\'s first programmer"',
                font_size=32,
                color=RED,
            )
            .next_to(vector2.get_end(), RIGHT)
            .scale(0.7)
        )
        self.play(
            ReplacementTransform(query_vec, query_text),
            ReplacementTransform(topic_vec, topic_text),
        )
        self.wait(1)

        # Create new vector labels in the correct positions
        new_query_vec = (
            MathTex(str(v1), color=BLUE).next_to(vector1.get_end(), RIGHT).scale(0.7)
        )
        new_topic_vec = (
            MathTex(str(v2), color=RED).next_to(vector2.get_end(), RIGHT).scale(0.7)
        )

        self.play(
            ReplacementTransform(query_text, new_query_vec),
            ReplacementTransform(topic_text, new_topic_vec),
        )

        # Draw arc between vectors
        arc = Arc(
            radius=2.5,  # Adjust as needed
            start_angle=vector1.get_angle(),
            angle=vector2.get_angle() - vector1.get_angle(),
            color=YELLOW,
        )
        # Move arc to the origin of the axes
        arc.move_arc_center_to(axes.c2p(0, 0))
        self.play(Create(arc))
        self.wait(1)

        # Draw arc
        theta_label = MathTex(
            r"\theta",
            color=YELLOW,
        ).move_to(vector1.get_end() + DOWN)
        self.play(Write(theta_label))
        self.wait(1)

        # cosine distance formula center
        cosine_distance_formula_1 = MathTex(r"1 - \cos(\theta)", color=YELLOW).to_edge(
            RIGHT, buff=1
        )
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

        # Replace transform into cosine similarity scalar
        cosine_similarity = 0.707107
        cosim_text = MathTex(str(cosine_similarity), font_size=36).move_to(
            cosine_distance_formula_2.get_center()
        )
        cosim_label = Text(
            "Cosine Similarity cos(θ)", font_size=32, color=YELLOW
        ).next_to(cosim_text, UP, buff=0.1)
        cosim_text_group = VGroup(cosim_label, cosim_text)
        self.play(
            ReplacementTransform(cosine_distance_formula_2, cosim_text_group),
        )
        self.wait(2)

        # Transform into cosine distance
        cos_dist_label = Text(
            "Cosine Distance (1 - cos(θ))", font_size=32, color=GREEN
        ).next_to(cosim_text, UP, buff=0.1)
        cos_dist_formula = MathTex(
            "1 - " + str(cosine_similarity), font_size=36, color=GREEN
        ).next_to(cos_dist_label, DOWN, buff=0.1)

        self.play(
            ReplacementTransform(cosim_label, cos_dist_label),
            ReplacementTransform(cosim_text, cos_dist_formula),
        )
        self.wait(1)

        # Show final cosine distance value
        cos_dist_value = round(1 - cosine_similarity, 2)
        final_cos_dist = (
            MathTex(str(cos_dist_value), font_size=72, color=GREEN)
            .move_to(cos_dist_formula.get_center())
            .shift(DOWN)
        )

        self.play(ReplacementTransform(cos_dist_formula, final_cos_dist))
        self.wait(2)

        # Final scene
        final_query_text = Text(
            '"Ada is the cutest pair programmer"', font_size=32, color=BLUE
        )
        final_topic_text = Text(
            '"Ada Lovelace was the world\'s first programmer"', font_size=32, color=RED
        )
        final_cos_dist_center = MathTex("0.29", font_size=72, color=GREEN)

        # Create a VGroup for the final scene
        final_group = (
            VGroup(final_query_text, final_cos_dist_center, final_topic_text)
            .arrange(DOWN, buff=0.5)
            .move_to(ORIGIN)
        )

        # Create the cosine distance value at its current position
        current_cos_dist = MathTex("0.29", font_size=72, color=GREEN).move_to(
            cos_dist_formula.get_center()
        )

        # Transform existing elements into the final arrangement
        self.play(
            ReplacementTransform(query_text, final_query_text),
            ReplacementTransform(topic_text, final_topic_text),
            ReplacementTransform(current_cos_dist, final_cos_dist_center),
            *[
                FadeOut(mob)
                for mob in self.mobjects
                if mob not in [query_text, topic_text, current_cos_dist]
            ],
        )
        self.wait(4)
