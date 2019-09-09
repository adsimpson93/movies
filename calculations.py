import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def get_top_genres(rows):
    """Returns List of top genres and average profit in order of greatest to least"""
    genresData = {}

    c = 0
    for row in rows:
        genres = row[0].split("|")
        for g in genres:
            if genresData.get(g) == None:
                genresData[g] = [0, 0, 0, 0]  # count, gross, budget, profit avg
            genresData[g][0] = genresData[g][0] + 1
            genresData[g][1] = genresData[g][1] + float(row[1])
            genresData[g][2] = genresData[g][2] + float(row[2])

    genreByProfits = [["placeholder", float("-inf")]]
    for g in genresData:
        genresData[g][3] = (genresData[g][1] - genresData[g][2]) / genresData[g][0]
        for i in range(0, len(genreByProfits)):
            if genresData[g][3] > genreByProfits[i][1]:
                genreByProfits.insert(i, [g, genresData[g][3]])
                break

    genreByProfits.pop()

    return genreByProfits


def get_top_actors(rows):
    """Returns List of top actors and average profit in order of greatest to least"""
    actorData = {}
    for row in rows:
        for a in [row[0], row[1], row[2]]:
            if a != None and a != "":
                if actorData.get(a) == None:
                    actorData[a] = [0, 0, 0, 0]  # count, gross, budget, profit avg
                actorData[a][0] = actorData[a][0] + 1
                actorData[a][1] = actorData[a][1] + float(row[3])
                actorData[a][2] = actorData[a][2] + float(row[4])

    actorsByProfits = [["placeholder", float("-inf")]]
    for g in actorData:
        actorData[g][3] = (actorData[g][1] - actorData[g][2]) / actorData[g][0]
        for i in range(0, len(actorsByProfits)):
            if actorData[g][3] > actorsByProfits[i][1]:
                actorsByProfits.insert(i, [g, actorData[g][3]])
                break

    actorsByProfits.pop()

    return actorsByProfits


def get_top_actors_director_pairs(rows):
    """Returns List of top actors/director and their average imbd scores"""
    directors = {}

    for r in rows:
        d = r[4]
        if d != None and d != "":
            if directors.get(d) == None:
                directors[d] = {}
            for a in [r[1], r[2], r[3]]:
                if a != None and a != "":
                    if directors[d].get(a) == None:
                        directors[d][a] = [0, 0, 0]  # score, count, imbd avg
                    directors[d][a][0] = directors[d][a][0] + float(r[0])
                    directors[d][a][1] = directors[d][a][1] + 1

    pairs = [["placeholder director", "placeholder actor", float("-inf")]]
    for d in directors:
        for a in directors[d]:
            directors[d][a][2] = directors[d][a][0] / directors[d][a][1]
            for i in range(0, len(pairs)):
                if directors[d][a][2] > pairs[i][2]:
                    pairs.insert(i, [d, a, directors[d][a][2]])
                    break

    pairs.pop()

    return pairs


def main():
    database = "movies.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("\nTop 10 Genres:")
        cur = conn.cursor()
        cur.execute(
            'SELECT genres, gross, budget FROM movies WHERE (gross IS NOT NULL AND gross != "") AND (budget IS NOT NULL AND budget != "") AND (genres IS NOT NULL AND budget != "")'
        )
        rows = cur.fetchall()
        topGenres = get_top_genres(rows)
        for i in range(0, 10):
            print(str(topGenres[i][0]) + ": " + str(topGenres[i][1]))

        print("\n\nTop 10 Actors:")
        cur.execute(
            'SELECT actor_1_name, actor_2_name, actor_3_name, gross, budget FROM movies WHERE (gross IS NOT NULL AND gross != "") AND (budget IS NOT NULL AND budget != "")'
        )
        rows = cur.fetchall()
        topActors = get_top_actors(rows)
        for i in range(0, 10):
            print(str(topActors[i][0]) + ": " + str(topActors[i][1]))

        print("\n\nTop 10 Director/Actor Pairs:")
        cur.execute(
            "SELECT imdb_score, actor_1_name, actor_2_name, actor_3_name, director_name FROM movies"
        )
        rows = cur.fetchall()
        topPairs = get_top_actors_director_pairs(rows)
        for i in range(0, 10):
            print(
                str(topPairs[i][0])
                + " - "
                + str(topPairs[i][1])
                + ": "
                + str(topPairs[i][2])
            )


if __name__ == "__main__":
    main()
