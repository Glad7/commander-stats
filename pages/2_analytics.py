from entry_screen import *
from data import *

st.set_page_config(page_title="View Stats")

def load_sheet_data():
    worksheet = get_worksheet()
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

df = load_sheet_data()

# Flatten into long format for analysis
player_cols = ['Player1', 'Player2', 'Player3', 'Player4']
commander_cols = ['Player1Commander', 'Player2Commander', 'Player3Commander', 'Player4Commander']
mull_cols = ['Player1Mulligans', 'Player2Mulligans', 'Player3Mulligans', 'Player4Mulligans']

long_data = []

for idx, row in df.iterrows():
    for i in range(4):
        player = row[player_cols[i]]
        if player.strip() == "":
            continue
        long_data.append({
            "GameID": idx,
            "Date": row["Date"],
            "Player": player,
            "Commander": row[commander_cols[i]],
            "Mulligans": row[mull_cols[i]],
            "Winner": player == row["Winner"],
            "TotalTurns": row["TotalTurns"],
            "GameTimeMinutes": row["GameTimeMinutes"]
        })

long_df = pd.DataFrame(long_data)

# Win rate per player
win_rate = long_df.groupby("Player")["Winner"].mean().sort_values(ascending=False)
st.bar_chart(win_rate)

# Average game length
avg_turns = df["TotalTurns"].mean()
st.metric("Average Turns per Game", f"{avg_turns:.1f}")