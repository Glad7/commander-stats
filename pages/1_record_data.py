from entry_screen import *

st.set_page_config(page_title="Record a Commander Game")

with st.form("game_form"):
    st.subheader("🗓 Game Metadata")
    date = st.date_input("Date")
    format_type = st.text_input("Format", value="Commander")
    playgroup = st.text_input("Playgroup")
    game_name = st.text_input("Game Name")
    bracket = st.text_input("Bracket")
    platform = st.text_input("Platform")

    st.subheader("👥 Players")
    players = []
    commanders = []
    mulligans = []

    num_players = st.slider("Number of Players", 2, 4, 4)

    for i in range(num_players):
        with st.expander(f"Player {i+1}"):
            pname = st.text_input(f"Player {i+1} Name", key=f"p{i}")
            pcommander = st.text_input(f"Commander", key=f"c{i}")
            pmull = st.number_input("Mulligans", min_value=0, max_value=10, value=0, key=f"m{i}")
            players.append(pname)
            commanders.append(pcommander)
            mulligans.append(pmull)

    for _ in range(4 - num_players):  # pad to 4
        players.append("")
        commanders.append("")
        mulligans.append("")

    winner = st.selectbox("🏆 Winner", players[:num_players])
    time_mins = st.number_input("Game Length (Minutes)", min_value=1)
    turns = st.number_input("Total Turns", min_value=1)
    win_condition = st.text_input("Win Condition", placeholder="e.g. Infinite Combo")
    tags = st.text_input("Tags (comma-separated)")
    notes = st.text_area("Notes")

    submitted = st.form_submit_button("Submit Game")

if submitted:
    row = [
        str(date), format_type, playgroup, game_name, bracket, platform,
        *players, *commanders, *mulligans,
        winner, time_mins, turns, win_condition, tags, notes
    ]
    worksheet.append_row(row)
    st.success("Game recorded successfully!")