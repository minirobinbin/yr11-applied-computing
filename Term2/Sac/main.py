import sqlite3


database_path = "world_population.db"

create = """SELECT Rank, Country_Code, Growth_rate, World_Population_Percentage, Area FROM worldPopulationGrowth ORDER BY Area ASC;"""


with sqlite3.connect(database_path) as conn:
    cursor = conn.cursor()
    cursor.execute(create)
    conn.commit()
    results = cursor.fetchall()
    print("Rank | Country_Code | Growth_rate  | World_Population_Percentage  | Area")
    print("------------------------------------------------------------------------")
    for result in results:
        print(f"{result[0]}  | {result[1]}          | {result[2]}       | {result[3]}                           | {result[4]}")

    # print(results)