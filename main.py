import pprint
import click
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://stackoverflow.com'
SEARCH = f"{BASE_URL}/search?q="


def search(query):
    """Search query through stackoverflow search page

    :query: TODO
    :returns: TODO

    """
    resp = requests.get(f"{SEARCH}{query}")
    soup = BeautifulSoup(resp.content)

    result_count = soup.select_one(".fl1.fs-body3").text
    search_results = soup.select(".search-result .result-link a")
    next_ = soup.select_one("[rel='next']")['href']

    results = [{
        "title": result['title'],
        "url": f"{BASE_URL}{result['href']}"
    } for result in search_results]

    return {'count': result_count, 'results': results, 'next': f"{BASE_URL}{next_}"}


@click.command()
@click.argument('query', nargs=-1)
def searching(query):
    result = search(' '.join(query))
    pprint.pprint(result, indent=4)


if __name__ == "__main__":
    searching()
