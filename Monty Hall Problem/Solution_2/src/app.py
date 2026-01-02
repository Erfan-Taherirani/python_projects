import time


import streamlit as st


from src.monty_hall import simulate_problem


st.image("https://mathematicalmysteries.org/wp-content/uploads/2021/12/04615-0sxvwbnzvvnhuklug.png", width=500)
st.title(":zap: Monty Hall Problem Simulation")

num_simulations = st.number_input("NUmebr of Simulations",
                min_value=1, max_value=10000)

col1, col2 = st.columns(2)
col1.subheader("Win Percentage with Switching")
col2.subheader("Win Percentage without Switching")
chart1 = col1.line_chart(x=None, y=None, width=500)
chart2 = col2.line_chart(x=None, y=None, width=500)

wins_switch = 0
wins_no_switch = 0

chart1.add_rows([1.0])
chart2.add_rows([1.0])
for i in range(num_simulations):
    num_wins_with_switching, num_wins_without_switching = simulate_problem(1)

    wins_switch += num_wins_with_switching
    wins_no_switch += num_wins_without_switching

    chart1.add_rows([wins_switch / (i + 1)])
    chart2.add_rows([wins_no_switch / (i + 1)])

    time.sleep(0.01)
