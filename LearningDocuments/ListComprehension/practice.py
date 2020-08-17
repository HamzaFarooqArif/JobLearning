print('abc'*3)

squares = [i**2 for i in range(1, 10)]
print(squares)

print("")
movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story"]
cmovies = [title for title in movies if title.startswith("S")]
print(cmovies)

print("")
movies2 = [("Star Wars", 1940), ("Gandhi", 1945), ("Casablanca", 1950), ("Shawshank Redemption", 1955), ("Toy Story", 1960)]
cmovies2 = [title for (title, year) in movies2 if year < 1950]
print(cmovies2)
