import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):

    number_of_pages = len(corpus)
    number_of_neighbours = len(corpus[page])
    probability_distribution = dict()
    if(number_of_neighbours == 0):
        for new_page in corpus.keys():
            probability_distribution[new_page] = 1 / number_of_pages
        return probability_distribution
    for new_page in corpus.keys():
        probability_distribution[new_page] = (1 - damping_factor) / number_of_pages
    for new_page in corpus[page]:
        probability_distribution[new_page] += damping_factor /  number_of_neighbours
    return probability_distribution
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """


def sample_pagerank(corpus, damping_factor, n):
    pages = corpus.keys()
    current_page = random.choice(list(pages))
    result_sample = {key:0 for key in pages}
    org_n = n
    while(n > 0):
        result_sample[current_page] += 1
        trans_model = transition_model(corpus, current_page, damping_factor)

        current_page = random.choices(list(trans_model.keys()), weights=trans_model.values(), k=1)[0]
        n -= 1
    for page in result_sample.keys():
        result_sample[page] = result_sample[page] / org_n
    return result_sample
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages_number = len(corpus)
    old_dict = {}
    new_dict = {}

    # assigning each page a rank of 1/n, where n is total number of pages in the corpus
    for page in corpus:
        old_dict[page] = 1 / pages_number

    # repeatedly calculating new rank values basing on all of the current rank values
    while True:
        for page in corpus:
            temp = 0
            # if(len(corpus[page]) == 0):
            #     temp += old_dict[neighbours] / pages_number
            # else:
            for link_to_page in corpus:
                if page in corpus[link_to_page]:
                    temp += old_dict[link_to_page] / len(corpus[link_to_page])
                if len(corpus[link_to_page]) == 0:
                    temp += (old_dict[link_to_page]) / len(corpus)
            temp *= damping_factor
            temp += (1 - damping_factor) / pages_number
            new_dict[page] = temp
        difference = max([abs(new_dict[x] - old_dict[x]) for x in old_dict])
        if difference < 0.001:
            break
        old_dict = new_dict.copy()
    return old_dict


if __name__ == "__main__":
    main()
