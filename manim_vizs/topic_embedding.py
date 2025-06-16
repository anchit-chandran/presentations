from manim import *
import numpy as np


class TopicEmbedding(Scene):
    def construct(self):
        # Topic components
        topic_name = Text("topic_name: 'ada-the-cat'", font_size=30)
        topic_content = Text("topic_content: 'Ada is the best cat'", font_size=30)
        sample_query_title = Text("Sample queries:", font_size=20)
        sample_query1 = Text("'why is ada so cute?'", font_size=30)
        sample_query2 = Text("'i really love ada'", font_size=30)

        # Create group and position at left edge
        topic_group = VGroup(
            topic_name, topic_content, sample_query_title, sample_query1, sample_query2
        )
        topic_group.arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(LEFT * 3)

        self.play(Write(topic_group))

        # Create embeddings
        def create_embedding_vector():
            return np.random.uniform(-1, 1, 3)  # 3D vector for simplicity

        # Embedding vectors
        name_embedding = create_embedding_vector()
        content_embedding = create_embedding_vector()
        combined_embedding = name_embedding + content_embedding
        query1_embedding = create_embedding_vector()
        query2_embedding = create_embedding_vector()

        # Create vector representations
        def vector_to_text(vector):
            return Text(
                f"[{', '.join([f'{x:.2f}' for x in vector])}]",
                font_size=24,
            )

        name_vec_text = vector_to_text(name_embedding)
        content_vec_text = vector_to_text(content_embedding)
        # name_content_vec_text = vector_to_text(name_embedding + content_embedding)
        query1_vec_text = vector_to_text(query1_embedding)
        query2_vec_text = vector_to_text(query2_embedding)
        embeddings_group = (
            VGroup(name_vec_text, content_vec_text, query1_vec_text, query2_vec_text)
            .arrange(DOWN, buff=0.5, aligned_edge=RIGHT)
            .shift(RIGHT * 3)
        )

        # Show all together
        self.play(
            AnimationGroup(
                Create(Arrow(topic_name.get_right(), name_vec_text.get_left())),
                Create(Arrow(topic_content.get_right(), content_vec_text.get_left())),
                Create(Arrow(sample_query1.get_right(), query1_vec_text.get_left())),
                Create(Arrow(sample_query2.get_right(), query2_vec_text.get_left())),
                Write(embeddings_group),
            )
        )

        # Plus sign between name and content embeddings
        plus_sign = Text("+", font_size=30)
        plus_sign.move_to((name_vec_text.get_bottom() + content_vec_text.get_top()) / 2)
        self.play(Write(plus_sign))
        self.wait()

        # Combine name and content embeddings into 1 embedding
        combined_embedding = name_embedding + content_embedding
        combined_vec_text = vector_to_text(combined_embedding)
        combined_vec_text.move_to(plus_sign.get_center())

        # transform topic name and content embeddings into combined embedding
        self.play(
            Transform(name_vec_text, combined_vec_text),
            Transform(content_vec_text, combined_vec_text),
            Transform(plus_sign, combined_vec_text),
        )
        self.wait(2)
