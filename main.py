"""
Anime Information Finder

Uses the Jikan API to get information about an anime.
"""

import requests


# Function to get anime information
def get_anime_info(anime_name):

    url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"

    data = requests.get(url, timeout=10).json()

    anime = data["data"][0]

    title = anime["title"]
    episodes = anime["episodes"]
    score = anime["score"]
    status = anime["status"]
    synopsis = anime["synopsis"]

    return title, episodes, score, status, synopsis


# Main function
def main():

    print("Anime Information Finder\n")

    anime_name = input("Enter an anime name: ").strip()

    try:
        title, episodes, score, status, synopsis = get_anime_info(anime_name)

        print("\n--- Anime Information ---")
        print(f"Title: {title}")
        print(f"Episodes: {episodes}")
        print(f"Score: {score}")
        print(f"Status: {status}")
        print(f"Synopsis: {synopsis}")

    except:
        print("Anime not found.")


# Run program
if __name__ == "__main__":
    main()