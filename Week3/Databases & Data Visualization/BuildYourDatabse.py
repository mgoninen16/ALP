from replit import db

def add_game(opponent, minuteAverage):
    if opponent in db:
        print("Stats against this team already exist")
    else:
        db[opponent] = minuteAverage

def get_minutes(opponent):
    number = db.get(opponent)
    return number

def update_stats(oldTeamName, newTeamName, newNumber):
    db[newTeamName] = newNumber
    del db[oldTeamName]

def delete_team(opponent):
    del db[opponent]


add_game("Pacers", 41.5)
add_game("Heat", 38.0)
add_game("Knicks", 43.5)
add_game("Hornets", 45.0)
add_game("76ers", 43.5)
add_game("Raptors", 43.5)
add_game("Pistons", 38.0)
add_game("Bucks", 38.0)
add_game("Magic", 43.0)
add_game("Celtics", 41.0)
add_game("Cavaliers", 37.0)
add_game("Nets", 42.0)
add_game("Wizards", 42.0)
add_game("Hawks", 33.0)
add_game("Bulls", 45.0)
add_game("Jazz", 41.0)
add_game("Trail Blazers", 43.3)
add_game("Spurs", 35.3)
add_game("Suns", 43.3)
add_game("Timberwolves", 42.5)
add_game("SuperSonics", 40.0)
add_game("Kings", 43.8)
add_game("Mavericks", 39.5)
add_game("Nuggets", 40.8)
add_game("Rockets", 30.7)
add_game("Grizzlies", 38.5)
add_game("Warriors", 34.5)
add_game("Clippers", 37.3)
print("Complete!")