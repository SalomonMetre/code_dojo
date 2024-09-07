import urllib.parse
import urllib.request

# number of results you want
NB_PAPERS=10

# title of the paper you're looking for
search_string = 'Attention is all you need. Vaswani'

encoded_search_string = urllib.parse.quote(search_string)
url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_search_string}&start=0&max_results={NB_PAPERS}"

data = urllib.request.urlopen(url)
print(data.read().decode('utf-8'))