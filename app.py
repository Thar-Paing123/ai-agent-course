import argparse
import json
from urllib import error, request

API_URL = "https://official-joke-api.appspot.com/random_joke"


def fetch_joke():
    try:
        with request.urlopen(API_URL, timeout=10) as response:
            payload = response.read()
    except error.URLError as exc:
        raise RuntimeError(f"Unable to fetch joke from {API_URL}: {exc}") from exc

    joke = json.loads(payload)
    if "setup" not in joke or "punchline" not in joke:
        raise ValueError(f"Unexpected joke payload: {joke!r}")
    return joke


def main():
    parser = argparse.ArgumentParser(description="Fetch a joke from a public API.")
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of jokes to fetch (default: 1)",
    )
    args = parser.parse_args()

    if args.count < 1:
        parser.error("--count must be at least 1")

    for index in range(args.count):
        joke = fetch_joke()
        print(f"Joke {index + 1}:")
        print("Setup:", joke["setup"])
        print("Punchline:", joke["punchline"])
        if index < args.count - 1:
            print()


if __name__ == "__main__":
    main()