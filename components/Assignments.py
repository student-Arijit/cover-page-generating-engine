import streamlit as st
from components.handler import Handler


class AssignmentPage(Handler):

    def __init__(self):

        self.load_css("assets/style.css")

    def _render_header(self):

        st.markdown(
            """
            <div class="assignment-container">

                <div class="page-header">

                    <div class="header-left">

                        <div class="page-title">
                            Assignments
                        </div>

                        <div class="page-sub">
                            Manage your assignments using AI
                        </div>

                    </div>

                    <div class="badge-div">

                        <span class="badge green">
                            ● Active
                        </span>

                        <span class="badge blue">
                            GPT-4o
                        </span>

                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    def _render_cards(self):

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                """
                <div class="assignment-card">

                    <div class="card-icon">
                        📄
                    </div>

                    <div class="card-title">
                        Create Assignment
                    </div>

                    <div class="card-text">
                        Generate assignments using AI
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.button(
                "Create",
                key="create_btn",
                use_container_width=True
            )

        with col2:

            st.markdown(
                """
                <div class="assignment-card">

                    <div class="card-icon">
                        📚
                    </div>

                    <div class="card-title">
                        My Assignments
                    </div>

                    <div class="card-text">
                        View submitted assignments
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.button(
                "Open",
                key="open_btn",
                use_container_width=True
            )

        with col3:

            st.markdown(
                """
                <div class="assignment-card">

                    <div class="card-icon">
                        🤖
                    </div>

                    <div class="card-title">
                        AI Generator
                    </div>

                    <div class="card-text">
                        Create answers instantly
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.button(
                "Generate",
                key="generate_btn",
                use_container_width=True
            )

    def run(self):

        self._render_header()

        st.markdown("<br>", unsafe_allow_html=True)

        self._render_cards()