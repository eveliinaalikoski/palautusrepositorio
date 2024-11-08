from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    stats = PlayerStats(PlayerReader(url))

    top = stats.top_scorers_by_nationality("FIN")
    draw_table(top)


def draw_table(players_list):
    table = Table(title = "Top finnish players")

    table.add_column("name", style = "bold cyan", no_wrap = True)
    table.add_column("team", style = "green")
    table.add_column("goals", style = "magenta", justify = "center")
    table.add_column("assists", style = "magenta", justify = "center")
    table.add_column("points", style = "bold red", justify = "center")
    
    for player in players_list:
        table.add_row(player.name, 
                      player.team, 
                      str(player.goals),
                      str(player.assists),
                      str(player.points()))
        
    console = Console()
    console.print(table, justify = "center")

if __name__ == "__main__":
    main()
