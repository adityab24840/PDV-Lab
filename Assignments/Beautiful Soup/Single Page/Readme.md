# GitHub Repository Scraper

This script scrapes repository information from a GitHub profile page and saves it to a CSV file.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Example Output](#example-output)
- [Conclusion](#conclusion)

## Requirements

- `Python` (3.6 or higher)
- `bs4` (Beautiful Soup) library
- `pandas` library
## Usage

1. Install the required libraries using the following commands:

```sh
   pip install requests-html pandas
```
2. Clone or download this repository.

3. Run the scrape_repositories.py script:
```sh
python scrape_repositories.py
```

4. The script will scrape repository names and creation dates from the provided GitHub profile and save the information to a file named repositories.csv.

## Example Output

The script will generate a CSV file named repositories.csv containing repository information in the following format:

``` css
Name,Date
repository1,YYYY-MM-DD
repository2,YYYY-MM-DD
...

```

## Conclusion
This script provides a simple way to gather repository information from a GitHub profile page. You can easily adapt and extend it for other purposes, such as analyzing repository trends or keeping track of your own projects.