from Model.Glassdoor import Glassdoor
from Model.Indeed import Indeed

def WebChooser(website, url):
    websites = {
        "indeed": Indeed,
        "glassdoor": Glassdoor
    }
    return websites[website](url)
